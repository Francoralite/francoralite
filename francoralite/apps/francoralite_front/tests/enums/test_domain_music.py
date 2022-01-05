from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestDomainMusic(EnumsTest):
    entity = 'domain_music'
    title = _('Genre de musique')
    data = [
        {"id":"1", "name":"air de musique", "notes":"Notes air de musique"}
    ]
    new_data = {"name":"air de fanfare", "notes":"Notes air de fanfare"}