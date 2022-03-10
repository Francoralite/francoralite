from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestHornbostelsachs(EnumsTest):
    entity = 'hornbostelsachs'
    title = _("Classification Hornbostel-Sachs")
    data = [
        {"id":"1", "number":"321.322", "name":"Violon"}
    ]
    new_data = {"number":"4", "name":"Voix"}
    
    def test_list(self, francoralite_context, name="number"):
        super().test_list(francoralite_context, name="number")
        
    def test_details(self, francoralite_context, name="number", notes="name"):
        super().test_details(francoralite_context, name="number", notes="name")
        
    def test_add(self, francoralite_context, name="number", notes="name"):
        super().test_add(francoralite_context, name="number", notes="name")
        
    def test_update(self, francoralite_context, notes="name"):
        super().test_update(francoralite_context, notes="name")
        
    def test_create_err_409(self, francoralite_context, name="number"):
        super().test_create_err_409(francoralite_context, name="number")