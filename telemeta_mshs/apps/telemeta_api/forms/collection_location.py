# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from django.forms import ModelForm
from .models import collection_location


class Collection_locationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(Collection_locationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = collection_location
        exclude = []
