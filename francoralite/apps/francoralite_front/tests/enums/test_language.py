from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestLanguage(EnumsTest):
    entity = 'language'
    first_text_field = 'identifier'
    second_text_field = 'name'
    title_use_second_text_field = True
    title = _("Langue")
    data = [
        {"id":"4", "identifier":"FRA", "name":"Français"}
    ]
    new_data = {"identifier":"ENG", "name":"Anglais"}

    def test_add(self, francoralite_context):
        # TODO FIX
        pass

    def test_create_err_409(self, francoralite_context):
        # TODO FIX
        pass
