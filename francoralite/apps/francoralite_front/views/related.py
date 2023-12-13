# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
from rest_framework import status
import requests
import json
from django.conf import settings


class related():
    def __init__(self, main, main_field, id_list):
        self.main_entity = main  # ID of the main entity
        self.main_field = main_field  # name of the main entity
        self.id_list = id_list

    def set_id_data(self):
        self.main_data[self.main_field] = self.main_entity

    def add_data(self, data):
        self.main_data = data

    def add_relation(self, relation):
        self.relation_entity = relation

    def update_data(self, new_data):
        self.main_data = new_data


def write_fond_related(fond, request, headers):
    url_documents = \
        settings.FRONT_HOST_URL + '/api/fond/' + \
        str(fond["id"]) + '/document'

    documents_selected = json.loads(request.POST['media'])

    # Use only the fond ID (not all the data of a fond)
    for doc in documents_selected:
        doc["fond"] = fond["id"]

    write_relations(fond["id"],
                    "document_fond",
                    documents_selected,
                    url_documents,
                    "",
                    headers)


def write_mission_related(mission, request, headers):
    url_documents = \
        settings.FRONT_HOST_URL + '/api/mission/' + \
        str(mission["id"]) + '/document'

    documents_selected = json.loads(request.POST['media'])

    # Use only the mission ID (not all the data of a mission)
    for doc in documents_selected:
        doc["mission"] = mission["id"]

    write_relations(mission["id"],
                    "document_mission",
                    documents_selected,
                    url_documents,
                    "",
                    headers)


def write_collection_related(collection, request, headers):

    list_related = [
        'collector',
        'informer',
        'location',
        'language',
        'publisher',
        'performance'
    ]

    for related in list_related:
        items = json.loads(request.POST[related + 's'])
        nested = related
        if related == 'collector':
            nested = 'collectors'
        url = \
            settings.FRONT_HOST_URL + '/api/collection/' + \
            str(collection["id"]) + '/' + nested
        if related == 'performance':
            for item in items:
                if "emit" in item:
                    if item["emit"] == '0' or item["emit"] == 0:
                        del item["emit"]
            related = ""

        # Create the related records
        write_relations(collection["id"],
                        "collection", items,
                        url, related, headers)

    url_performances = \
        settings.FRONT_HOST_URL + '/api/collection/' + \
        str(collection["id"]) + '/performance'
    index = 0
    # Request the performances ordered by ID
    performances = query_related(
        url_performances + "?ordering=id", headers)

    performances_selected = json.loads(request.POST['performances'])

    for performance in performances_selected:
        if "id" not in performance:
            # The performance wasn't exist.
            # Search and retrieve the ID of the new performance
            # in the database
            try:
                performance["id"] = performances[index]["id"]
            except Exception:
                performance["id"] = 0

        if "informers" not in performance:
            performance["informers"] = []
        url_musicians = \
            settings.FRONT_HOST_URL + '/api/collection/' + \
            str(collection["id"]) + '/performance/' + \
            str(performance["id"]) + '/musician'
        write_relations(performance["id"],
                        "performance_collection",
                        performance["informers"],
                        url_musicians,
                        "musician",
                        headers)
        index = index + 1

    # Documents related (media)
    url_documents = \
        settings.FRONT_HOST_URL + '/api/collection/' + \
        str(collection["id"]) + '/document'
    media = request.POST['media']
    if media:
        documents_selected = json.loads(media)
    else:
        documents_selected = []

    # Use only the collection ID (not all the data of a collection)
    for doc in documents_selected:
        doc["collection"] = collection["id"]

    write_relations(collection["id"],
                    "document_collection",
                    documents_selected,
                    url_documents,
                    "",
                    headers)


def write_item_related(id_main, request, headers):
    related = [
        ["collector", "collectors"],
        ["informer", "informers"],
        ["author", "authors"],
        ["compositor", "compositors"],
        ["keyword", "keywords"],
        ["thematic", "thematics"],
        ["dance", "dances"],
        ["usefulness", "usefulnesses"],
        ["domain_song", "domainsongs"],
        ["domain_vocal", "domainvocals"],
        ["domain_music", "domainmusics"],
        ["domain_tale", "domaintales"],
        ["musical_organization", "musical_organizations"],
        ["musical_group", "musical_groups"],
        ["coirault", "coiraults"],
        ["language", "languages"],
    ]

    for rel_item in related:

        write_relations(
            id_main["id"],
            "item",
            json.loads(request.POST[rel_item[1]]),
            settings.FRONT_HOST_URL + '/api/item/' +
            str(id_main["id"]) + '/' + rel_item[0],
            rel_item[0],
            headers=headers
        )

    # Documents related (media)
    url_documents = \
        settings.FRONT_HOST_URL + '/api/item/' + \
        str(id_main["id"]) + '/document'

    documents_selected = json.loads(request.POST['media'])

    # Use only the item ID (not all the data of an item)
    for doc in documents_selected:
        doc["item"] = id_main["id"]

    write_relations(id_main["id"],
                    "document_item",
                    documents_selected,
                    url_documents,
                    "",
                    headers)

    # Performances ---------------
    url_performances = \
        settings.FRONT_HOST_URL + '/api/item/' + \
        str(id_main["id"]) + '/performance'

    performances_selected = json.loads(request.POST['performances'])

    # Use only the item ID (not all the data of an item)
    for perf in performances_selected:
        perf["item"] = id_main["id"]

    write_relations(id_main["id"],
                    "item_performance",
                    performances_selected,
                    url_performances,
                    "performance",
                    headers)


def write_relations(id_main,
                    name_main, selected, url_related, name_related, headers):

    list_selected = []
    list_to_create = []  # list of the related records to create
    dict_selected = {}
    set_selected = set()
    i = 0  # ordering number of the selected

    # Every selected item is parsed and stored in an object
    for item in selected:
        # Selected entity
        obj = related(id_main, name_main, i)
        obj.add_data(item)

        list_selected.append((item, obj))
        # Is there an item ID ?
        if "id" in item:
            # Add the item ID to the set.
            # It will be a link between the set and the list
            set_selected.add(item["id"])
            # ... and with the dictionnary
            dict_selected[item["id"]] = obj
        else:
            list_to_create.append((item, obj))
        i = i + 1

    set_related = set()
    # Query the list of related records in the database
    list_related = query_related(url_related, headers)
    dict_related = {}

    if list_related != [] and list_related is not None:
        # create a dict to know the id of the related record
        for item in list_related:
            if name_related != "":
                ID = item[name_related]["id"]
                set_related.add(ID)
                # Feed the dict
                dict_related[ID] = item["id"]
            else:
                # Add the item ID to the set
                set_related.add(item["id"])
                # Feed the dict
                dict_related[item["id"]] = item["id"]

        if name_main == 'item_performance':
            new_perfs = set_selected.difference(set_related)
            for perf in new_perfs:
                # Create a related performance
                response = requests.post(
                    url_related,
                    data={
                        'item': id_main,
                        'performance': perf
                    },
                    headers=headers)
                if response.status_code \
                        != status.HTTP_201_CREATED:
                    raise Exception(response.status_code)

        # No exists in list of related : delete the related record
        list_delete = set_related.difference(set_selected)
        for id in list_delete:
            requests.delete(url_related + "/" + str(dict_related[id]),
                            headers=headers)

        # No exists in list of selected : create the related record
        for item in list_to_create:
            try:
                create_record(url_related, item[0], item[1], headers)
            except Exception:
                pass

        list_intersect = set_selected.intersection(set_related)
        for id in list_intersect:
            if name_main == 'item_performance':
                update_record(
                    url_related, dict_related[id], dict_selected[id], headers)
            else:
                update_record(url_related, id, dict_selected[id], headers)

    if list_related == []:
        for item in list_to_create:
            try:
                create_record(url_related, item[0], item[1], headers)
            except Exception:
                pass
        if name_main == 'item_performance':
            for perf in set_selected:
                # Create a related performance
                response = requests.post(
                    url_related,
                    data={
                        'item': id_main,
                        'performance': perf
                    },
                    headers=headers)
                if response.status_code \
                        != status.HTTP_201_CREATED:
                    raise Exception(response.status_code)


def create_record(url_related, item_selected, obj, headers):
    item_selected[obj.main_field] = obj.main_entity
    # Create a related record
    response = requests.post(
        url_related,
        data=item_selected,
        headers=headers)
    if response.status_code \
            != status.HTTP_201_CREATED:
        raise Exception(response.status_code)


def update_record(url_related, id, obj, headers):
    obj.set_id_data()
    # update a related record
    response = requests.patch(
        url_related + "/" + str(id),
        data=obj.main_data,
        headers=headers)
    if response.status_code \
            != status.HTTP_200_OK:
        raise Exception(response.status_code)


def query_related(url_related, headers):
    list_related = {}
    response = requests.get(url_related, headers=headers)
    if response.status_code == status.HTTP_200_OK:
        # values of the related records
        list_related = response.json()
        return list_related
