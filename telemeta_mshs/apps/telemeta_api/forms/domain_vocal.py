# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.forms import ModelForm
from telemeta.models import DomainVocal


class DomainVocalForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(DomainVocalForm, self).__init__(*args, **kwargs)

    class Meta:
        model = DomainVocal
        exclude = []
