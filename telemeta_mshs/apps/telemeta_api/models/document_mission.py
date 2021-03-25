# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from django.utils.translation import gettext_lazy as _
from django.db import models
from .document import Document
from .mission import Mission


class DocumentMission(Document):
    "Mission related document"

    mission = models.ForeignKey(
        Mission,
        related_name="related_document",
        verbose_name=_('mission'),
        on_delete=models.CASCADE
        )

    class Meta:
        app_label = 'telemeta_api'
        db_table = 'api_document_mission'
        verbose_name_plural = _('document')
        ordering = ['mission', 'title']
