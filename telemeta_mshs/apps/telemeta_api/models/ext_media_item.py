# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>


from django.db.models import CASCADE, ForeignKey, OneToOneField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from telemeta.models.item import MediaItem
from telemeta.models.core import ModelCore, MetaCore
from .coupe import Coupe


class ExtMediaItem(ModelCore):
    """
    Telemeta MediaItem model extend
    """
    media_item = OneToOneField(MediaItem, on_delete=CASCADE)
    mshs_ch_coupe = ForeignKey(Coupe, blank=True, null=True, verbose_name=_('coupe'))

    class Meta(MetaCore):
        app_label = 'telemeta_api'
        db_table = 'ext_media_item'


@receiver(post_save, sender=MediaItem)
def create_media_item_extended(sender, instance, created, **kwargs):
    print dir(instance)
    if created:
        ExtMediaItem.objects.create(media_item=instance)


@receiver(post_save, sender=MediaItem)
def save_media_item_extended(sender, instance, **kwargs):
    print dir(instance)
    instance.extmediaitem.save()
