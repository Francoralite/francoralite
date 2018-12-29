# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import template
from django.utils.translation import ugettext_lazy as _

register = template.Library()


@register.simple_tag
def field_data(label, data):
    try:
        str_label = str(label)
    except Exception:
        str_label = label

    try:
        str_data = str(data)
        if str_data == "None":
            str_data = ""
    except Exception:
        str_data = data

    code = "<span class=\"container_data\"><span class=\"libelle\">"
    code = code + str_label + "</span> <span class=\"donnee\" >"
    code = code + str_data + "</span> </span>"

    return code


@register.simple_tag
def field_data_bool(label, data):
    icon = ""
    if data is True:
        icon = "glyphicon-ok "
    code = "<span class=\"container_data\"><span class=\"libelle\">"
    code = code + str(label) + "</span> <span class=\" center glyphicon "
    code = code + icon + "donnee\" >"
    code = code + "</span> </span>"

    return code


@register.inclusion_tag('inc/modal-delete.html')
def modal_delete():
    return {}


@register.inclusion_tag('inc/buttons-form.html', takes_context=True)
def buttons_form(context):
    request = context['request']
    url_back = "#"
    if 'HTTP_REFERER' in request.META:
        url_back = request.META['HTTP_REFERER']
    return {'url_back': url_back}


@register.filter
def virgule(self):
    return str(self).replace(",", ".")


@register.filter
def public_access(self):
    choices = {}
    choices['none'] = _(u"Aucun")
    choices['metadata'] = _(u"Meta-données")
    choices['partial'] = _(u"Partiel")
    choices['full'] = _(u"Complet")
    return choices[self]
