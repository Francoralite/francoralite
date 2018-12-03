# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
from rest_framework import status
import requests
from requests.exceptions import RequestException


def create_related_records(list_related, url_related, name_related, id_main):
    for related in list_related:
        write_related_record(related["id"], url_related, name_related, id_main)


def write_related_record(id_related, url_related, name_related, id_main):
    # Compose a collection-related record
    data = {}
    data["collection"] = str(id_main)
    data[name_related] = str(id_related)

    # Create a related record
    response = requests.post(
        url_related,
        data=data)
    if response.status_code \
            != status.HTTP_201_CREATED:
        raise Exception(response.status_code)


def compare_related(selected, url_related, name_related, id_main):
    # Query the list of related records in the database
    response = requests.get(url_related)
    if response.status_code == status.HTTP_200_OK:
        # values of the related records
        list_related = response.json()

        set_related = set()
        # create a dict to know the id of the related record
        dict_related = {}
        for item in list_related:
            # Add the item ID to the set
            set_related.add(item[name_related]["id"])
            # Feed the dict
            dict_related[item[name_related]["id"]] = item["id"]

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
                write_related_record(id, url_related, name_related, id_main)
            except RequestException:
                pass
