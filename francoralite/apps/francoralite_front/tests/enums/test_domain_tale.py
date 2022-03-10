from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestDomainTale(EnumsTest):
    entity = 'domain_tale'
    title = _('Genre de conte')
    data = [
        {"id":"1", "name":"conte facétieux", "notes":"Notes conte facétieux"},
        {"id":"2", "name":"récit", "notes":"Notes récit"}
    ]
    new_data = {"name":"conte merveilleux", "notes":"Notes conte merveilleux"}