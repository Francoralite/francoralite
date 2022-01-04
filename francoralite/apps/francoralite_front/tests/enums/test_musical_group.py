from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestMusicalGroup(EnumsTest):
    entity = 'musical_group'
    title = _("Formation")
    data = [
        {"id":"1", "name":"duo", "notes":"Notes duo"}
    ]
    new_data = {"name":"solo", "notes":"Notes solo"}