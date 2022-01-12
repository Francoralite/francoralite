from django.utils.translation import gettext as _
from enums_test import EnumsTest


class TestInstrument(EnumsTest):
    entity = 'instrument'
    title = _("Voix/Instruments")
    data = [
        {"id": "1", "name": "Violon", "notes": ""},
        {"id": "2", "name": "Voix d'homme", "notes": ""}
    ]
    new_data = {"name": "guitare", "notes": "Notes guitare"}
