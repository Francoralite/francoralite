from django.shortcuts import render
from django.utils.decorators import classonlymethod
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from urllib.parse import urlparse, parse_qs

from francoralite.apps.francoralite_front import tools


class FrancoraliteFormView(FormView):
    is_front_view = True

    def get_initial(self):
        initial = super().get_initial()
        record_id = self.kwargs.get('id')
        record = tools.request_api(self.api_url_prefix + str(record_id))
        initial.update(record)

        return initial

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        record_id = kwargs.get('id')

        # Obtain values of the record
        record = tools.request_api(self.api_url_prefix + str(record_id))
        form = self.form_class(initial=self.get_initial())

        return render(request, self.template_name, {
            'form': form,
            'id': record_id,
            self.template_variable_name: record,
        })

    def post(self, request, *args, **kwargs):
        return tools.patch(self.entity_name, self.form_class, request,
                           *args, **kwargs)


class FrancoraliteTemplateView(TemplateView):
    is_front_view = True

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

            # Obtain params values of the request
            parsed_url = urlparse(self.api_url)
            params = parse_qs(parsed_url.query)
            
            api_response = tools.request_api(
                '%s%slimit=%s&offset=%s&ordering=%s' % (
                    self.api_url,
                    '&' if '?' in self.api_url else '?',
                    self.PAGE_SIZE,
                    offset,
                    params['ordering'][0] if 'ordering' in params else '',
                )
            )
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
                'ordering': self.request.GET.get('ordering', None),
            }

            complementary_data_loaders = getattr(self, 'complementary_data_loaders', None)
            if complementary_data_loaders:
                for record in context[self.context_results_name]:
                    for loader in complementary_data_loaders:
                        loader.complete_record(record)
                for loader in complementary_data_loaders:
                    loader.complete_context(context)

        except Exception as err:
            context[self.context_results_name] = []
            context['error'] = err

        return context
