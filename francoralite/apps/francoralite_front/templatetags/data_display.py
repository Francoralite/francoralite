# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

import json

from django import template
from django.forms.widgets import CheckboxInput, CheckboxSelectMultiple, HiddenInput
from django.utils.datastructures import MultiValueDict
from django.utils.html import format_html, format_html_join
from django.utils.http import urlencode
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from francoralite_front.errors import APPLICATION_ERRORS

register = template.Library()


@register.simple_tag(takes_context=True)
def current_url_params(context, **kwargs):
    # Get previous parameters
    params = MultiValueDict(context['request'].GET)
    # Remove parameters to be replaced, otherwise new are added, not replaced
    for key in kwargs:
        if key in params:
            del params[key]
    # Add new parameters
    params.update(kwargs)
    # Remove empty parameters
    for key in tuple(params):
        if not any(params.getlist(key)):
            del params[key]
    # Build new query string
    return '?' + urlencode(params, doseq=True)


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

    return mark_safe(code)

@register.simple_tag
def field_data_id(field, data, empty=True, truncate=0):
    try:
        str_label = str(field.label)
    except Exception:
        str_label = field.label

    try:
        str_data = str(data)
        if str_data == "None" or str_data == "<p>None</p>":
            str_data = ""
    except Exception:
        str_data = data
        
    if truncate>0:
        str_data = str_data[:truncate] + " ..."

    if empty is False and str_data == "":
        code = ""
    else:
        code = "<dl class=\"container_data\"><dt class=\"libelle\">"
        code = code + str_label + "</dt> <dd id=\"" + field.id_for_label + "\" class=\"donnee\" >"
        code = code + str_data + "</dd> </dl>"

    return mark_safe(code)


@register.simple_tag
def field_data_bool(label, data):
    icon = ""
    if data is True:
        icon = "glyphicon-ok "
    code = "<dl class=\"container_data\"><dt class=\"libelle\">"
    code = code + str(label) + "</dt> <dd class=\" center glyphicon "
    code = code + icon + "donnee\" >"
    code = code + "</dd> </dl>"

    return mark_safe(code)


@register.simple_tag
def field_editor(field):
    if isinstance(field.field.widget, HiddenInput):
        return field

    elif isinstance(field.field.widget, CheckboxInput):
        inner_html = format_html(
            '<div class="checkbox"><label for="{}">{} {}</label>{}</div>',
            field.id_for_label,
            field,
            field.label,
            field.errors,
        )

    elif isinstance(field.field.widget, CheckboxSelectMultiple):
        value = field.value()
        widget = CheckboxInput()
        inner_html = format_html(
            '<label class="control-label">{}</label><div id="id_{}">{}</div>',
            field.label,
            field.name,
            format_html_join(
                '',
                '<div class="checkbox"><label for="{}">{} {}</label></div>',
                (
                    (
                        f'id_{field.name}_{context["index"]}',
                        widget.render(
                            field.name,
                            value is not None and context['value'] in value,
                            {
                                'id': f'id_{field.name}_{context["index"]}',
                                'value': context['value'],
                            },
                        ),
                        context['label'],
                    ) for context in field.field.widget.subwidgets(field.name, value)
                ),
            ),
        )

    else:
        attrs = field.field.widget.attrs
        attrs['class'] = f'form-control {attrs.get("class") or ""}'.strip()
        inner_html = format_html(
            '<label class="control-label" for="{}">{}</label>{}{}',
            field.id_for_label,
            field.label,
            field,
            field.errors,
        )

    return format_html(
        '<div class="{}">{}</div>',
        ' '.join(filter(None, [
            'form-group',
            'has-error' if field.errors else '',
            'has-warning' if field.field.required else '',
        ])),
        inner_html,
    )


@register.simple_tag
def display_error(error="0"):
    url_error = {
        'HTTP_API_401': 'inc/non_authentified.html',
        'HTTP_API_404': 'inc/not_present.html',
        'KEY_ERROR': 'inc/key_error.html',
    }
    code = error
    for key, value in url_error.items():
        if error == APPLICATION_ERRORS[key]:
            code = template.loader.get_template(value)

    if error != "0" and error != '':
        # Display the code of the error
        html = "<i>ERR : " + error + "</i>"
        # Render the template to HTML source code
        if isinstance(code, template.__class__):
            html += code.render()
        return html
    return mark_safe(code)


@register.inclusion_tag('inc/modal-delete.html')
def modal_delete():
    return {}


@register.inclusion_tag('inc/select-vue-personne.html', takes_context=True)
def select_vue_personne(context):
    if 'id' in context:
        return {
            'id': context['id'],
        }
    return {}


@register.inclusion_tag('inc/select-vue-item.html', takes_context=True)
def select_vue_item(context):
    if 'id' in context:
        return {
            'id': context['id'],
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


@register.filter(name='json')
def json_dumps(data):
    return json.dumps(data)


@register.filter(name='range')
def range_filter(length, offset=0):
    return range(offset, length + offset)
