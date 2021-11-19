from django.utils.translation import gettext as _


def test_location_list(francoralite_context):
    for username in francoralite_context.USERNAMES:
        # Open the locations list page for each profile
        francoralite_context.open_homepage(auth_username=username)
        francoralite_context.open_url('/location_gis/')
        
         # Verify the label of the location page
        francoralite_context.verify_title(_('Lieux'))
        
        # Verify buttons
        has_buttons = username in francoralite_context.WRITERS
        assert has_buttons == francoralite_context.exists_element(by_link_url='/location_gis/add')
        
        # And, then logout (if authenticated user)
        if username:
            francoralite_context.logout(username)
            
def test_location_details(francoralite_context):
    for username in francoralite_context.USERNAMES:
        # Open the first collection page for each profile
        francoralite_context.open_homepage(auth_username=username)
        francoralite_context.open_url('/location_gis/1')
        
        # Verify data
        data = {
            'id_code': "poitiers",
            'id_latitude': '46.5802596',
            'id_longitude': '0.340196',
        }
        francoralite_context.verify_data(data)
        
        # Verify buttons
        has_buttons = username in francoralite_context.WRITERS
        assert has_buttons == francoralite_context.exists_element(by_link_url='/location_gis/edit/1')
        assert has_buttons == francoralite_context.exists_element(by_button_url='/location_gis/delete/1')

        # And, then logout (if authenticated user)
        if username:
            francoralite_context.logout(username)

def test_location_add(francoralite_context):
    last_id = 3
    for username in francoralite_context.WRITERS:
        last_id = last_id + 1
        # Open the first location page for each profile
        francoralite_context.open_homepage(auth_username=username)
        francoralite_context.open_url('/location_gis/')
        
        # Click on the "add" link
        francoralite_context.find_element(by_link_url='/location_gis/add').click()
        
        # Write content
        content = {
            'id_code': 'cherves',
            'id_name': "Cherves, Poitiers, Vienne, Nouvelle-Aquitaine, France métropolitaine, 86170, France",
            'id_latitude': '46.7175881',
            'id_longitude': '0.0189083',
        }
        francoralite_context.fill_data(content)
        
        # Validation
        francoralite_context.find_element(by_id='save').click()

        # Go to the new mission
        francoralite_context.open_url('/location_gis/' + str(last_id))

        # Verify content
        del content["id_name"]
        francoralite_context.verify_data(content)
 
        
        # And, then logout (if authenticated user)
        if username:
            francoralite_context.logout(username)
