from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestLanguage(EnumsTest):
    entity = 'language'
    title = _("Langue")
    data = [
        {"id":"1", "identifier":"FRA", "name":"Français"}
    ]
    new_data = {"identifier":"ENG", "name":"Anglais"}

    def test_list(self, francoralite_context, name="identifier"):
        super().test_list(francoralite_context, name="identifier")
        
    def test_details(self, francoralite_context, name="identifier", notes="name"):
        super().test_details(francoralite_context, name="identifier", notes="name")
    
    def test_add(self, francoralite_context, name="identifier", notes="name"):
        # TODO FIX
        # super().test_add(francoralite_context, name="identifier", notes="name")
        pass
        
    def test_update(self, francoralite_context, notes="identifier"):
        # TODO FIX
        #super().test_update(francoralite_context, notes="identifier")
        pass
        
    def test_create_err_409(self, francoralite_context, name="identifier"):
        # TODO FIX
        # super().test_create_err_409(francoralite_context, name="identifier")
        pass
