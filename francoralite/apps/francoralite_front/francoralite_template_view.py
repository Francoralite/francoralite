from django.shortcuts import render
from django.utils.decorators import classonlymethod
from django.utils.translation import gettext_lazy as _
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

import francoralite.apps.francoralite_front.tools as tools


class FrancoraliteFormView(FormView):
    default_403_error_message = _('Accès interdit.')

    def get(self, request, *args, **kwargs):

        record_id = kwargs.get('id')

        # Obtain values of the record
        record = tools.request_api(self.api_url_prefix + str(record_id))
        form = self.form_class(initial=record)

        return render(request, self.template_name, {
            'form': form,
            'id': record_id,
            self.template_variable_name: record,
        })

    def post(self, request, *args, **kwargs):
        return tools.patch(self.entity_name, self.form_class, request,
                           *args, **kwargs)


class FrancoraliteTemplateView(TemplateView):
    default_403_error_message = _('Accès interdit.')

    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super(FrancoraliteTemplateView, cls).as_view(**initkwargs)
        view.cls = cls
        return view
