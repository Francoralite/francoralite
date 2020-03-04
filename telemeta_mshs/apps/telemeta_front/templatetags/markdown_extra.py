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
    return md.markdown(value, extensions=[
        'markdown.extensions.nl2br',
        'markdown.extensions.tables',
        'markdown.extensions.fenced_code'])


@register.inclusion_tag('inc/markdown_editor.html')
def markdown_editor(*args, **kwargs):
    return{
        'component': kwargs['component'],
    }
