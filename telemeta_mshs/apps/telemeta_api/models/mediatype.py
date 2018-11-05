# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>


from telemeta.models.enum import Enumeration, MetaEnumeration
from django.utils.translation import ugettext_lazy as _


class MediaType(Enumeration):
    "Media Type"

    class Meta(MetaEnumeration):
        app_label = 'telemeta_api'
        db_table = 'mediatype'
        verbose_name = _("mediatype")
