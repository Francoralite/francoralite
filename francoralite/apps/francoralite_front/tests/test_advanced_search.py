import time
from django.utils.translation import gettext as _


def test_search_dance(francoralite_context):
    francoralite_context.open_homepage(auth_username="")
    
    url_prefix = "/search_advanced/"
    
    # Go to advanced search page
    francoralite_context.open_url(url_prefix)
    
    # Verify the label of the page
    francoralite_context.verify_title(_('Recherche avancée'))
    
    # Write first characters of the content
    francoralite_context.scroll_to_element(
        by_xpath="//input[@placeholder='" + _("Recherche sur danse") + " ...']").send_keys('va')
    
    # There is an option named "valse"
    francoralite_context.find_element(
        by_xpath="//p[contains(text(), 'valse')]", visibility_timeout=5)
      