from enums_test import EnumsTest


class TestBlock(EnumsTest):
    entity = 'block'
    first_text_field = 'title'
    second_text_field = 'content'
    update_record_id = 3
    title = 'Bloc'
    data = [
        {'id': '3', 'title': 'Présentation', 'type': '', 'content': 'Bonjour et bienvenue sur Francoralité !', 'order': 1, 'show': True},
        {'id': '1', 'title': 'Géo-Navigateur', 'type': 'M', 'content': '', 'order': 2, 'show': True},
        {'id': '4', 'title': 'Focus', 'type': '', 'content': '', 'order': 3, 'show': True},
        {'id': '2', 'title': 'Partenaires', 'type': 'P', 'content': '', 'order': 4, 'show': True},
    ]
    new_data = {'title': 'Nouveau bloc', 'type': '', 'content': 'Contenu du nouveau bloc', 'order': 5}

    def test_add(self, francoralite_context):
        # TODO FIX
        pass

    def test_create_err_409(self, francoralite_context):
        # TODO FIX
        pass
