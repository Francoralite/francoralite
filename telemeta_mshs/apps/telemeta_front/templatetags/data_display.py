# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django import template
from django.utils.translation import ugettext_lazy as _
from telemeta_front.errors import APPLICATION_ERRORS

register = template.Library()


@register.simple_tag
def field_data(label, data, empty=True):
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

    if empty is False and str_data == "":
        code = ""
    else:
        code = "<dl class=\"container_data\"><dt class=\"libelle\">"
        code = code + str_label + "</dt> <dd class=\"donnee\" >"
        code = code + str_data + "</dd> </dl>"

    return code


@register.simple_tag
def field_data_bool(label, data):
    icon = ""
    if data is True:
        icon = "glyphicon-ok "
    code = "<dl class=\"container_data\"><dt class=\"libelle\">"
    code = code + str(label) + "</dt> <dd class=\" center glyphicon "
    code = code + icon + "donnee\" >"
    code = code + "</dd> </dl>"

    return code


@register.simple_tag
def display_error(error="0"):
    url_error = {
        'HTTP_API_401': 'inc/non_authentified.html',
        'HTTP_API_404': 'inc/not_present.html',
        'KEY_ERROR': 'inc/key_error.html',
    }
    code = error
    for key, value in url_error.iteritems():
        if error == APPLICATION_ERRORS[key]:
            code = template.loader.get_template(value)

    if error != "0" and error != '':
        # Display the code of the error
        html = "<i>ERR : " + error + "</i>"
        # Render the template to HTML source code
        if isinstance(code, template.__class__):
            html += code.render()
        return html
    return code


@register.inclusion_tag('inc/modal-delete.html')
def modal_delete():
    return {}


@register.inclusion_tag('inc/select-vue-item.html', takes_context=True)
def select_vue_item(context):
    if 'id' in context:
        return {
            'id': context['id'],
            'url_external': context['url_external'],
        }
    return {}


@register.inclusion_tag('inc/select-vue-collection.html', takes_context=True)
def select_vue_collection(context):
    if 'id' in context:
        return {
            'id': context['id'],
        }
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


@register.filter
def domains(self):
    values = str(self)
    labels = ""
    DOMAINS = (
        ('T', _(u"Témoignage")),
        ('C', _(u"Chanson")),
        ('A', _(u"Autre expression vocale")),
        ('I', _(u"Expression instrumentale")),
        ('R', _(u"Conte ou récit légendaire"))
    )
    for (d, lib) in DOMAINS:
        if d in values:
            if len(labels) > 0:
                labels = labels + ", "
            labels = labels + str(lib)

    return labels


@register.filter
def get_obj_attr(obj, attr):
    # return getattr(obj, attr)
    return obj[attr]


@register.inclusion_tag('inc/related-list.html')
def related_list(*args, **kwargs):
    return {
        'libelle': kwargs.get('libelle', ""),
        'items': kwargs['items'],
        'url_detail': kwargs.get('url_detail', ""),
        'field': kwargs['field'],
        'field2': kwargs.get('field2', ""),
        'empty': kwargs.get('empty', True),
        }


@register.inclusion_tag('inc/display_documents.html', takes_context=True)
def display_documents(context):
    if 'documents' in context:
        return {
            'documents': context['documents'],
        }
    return {}


@register.inclusion_tag('inc/nakala_button.html')
def nakala_button(*args, **kwargs):
    return{}
