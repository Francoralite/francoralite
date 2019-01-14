# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


from django.forms import ModelForm
from telemeta.models import Thematic


class ThematicForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ThematicForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Thematic
        exclude = []