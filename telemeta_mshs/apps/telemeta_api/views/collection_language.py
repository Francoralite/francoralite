# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.db.models.query import QuerySet
from rest_framework import viewsets
from ..models.collection_language import (
        CollectionLanguage as CollectionLanguageModel)
from ..serializers.collection_language import CollectionLanguageSerializer


class CollectionLanguageViewSet(viewsets.ModelViewSet):
    """
    CollectionLanguage management
    """

    queryset = CollectionLanguageModel.objects.all()
    serializer_class = CollectionLanguageSerializer

    def get_queryset(self):
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = CollectionLanguageModel.objects.filter(
                collection_id=self.kwargs['collection_pk'])
        return queryset
