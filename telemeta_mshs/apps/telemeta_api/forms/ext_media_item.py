# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


import django.forms as forms
from django.forms import ModelForm
from telemeta.models import ExtMediaItem


class ExtMediaItemForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ExtMediaItemForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ExtMediaItem
        exclude = []
