from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestDance(EnumsTest):
    entity = 'dance'
    title = _('Genre de danse')
    data = [
        {"id":"1", "name":"polka", "notes":"Notes de polka"},
        {"id":"2", "name":"valse", "notes":"Notes de valse"},
        {"id":"3", "name":"mazurka", "notes":"Notes de mazurka"},
    ]
    new_data = {"name":"bourrée", "notes":"Notes de bourrée"}