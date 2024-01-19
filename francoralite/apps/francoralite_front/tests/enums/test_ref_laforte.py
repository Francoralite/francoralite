from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestRefLaforte(EnumsTest):
    entity = "ref_laforte"
    title = _("Catalogue Laforte")
    first_text_field = "number"
    second_text_field = "name"
    data = [
        {"id": "1", "number": "I.A01", "name": "Gabriel (archange)"},
        {"id": "2", "number": "I.A02", "name": "La fuite en Égypte : Le blé"},
    ]
    new_data = {"number": "I.A03", "name": "Jésus et sa mère"}
