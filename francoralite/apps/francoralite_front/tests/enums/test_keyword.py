from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestKeyword(EnumsTest):
    entity = 'keyword'
    title = _('Mot-clé')
    data = [
        {'id': '1', 'name': 'violon', 'notes': 'Notes violon'},
        {'id': '2', 'name': 'biographie', 'notes': ''},
    ]
    new_data = {'name': 'à vérifier', 'notes': 'Notes à vérifier'}
