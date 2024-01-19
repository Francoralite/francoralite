# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
from rest_framework import serializers

from .item import ItemSerializer
from .language import LanguageSerializer
from .asymetric_related_field import AsymetricRelatedField

from ..models.item_language import (
    ItemLanguage as ItemLanguageModel)


class ItemLanguageSerializer(serializers.ModelSerializer):
    """
    Common serializer for all ItemLanguage actions
    """

    # Fields of the serializer
    item = AsymetricRelatedField.from_serializer(
        ItemSerializer, kwargs={'required': True})
    language = AsymetricRelatedField.from_serializer(
        LanguageSerializer, kwargs={'required': True})

    class Meta:
        model = ItemLanguageModel
        fields = '__all__'
