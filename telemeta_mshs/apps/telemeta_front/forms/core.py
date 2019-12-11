# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

import requests
from settings import FRONT_HOST_URL


class Core():

    @staticmethod
    def get_choices(entity="", label_field=""):
        """
            Generate a list of choices to feed a ChoiceField
            :param entity: name of the entity to refer
            :param label_field: label of the entity to display
            :return: a list of choices
        """
        choices = []
        # Nothing to do, when parameters are empty
        if entity == "" or label_field == "":
            return choices

        # Calling the entity via the API
        response = requests.get(
            FRONT_HOST_URL+'/api/' + entity)
        if response.status_code == 200:
            # Make a JSON structure
            data = response.json()

            # Feed the choices
            for a in data:
                choices.append((a['id'], a[label_field]))
            choices.append(("", ""))

        return choices
