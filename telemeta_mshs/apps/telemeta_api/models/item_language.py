# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>


from django.db import models
from django.utils.translation import ugettext_lazy as _
from .item import Item
from .language import Language


class ItemLanguage(models.Model):
    # Description of the table
    "Language(s) of an item"

    # List of the fields
    item = models.ForeignKey(Item, verbose_name=_('item'),
            on_delete=models.CASCADE)
    language = models.ForeignKey(Language,
                                 verbose_name=_('language'),
                                 on_delete=models.PROTECT)

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'api_item_language'
        verbose_name_plural = _('item_languages')
