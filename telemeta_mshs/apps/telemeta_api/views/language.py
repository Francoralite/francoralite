# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from rest_framework import viewsets
from telemeta.models.language import Language as LanguageModel
from ..serializers.language import LanguageSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    """
    Language management
    """

    queryset = LanguageModel.objects.all()
    serializer_class = LanguageSerializer
