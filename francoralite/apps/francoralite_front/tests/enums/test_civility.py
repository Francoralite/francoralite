from enums_test import EnumsTest


class TestCivility(EnumsTest):
    second_text_field = None
    entity = 'civility'
    title = 'Civilités'
    data = [
        {"id":"1", "name":"(Mme)"},
        {"id":"2", "name":"Mlle"},
        {"id":"3", "name":"Monsieur"},
        {"id":"4", "name":"Sr"},
    ]
    new_data = {"name":"Dr"}
