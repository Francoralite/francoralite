from enums_test import EnumsTest


class TestCoupe(EnumsTest):
    entity = 'coupe'
    title = 'Coupe'
    data = [
        {"id":"1", "name":"AABB", "notes":"Notes de AABB"},
        {"id":"2", "name":"ABCD", "notes":"Notes de ABCD"},
    ]
    new_data = {"name":"AAB", "notes":"Notes de AAB"}
