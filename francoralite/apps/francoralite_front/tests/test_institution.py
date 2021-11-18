from django.utils.translation import gettext as _


def test_institution_add(francoralite_context):
    # Go to the home page
    francoralite_context.open_homepage(auth_username='administrateur')

    # Click on the institution menu
    francoralite_context.find_element(by_link_text=_('Institutions')).click()

    # Verify the label "Institutions"
    francoralite_context.verify_title(_('Institutions'))

    # Click on the "add" link
    francoralite_context.find_element(by_link_class='btn_add').click()

    # Verify the label "Institutions - Création"
    francoralite_context.verify_title(_('Institutions - Création'))

    # Write content
    francoralite_context.find_element(by_id='id_name').send_keys('Institution Test')
    francoralite_context.find_element(by_div_class='ProseMirror').send_keys('Ceci est une institution de **test**.')

    # Validation
    francoralite_context.find_element(by_id='save').click()

    # Goto to list of institution
    # Verify the label "Institutions"
    francoralite_context.verify_title(_('Institutions'))

    # Click on the new institution created
    francoralite_context.find_element(by_link_text='Institution Test').click()

    # Check values
    # Verify the label "Institution : Institution Test"
    francoralite_context.verify_title('Institution : Institution Test')
