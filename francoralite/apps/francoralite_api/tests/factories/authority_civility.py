# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
"""
authority_civility factory to execute tests
"""

import factory
from ...models.authority_civility import AuthorityCivility
from .authority import AuthorityFactory
from .civility import CivilityFactory


class AuthorityCivilityFactory(factory.django.DjangoModelFactory):
    """
    AuthorityCivility factory
    """

    class Meta:
        model = AuthorityCivility
        django_get_or_create = ('authority', 'civility',)

    # Nested/related factories
    authority = factory.SubFactory(AuthorityFactory)
    civility = factory.SubFactory(CivilityFactory)
