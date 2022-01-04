from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestMusicalGroup(EnumsTest):
    entity = 'musical_organization'
    title = _("Organisation musicale")
    data = [
        {"id":"1", "name":"monodie", "notes":"Notes monodie"}
    ]
    new_data = {"name":"polyphonie", "notes":"Notes polyphonie"}
