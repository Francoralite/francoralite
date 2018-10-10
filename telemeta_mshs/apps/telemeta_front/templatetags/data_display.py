# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import template

register = template.Library()


@register.simple_tag
def field_data(label, data):
    str_data = str(data)
    if str_data == "None":
        str_data = ""
    code = "<span class=\"container_data\"><span class=\"libelle\">"
    code = code + str(label) + "</span> <span class=\"donnee\" >"
    code = code + str_data + "</span> </span>"

    return code
