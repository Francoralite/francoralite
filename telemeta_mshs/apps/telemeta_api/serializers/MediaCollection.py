# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>
from rest_framework import serializers

from telemeta.models.collection import MediaCollection as MediacollectionModel


class MediacollectionSerializer(serializers.ModelSerializer):
    """
    Common serializer for all MediaCollection actions
    """

    # FIXIT ----
    title = serializers.CharField(required=True)
    alt_title = serializers.CharField()
    creator = serializers.CharField()
    description = serializers.CharField()
    recording_context = serializers.StringRelatedField()
    recorded_from_year = serializers.IntegerField()
    recorded_to_year = serializers.IntegerField()
    year_published = serializers.IntegerField()
    public_access = serializers.CharField()

    collector = serializers.CharField()
    publisher = serializers.StringRelatedField()
    publisher_collection = serializers.StringRelatedField()
    publisher_serial = serializers.CharField()
    booklet_author = serializers.CharField()
    reference = serializers.CharField()
    external_references = serializers.CharField()

    auto_period_access = serializers.BooleanField()
    legal_rights = serializers.StringRelatedField()

    code = serializers.CharField()
    old_code = serializers.CharField()
    acquisition_mode = serializers.StringRelatedField()
    cnrs_contributor = serializers.CharField()
    copy_type = serializers.StringRelatedField()
    metadata_author = serializers.StringRelatedField()
    booklet_description = serializers.CharField()
    publishing_status = serializers.StringRelatedField()
    status = serializers.StringRelatedField()
    alt_copies = serializers.CharField()
    comment = serializers.CharField()
    metadata_writer = serializers.StringRelatedField()
    archiver_notes = serializers.CharField()
    items_done = serializers.CharField()
    collector_is_creator = serializers.BooleanField()
    is_published = serializers.BooleanField()
    conservation_site = serializers.CharField()

    media_type = serializers.StringRelatedField()
    approx_duration = '00:20:00'
    physical_items_num = serializers.IntegerField()
    original_format = serializers.StringRelatedField()
    physical_format = serializers.StringRelatedField()
    ad_conversion = serializers.StringRelatedField()

    alt_ids = serializers.CharField()
    travail = serializers.CharField()

    class Meta:
        model = MediacollectionModel
        fields = '__all__'
