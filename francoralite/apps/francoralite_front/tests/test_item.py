from django.utils.translation import gettext as _


def _test_item_list(francoralite_context):
    for username in francoralite_context.USERNAMES:
        # Open the items list page for each profile
        francoralite_context.open_homepage(auth_username=username)
        francoralite_context.open_url('/item')

        # Verify the label of the mission page
        francoralite_context.verify_title(_('Items'))

        # links to the items
        link_view_1 = francoralite_context.find_element(by_link_url='/item/1')
        assert link_view_1.text == 'UPOI_ATP_0001_0001_001'

        has_buttons = username in ('contributeur', 'administrateur')
        assert has_buttons == francoralite_context.exists_element(by_link_url='/item/edit/1')
        assert has_buttons == francoralite_context.exists_element(by_button_url='/item/delete/1')

        # And, then logout (if authenticated user)
        if username:
            francoralite_context.logout(username)
            
def _test_item_details(francoralite_context):
    for username in francoralite_context.USERNAMES:
        # Open the first item page for each profile
        francoralite_context.open_homepage(auth_username=username)
        francoralite_context.open_url('/item/1')     

        # Verify data
        data = {
            'id_title': "A propos du métier de violoneux (doc.)",
            'id_description': "M. Aubrière raconte ses premiers bals.",
            'id_code': 'UPOI_ATP_0001_0001_001',
            'id_code_partner': 'MUS1969.33.1',
            'id_recording_context': '1',
            "id_location_details": "La Biroire est un lieu-dit situé à Saint-Pierre-d'Oléron, sur l'Île d'Oléron.",
        }
        francoralite_context.verify_data(data)

        # And, then logout (if authenticated user)
        if username:
            francoralite_context.logout(username)
            
def test_item_update(francoralite_context):

    for username in francoralite_context.WRITERS:
        # Open the first item page for each profile
        francoralite_context.open_homepage(auth_username=username)
        francoralite_context.open_url('/item/edit/1')
 
        # Verify data
        data = {
            'id_title': "A propos du métier de violoneux (doc.)",
            'id_description': "M. Aubrière raconte ses premiers bals.",
            'id_code': 'UPOI_ATP_0001_0001_001',
            'id_code_partner': 'MUS1969.33.1'
        }
        francoralite_context.verify_data_form_id(data)
        data = {
            'item_collector': "Claudie Marcel-Dubois",
            'item_informer': "Charles Aubrière"            
        }
        francoralite_context.verify_data_form_related(data)

        # And, then logout (if authenticated user)
        if username:
            francoralite_context.logout(username)