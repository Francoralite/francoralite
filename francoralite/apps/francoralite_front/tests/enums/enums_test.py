from django.utils.translation import gettext as _


class EnumsTest:
    
    @property
    def url_prefix(self):
        return "/" + self.entity
    
    @property
    def counter(self):
        return len(self.data)

    def test_list(self, francoralite_context, name="name"):
        for username in francoralite_context.USERNAMES:
            
            # Open the list page for each profile
            francoralite_context.open_homepage(auth_username=username)
            francoralite_context.open_url(self.url_prefix)

            # Verify the label of the page
            francoralite_context.verify_title(_(self.title))
            
            has_buttons = username in francoralite_context.ADMINS
            assert has_buttons == francoralite_context.exists_element(
                    by_link_url=self.url_prefix + '/add' )

            # links to the entity detail
            for d in self.data :
                link_view = francoralite_context.find_element(by_link_url=self.url_prefix + '/' + d["id"])
                assert link_view.text == d[name].upper()
                assert has_buttons == francoralite_context.exists_element(
                    by_link_url=self.url_prefix + '/edit/' + d["id"])
                assert has_buttons == francoralite_context.exists_element(
                    by_button_url=self.url_prefix + '/delete/' + d["id"])

            # And, then logout (if authenticated user)
            if username:
                francoralite_context.logout(username)
                
    def test_details(self, francoralite_context, name="name", notes="notes"):
        for username in francoralite_context.USERNAMES:
            francoralite_context.open_homepage(auth_username=username)
            # Open the entity detail page for each profile
            for d in self.data :
                francoralite_context.open_url(self.url_prefix + '/' + d["id"])

                # Verify data
                data = {
                    'id_' + name : d[name],
                    'id_' + notes : d[notes],
                }
                if self.entity == "language":
                    francoralite_context.verify_title(_(self.title) + ' : ' + d[notes])
                else:
                    francoralite_context.verify_title(_(self.title) + ' : ' + d[name])
                francoralite_context.verify_data(data)

            # And, then logout (if authenticated user)
            if username:
                francoralite_context.logout(username)
                
    def test_add(self, francoralite_context, name="name", notes="notes"):
        for username in francoralite_context.ADMINS:
            # Go to the add page
            francoralite_context.open_homepage(auth_username=username)
            francoralite_context.open_url(self.url_prefix + '/add')

            # On page add
            francoralite_context.verify_title(_(self.title) + ' - Création')

            # Write content
            content = {
                'id_' + name: self.new_data[name],
                'id_' + notes: self.new_data[notes],
            }
            francoralite_context.fill_data(content)

            # Validation
            francoralite_context.find_element(by_id='save').click()

            # Go to the new coupe
            francoralite_context.open_url(self.url_prefix + '/' + str(self.counter+1))

            # Verify data
            francoralite_context.verify_title(_(self.title) + ' : ' + self.new_data[name])
            francoralite_context.verify_data(content)
            
            # And, then logout (if authenticated user)
            if username:
                francoralite_context.logout(username)
                
    def test_update(self, francoralite_context, notes="notes"):
        for username in francoralite_context.ADMINS:
            # Go to the home page
            francoralite_context.open_homepage(auth_username=username)

            # Go to the first edit page
            francoralite_context.open_url(self.url_prefix + '/edit/1')

            # Write a note
            francoralite_context.set_element_value('id_' + notes, 'Test notes')

            # Validation
            francoralite_context.find_element(by_id='save').click()

            # The notes updated on the detail page
            francoralite_context.open_url(self.url_prefix + '/1')
            label = francoralite_context.find_element(by_id="id_" + notes )
            assert label.text == 'Test notes'

            # And, then logout (if authenticated user)
            if username:
                francoralite_context.logout(username)
                
    def test_create_err_409(self, francoralite_context, name="name"):
        for username in francoralite_context.ADMINS:
            # Go to the home page
            francoralite_context.open_homepage(auth_username=username)

            # Create a new item
            francoralite_context.open_url(self.url_prefix + '/add')

            # Write a code
            francoralite_context.set_element_value('id_' + name, self.data[0][name])

            # Validation
            francoralite_context.find_element(by_id='save').click()

            # Message for error HTTP 409
            message = francoralite_context.find_element(by_id="id_message")
            assert message.text == _('Une fiche avec ce code existe déjà.')

            # And, then logout (if authenticated user)
            if username:
                francoralite_context.logout(username)