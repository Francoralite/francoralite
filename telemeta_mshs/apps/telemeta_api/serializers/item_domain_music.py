# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
from rest_framework import serializers

from .asymetric_related_field import AsymetricRelatedField

# Add nested/related serializers
from .item import ItemSerializer
from .domain_music import DomainMusicSerializer

from ..models.item_domain_music import(
    ItemDomainMusic as ItemDomainMusicModel)

# Add nested/related table
from ..models.item_domain_music import ItemDomainMusic as ItemDomainMusicModel


class ItemDomainMusicSerializer(serializers.ModelSerializer):
    """
    Common serializer for all ItemDomainMusic actions
    """

    # fields of the serializer
    item = AsymetricRelatedField.from_serializer(
        ItemSerializer, kwargs={'required': True})
    domain_music = AsymetricRelatedField.from_serializer(
        DomainMusicSerializer, kwargs={'required': True})

    class Meta:
        model = ItemDomainMusicModel
        fields = '__all__'
