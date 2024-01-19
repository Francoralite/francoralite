from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestHornbostelsachs(EnumsTest):
    entity = 'hornbostelsachs'
    first_text_field = 'number'
    second_text_field = 'name'
    title = _("Classification Hornbostel-Sachs")
    data = [
        {"id":"1", "number":"321.322", "name":"Violon"}
    ]
    new_data = {"number":"4", "name":"Voix"}
