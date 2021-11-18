# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

import requests


def get_token(test, username='contributeur'):
    r = requests.post(
        'http://keycloak.francoralite.localhost:8080/auth/realms/francoralite/protocol/openid-connect/token', # noqa
        data={
            'client_id': 'admin-cli',
            'username': username,
            'password': 'password',
            'grant_type': 'password',
        })
    token = r.json()['access_token']

    test.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
