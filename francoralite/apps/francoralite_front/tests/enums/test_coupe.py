from enums_test import EnumsTest


class TestCoupe(EnumsTest):
    entity = 'coupe'
    data = [
        {"id":"1", "name":"AABB", "notes":"Notes de AABB"},
    ]
    new_data = {"name":"AAB", "notes":"Notes de AAB"}
