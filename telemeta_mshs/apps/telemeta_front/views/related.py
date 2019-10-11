# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
from rest_framework import status
import requests
import json
from settings import FRONT_HOST_URL


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
            FRONT_HOST_URL + '/api/collection/' + \
            str(collection["id"]) + '/' + nested + '/'
        # Create the related records
        write_relations(collection["id"],
                        "collection", items,
                        url, related, headers)

    url_performances = \
        FRONT_HOST_URL + '/api/collection/' + \
        str(collection["id"]) + '/performance/'
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
                pass

        if("informers" in performance):
            url_musicians = \
                FRONT_HOST_URL + '/api/collection/' + \
                str(collection["id"]) + '/performance/' + \
                str(performance["id"]) + '/musician/'
            write_relations(performance["id"],
                            "performance_collection",
                            performance["informers"],
                            url_musicians,
                            "musician",
                            headers)
        index = index + 1


def write_item_related(id_main, request):
    related = [
        ["collector", "collectors"],
        ["informer", "informers"],
        ["author", "authors"],
        ["compositor", "compositors"],
        ["thematic", "thematics"],
        ["dance", "dances"],
        ["usefulness", "usefulnesses"],
        ["domain_song", "domainsongs"],
        ["domain_vocal", "domainvocals"],
        ["domain_music", "domainmusics"],
        ["domain_tale", "domaintales"],
        ["musical_organization", "musical_organizations"],
        ["musical_group", "musical_groups"]
    ]

    for rel_item in related:
        write_relations(
            id_main,
            "item",
            json.loads(request.POST[rel_item[1]]),
            FRONT_HOST_URL + '/api/item/' +
            str(id_main) + '/' + rel_item[0] + '/',
            rel_item[0]
        )


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
    if list_related != {} and list_related is not None:
        # create a dict to know the id of the related record

        for item in list_related:
            if name_related != "":
                # Add the item ID to the set
                set_related.add(item[name_related]["id"])
                # Feed the dict
                dict_related[item[name_related]["id"]] = item["id"]
            else:
                # Add the item ID to the set
                set_related.add(item["id"])
                # Feed the dict
                dict_related[item["id"]] = item["id"]

        # No exists in list of related : delete the related record
        list_delete = set_related.difference(set_selected)
        for id in list_delete:
            requests.delete(url_related + str(dict_related[id]) + "/",
                            headers=headers)

        # No exists in list of selected : create the related record
        for item in list_to_create:
            try:
                create_record(url_related, item[0], item[1], headers)
            except Exception:
                pass

        list_intersect = set_selected.intersection(set_related)
        for id in list_intersect:
            update_record(url_related, id, dict_selected[id], headers)

    if list_related is None:
        for item in list_to_create:
            try:
                create_record(url_related, item[0], item[1], headers)
            except Exception:
                pass


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
    response = requests.put(
        url_related + str(id) + "/",
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
