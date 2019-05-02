from django.views.generic.base import TemplateView
from django.utils.decorators import classonlymethod


class FrancoraliteTemplateView(TemplateView):
    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super(FrancoraliteTemplateView, cls).as_view(**initkwargs)
        view.cls = cls
        return view
