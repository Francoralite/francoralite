# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>
from rest_framework import serializers

from .asymetric_related_field import AsymetricRelatedField

# Add nested/related serializers
from .item import ItemSerializer
from .ref_laforte import RefLaforteSerializer

from ..models.item_laforte import (
    ItemLaforte as ItemLaforteModel
)


class ItemLaforteSerializer(serializers.ModelSerializer):
    """
    Common serializer for all ItemLaforte actions
    """

    item = AsymetricRelatedField.from_serializer(
        ItemSerializer, kwargs={'required': True}
    )
    laforte = AsymetricRelatedField.from_serializer(
        RefLaforteSerializer, kwargs={'required': True}
    )

    class Meta:
        model = ItemLaforteModel
        fields = '__all__'
