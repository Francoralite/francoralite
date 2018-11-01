# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>


from django.db.models import(
    CASCADE,
    OneToOneField,
    TextField,
    ManyToManyField
    )
from django.db.models.signals import post_save
from django.db import models
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from telemeta.models.collection import MediaCollection
from telemeta.models.core import ModelCore, MetaCore
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class ExtMediaCollection(ModelCore):
    """
    Telemeta MediaCollection model extend
    """
    media_collection = OneToOneField(MediaCollection, on_delete=CASCADE)

    mission = models.ForeignKey(
            'telemeta_api.Mission',
            related_name='collection',
            verbose_name=_('Mission'), blank=True, default="")
    location_details = MarkdownxField(blank=True)
    cultural_area = TextField(
        'cultural area',
        help_text=('Aire culturelle ; Aire culturelle'),
        default="", blank=True)
    language = TextField(
        'langage',
        help_text=('Langage ; langage'),
        default="", blank=True)

    class Meta(MetaCore):
        app_label = 'telemeta_api'
        db_table = 'ext_media_collection'


@property
def description_markdown(self):
    return markdownify(self.description)


@property
def booklet_description_markdown(self):
    return markdownify(self.booklet_description)


@property
def location_details_markdown(self):
    return markdownify(self.location_details)


@receiver(post_save, sender=MediaCollection)
def create_media_collection_extended(sender, instance, created, **kwargs):
    if created:
        ExtMediaCollection.objects.create(media_collection=instance)


@receiver(post_save, sender=MediaCollection)
def save_media_collection_extended(sender, instance, **kwargs):
    instance.extmediacollection.save()
