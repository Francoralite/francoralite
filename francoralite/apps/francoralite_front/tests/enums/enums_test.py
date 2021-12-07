from django.utils.translation import gettext as _

class enums_test:
    def __init__(self, entity, data, new_data):
        self.entity = entity
        self.url_prefix = "/" + entity
        self.data = data
        self.new_data = new_data
        self.counter = len(data)

    def list_test(self, context):
        for username in context.USERNAMES:
            
            # Open the list page for each profile
            context.open_homepage(auth_username=username)
            context.open_url(self.url_prefix)

            # Verify the label of the page
            context.verify_title(_(self.entity.capitalize()))
            
            has_buttons = username in context.ADMINS
            assert has_buttons == context.exists_element(
                    by_link_url=self.url_prefix + '/add' )

            # links to the entity detail
            for d in self.data :
                link_view = context.find_element(by_link_url=self.url_prefix + '/' + d["id"])
                assert link_view.text == d["name"]
                assert has_buttons == context.exists_element(
                    by_link_url=self.url_prefix + '/edit/' + d["id"])
                assert has_buttons == context.exists_element(
                    by_button_url=self.url_prefix + '/delete/' + d["id"])

            # And, then logout (if authenticated user)
            if username:
                context.logout(username)
                
    def details_test(self,context):
        for username in context.USERNAMES:
            context.open_homepage(auth_username=username)
            # Open the entity detail page for each profile
            for d in self.data :
                context.open_url(self.url_prefix + '/' + d["id"])

                # Verify data
                data = {
                    'id_name' : d["name"],
                    'id_notes' : d["notes"],
                }
                context.verify_title(_(self.entity.capitalize()) + ' :')
                context.verify_data(data)

            # And, then logout (if authenticated user)
            if username:
                context.logout(username)
                
    def add_test(self,context):
        for username in context.ADMINS:
            # Go to the add page
            context.open_homepage(auth_username=username)
            context.open_url(self.url_prefix + '/add')

            # On page add
            context.verify_title(_(self.entity.capitalize()) + ' - Création')

            # Write content
            content = {
                'id_name': self.new_data["name"],
                'id_notes': self.new_data["notes"],
            }
            context.fill_data(content)

            # Validation
            context.find_element(by_id='save').click()

            # Go to the new coupe
            context.open_url(self.url_prefix + '/' + str(self.counter+1))

            # Verify data
            context.verify_title(_(self.entity.capitalize()) + ' :')
            context.verify_data(content)
            
            # And, then logout (if authenticated user)
            if username:
                context.logout(username)
                
    def update_test(self, context):
        for username in context.ADMINS:
            # Go to the home page
            context.open_homepage(auth_username=username)

            # Go to the first edit page
            context.open_url(self.url_prefix + '/edit/1')

            # Write a note
            context.set_element_value('id_notes', 'Test notes')

            # Validation
            context.find_element(by_id='save').click()

            # The notes updated on the detail page
            context.open_url(self.url_prefix + '/1')
            label = context.find_element(by_id="id_notes")
            assert label.text == 'Test notes'

            # And, then logout (if authenticated user)
            if username:
                context.logout(username)
                
    def err_409_test(self, context):
        for username in context.ADMINS:
            # Go to the home page
            context.open_homepage(auth_username=username)

            # Create a new item
            context.open_url(self.url_prefix + '/add')

            # Write a code
            context.set_element_value('id_name', self.data[0]["name"])

            # Validation
            context.find_element(by_id='save').click()

            # Message for error HTTP 409
            message = context.find_element(by_id="id_message")
            assert message.text == _("Une erreur indéterminée est survenue.")
            # TODO: à terme 400->409  : assert message.text == _('Une fiche avec ce code existe déjà.')
            

            # And, then logout (if authenticated user)
            if username:
                context.logout(username)