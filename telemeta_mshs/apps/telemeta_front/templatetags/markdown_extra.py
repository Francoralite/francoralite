# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import template
from django.template.defaultfilters import stringfilter

import markdown as md

register = template.Library()


@register.filter
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code'])


@register.simple_tag
def markdown_editor(component):
    code = """
    <script type="text/javascript">
      var simplemde = new SimpleMDE({
         element: $("#""" + component + """")[0] ,
         toolbar: ["bold", "italic", "heading", "|",
          "quote","unordered-list", "ordered-list", "|","preview"],
       });
    </script>
    """

    return code
