from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestRefLaforte(EnumsTest):
    entity = "ref_laforte"
    title = _("Catalogue Laforte")
    second_text_field = "description"
    data = [
        {"id": "1", "name": "I.A01", "description": "Gabriel (archange)"},
        {"id": "2", "name": "I.A02", "description": "La fuite en Égypte : Le blé"},
    ]
    new_data = {"name": "I.A03", "description": "Jésus et sa mère"}
