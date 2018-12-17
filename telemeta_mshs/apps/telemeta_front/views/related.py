# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
from rest_framework import status
import requests
from requests.exceptions import RequestException


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


def write_relations(id_main, name_main, selected, url_related, name_related):
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
    list_related = query_related(url_related)
    dict_related = {}
    if list_related != {}:
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
            requests.delete(url_related + str(dict_related[id]) + "/")

        # No exists in list of selected : create the related record
        for item in list_to_create:
            create_record(url_related, item[0], item[1])

        list_intersect = set_selected.intersection(set_related)
        for id in list_intersect:
                update_record(url_related, id, dict_selected[id])


def create_record(url_related, item_selected, obj):
    item_selected[obj.main_field] = obj.main_entity
    # Create a related record
    response = requests.post(
        url_related,
        data=item_selected)
    if response.status_code \
            != status.HTTP_201_CREATED:
        raise Exception(response.status_code)


def update_record(url_related, id, obj):
    obj.set_id_data()
    # update a related record
    response = requests.put(
        url_related + str(id) + "/",
        data=obj.main_data)
    if response.status_code \
            != status.HTTP_200_OK:
        raise Exception(response.status_code)


def create_related_records(list_related,
                           url_related, name_related,
                           name_main, id_main, data_main):
    for related in list_related:
        write_related_record(related["id"],
                             url_related, name_related,
                             name_main, id_main, data_main)


def write_related_record(id_related,
                         url_related, name_related,
                         name_main, id_main, data_main):
    # Compose a collection-related record
    data = {}
    data[name_main] = str(id_main)
    data[name_related] = str(id_related)
    data.update(data_main)

    # Create a related record
    response = requests.post(
        url_related,
        data=data)
    if response.status_code \
            != status.HTTP_201_CREATED:
        raise Exception(response.status_code)


def update_related_record(id_related,
                          url_related, name_related,
                          name_main, id_main, data_main):
    # Compose a collection-related record
    data = {}
    data[name_main] = str(id_main)
    data[name_related] = str(id_related)
    data.update(data_main)

    # Update a related record
    response = requests.put(
        url_related + str(id_related) + "/",
        data=data)
    if response.status_code \
            != status.HTTP_200_OK:
        raise Exception(response.status_code)


def query_related(url_related):
    list_related = {}
    response = requests.get(url_related)
    if response.status_code == status.HTTP_200_OK:
        # values of the related records
        list_related = response.json()
    return list_related


def compare_related(selected, url_related, name_related,
                    name_main, id_main, data_main={}):
    """
    Comparison between items in a selected set and items in a related set.
    Delete items that don't appear in the selected set.
    Create items that don't appear in the related set.

    Parameters
    ----------
    selected : list
        List of the selected items.
    url_related : string
        url of the related entity.
    name_related : string
        Name of the related entity. Empty string if none.
    id_main : int
        Id of the main entity.

    """

    # Query the list of related records in the database
    list_related = query_related(url_related)
    if list_related != {}:
        set_related = set()
        # create a dict to know the id of the related record
        dict_related = {}
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

        # Create a set with the selected items
        set_selected = set()
        for item in selected:
            # Add the item ID to the set
            set_selected.add(item["id"])

        # No exists in list of related : delete the related record
        list_delete = set_related.difference(set_selected)
        for id in list_delete:
            requests.delete(url_related + str(dict_related[id]) + "/")

        # No exists in list of selected : create the related record
        list_create = set_selected.difference(set_related)
        for id in list_create:
            try:
                write_related_record(id,
                                     url_related,
                                     name_related,
                                     name_main, id_main, data_main)
            except RequestException:
                pass

        list_intersect = set_selected.intersection(set_related)
        for id in list_intersect:
            try:
                update_related_record(id,
                                      url_related,
                                      name_related,
                                      name_main, id_main, data_main)
            except RequestException:
                pass
