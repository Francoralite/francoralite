# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Cooperative Artefacts <artefacts.lle@gmail.com>

from django.forms import ModelForm
from telemeta.models import Item_domain_song


class Item_domain_songForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(Item_domain_songForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Item_domain_song
        exclude = []
