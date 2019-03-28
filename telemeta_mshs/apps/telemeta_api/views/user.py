# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets
# from telemeta.models.user import User as UserModel
from django.contrib.auth.models import User as UserModel
from ..serializers.user import CurrentUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    User management
    """

    queryset = UserModel.objects.all()
    serializer_class = CurrentUserSerializer
