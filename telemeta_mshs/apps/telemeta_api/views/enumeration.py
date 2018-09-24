# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from rest_framework import viewsets
from telemeta.models.enum import (
    PhysicalFormat)
from ..serializers.enumeration import EnumerationSerializer


class EnumerationViewSet(viewsets.ModelViewSet):
    """
    Enumeration management
    """

    queryset = PhysicalFormat.objects.all()
    serializer_class = EnumerationSerializer
