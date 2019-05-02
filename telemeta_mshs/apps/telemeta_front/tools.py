# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import status
from settings import FRONT_HOST_URL
import requests

from telemeta_front.errors import APPLICATION_ERRORS

HTTP_ERRORS = {
    status.HTTP_401_UNAUTHORIZED: APPLICATION_ERRORS['HTTP_API_401'],
    status.HTTP_403_FORBIDDEN: APPLICATION_ERRORS['HTTP_API_403'],
    status.HTTP_404_NOT_FOUND: APPLICATION_ERRORS['HTTP_API_404'],
}


def request_api(endpoint):
    """
    TODO: A renseigner
    """

    try:
        response = requests.get(
            FRONT_HOST_URL + endpoint)

        if response.status_code == status.HTTP_200_OK:
            return response.json

        raise Exception(HTTP_ERRORS[response.status_code])
    except Exception:
        raise
