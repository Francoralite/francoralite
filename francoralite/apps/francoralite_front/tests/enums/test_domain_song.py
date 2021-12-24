from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestDomainSong(EnumsTest):
    entity = 'domain_song'
    title = _('Genre de chanson')
    data = [
        {"id":"1", "name":"relations sociales", "notes":"Notes relations sociales"}
    ]
    new_data = {"name":"travail", "notes":"Notes travail"}