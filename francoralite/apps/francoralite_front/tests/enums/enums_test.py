from django.utils.translation import gettext as _


class EnumsTest:
    first_text_field = 'name'
    second_text_field = 'notes'
    title_use_second_text_field = False
    update_record_id = 1

    @property
    def url_prefix(self):
        return "/" + self.entity

    @property
    def counter(self):
        return len(self.data)

    def test_list(self, francoralite_context):
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
                assert link_view.text == d[self.first_text_field].upper()
                assert has_buttons == francoralite_context.exists_element(
                    by_link_url=self.url_prefix + '/edit/' + d["id"])
                assert has_buttons == francoralite_context.exists_element(
                    by_button_url=self.url_prefix + '/delete/' + d["id"])

            # And, then logout (if authenticated user)
            if username:
                francoralite_context.logout(username)

    def test_details(self, francoralite_context):
        for username in francoralite_context.USERNAMES:
            francoralite_context.open_homepage(auth_username=username)
            # Open the entity detail page for each profile
            for d in self.data :
                francoralite_context.open_url(self.url_prefix + '/' + d["id"])

                # Verify data
                data = {
                    'id_' + self.first_text_field: d[self.first_text_field],
                    'id_' + self.second_text_field: d[self.second_text_field],
                }
                if self.title_use_second_text_field:
                    francoralite_context.verify_title(_(self.title) + ' : ' + d[self.second_text_field])
                else:
                    francoralite_context.verify_title(_(self.title) + ' : ' + d[self.first_text_field])
                francoralite_context.verify_data(data)

            # And, then logout (if authenticated user)
            if username:
                francoralite_context.logout(username)

    def test_add(self, francoralite_context):
        for username in francoralite_context.ADMINS:
            # Go to the add page
            francoralite_context.open_homepage(auth_username=username)
            francoralite_context.open_url(self.url_prefix + '/add')

            # On page add
            francoralite_context.verify_title(_(self.title) + ' - Création')

            # Write content
            content = {
                'id_' + self.first_text_field: self.new_data[self.first_text_field],
                'id_' + self.second_text_field: self.new_data[self.second_text_field],
            }
            francoralite_context.fill_data(content)

            # Validation
            francoralite_context.find_element(by_id='save').click()

            # Go to the new coupe
            francoralite_context.open_url(self.url_prefix + '/' + str(self.counter+1))

            # Verify data
            if self.title_use_second_text_field:
                francoralite_context.verify_title(_(self.title) + ' : ' + self.new_data[self.second_text_field])
            else:
                francoralite_context.verify_title(_(self.title) + ' : ' + self.new_data[self.first_text_field])
            francoralite_context.verify_data(content)

            # And, then logout (if authenticated user)
            if username:
                francoralite_context.logout(username)

    def test_update(self, francoralite_context):
        for username in francoralite_context.ADMINS:
            # Go to the home page
            francoralite_context.open_homepage(auth_username=username)

            # Go to the first edit page
            francoralite_context.open_url(self.url_prefix + '/edit/' + str(self.update_record_id))

            # Write a note
            francoralite_context.set_element_value('id_' + self.second_text_field, 'Test notes')

            # Validation
            francoralite_context.find_element(by_id='save').click()

            # The notes updated on the detail page
            francoralite_context.open_url(self.url_prefix + '/' + str(self.update_record_id))
            label = francoralite_context.find_element(by_id="id_" + self.second_text_field)
            assert label.text == 'Test notes'

            # And, then logout (if authenticated user)
            if username:
                francoralite_context.logout(username)

    def test_create_err_409(self, francoralite_context):
        for username in francoralite_context.ADMINS:
            # Go to the home page
            francoralite_context.open_homepage(auth_username=username)

            # Create a new item
            francoralite_context.open_url(self.url_prefix + '/add')

            # Write a code
            francoralite_context.set_element_value('id_' + self.first_text_field, self.data[0][self.first_text_field])

            # Validation
            francoralite_context.find_element(by_id='save').click()

            # Message for error HTTP 409
            message = francoralite_context.find_element(by_id="id_message")
            assert message.text == _('Une fiche avec ce code existe déjà.')

            # And, then logout (if authenticated user)
            if username:
                francoralite_context.logout(username)
