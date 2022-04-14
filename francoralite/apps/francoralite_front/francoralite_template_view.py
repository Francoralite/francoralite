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


class FrancoralitePaginatedTemplateView(FrancoraliteTemplateView):

    PAGE_SIZE = 20

    def get_context_data(self, **kwargs):
        try:
            context = super(FrancoralitePaginatedTemplateView, self).get_context_data(**kwargs)

            try:
                page = int(self.request.GET.get('page', None)) or 1
                if page < 1:
                    page = 1
            except:
                page = 1
            offset = self.PAGE_SIZE * (page - 1)

            api_response = tools.request_api('%s%slimit=%s&offset=%s' % (
                self.api_url,
                '&' if '?' in self.api_url else '?',
                self.PAGE_SIZE,
                offset,
            ))

            results_count = api_response.get('count') or 0
            last_page = (results_count - 1) // self.PAGE_SIZE + 1

            context[self.context_results_name] = api_response.get('results', ())
            context['pagination'] = {
                'count': results_count,
                'page_size': self.PAGE_SIZE,
                'current_page': page,
                'has_previous': page > 1,
                'has_next': page * self.PAGE_SIZE < results_count,
                'first_item': min(self.PAGE_SIZE * (page - 1) + 1, results_count),
                'last_item': min(self.PAGE_SIZE * page, results_count),
                'last_page': last_page,
                'pages': tuple(range(1, last_page + 1)),
            }

        except Exception as err:
            context[self.context_results_name] = []
            context['error'] = err

        return context
