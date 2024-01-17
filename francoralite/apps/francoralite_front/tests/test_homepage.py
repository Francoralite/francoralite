from django.utils.translation import gettext as _


def test_homepage(francoralite_context):
    francoralite_context.open_homepage()

    # Test title
    assert 'Francoralité' in francoralite_context.browser.title

    # Define the hierarchy of all menus
    all_menus = [
        [_('Accueil'), False, []],
        [_('Archives sonores'), False, [
            [_('Institutions'), None, []],
            [_('Fonds'), None, []],
            [_('Missions'), None, []],
            [_('Enquêtes'), None, []],
            [_('Items'), None, []],
        ]],
        [_('Thésaurus'), False, [
            [_('Personnes'), None, [
                [_('Enquêteurs'), None, []],
                [_('Informateurs'), None, []],
                [_('Auteurs'), None, []],
                [_('Compositeurs'), None, []],
                [_('Éditeurs'), None, []],
            ]],
            [_('Lieux'), None, [
                [_('Par enquêtes'), _('Lieux, par enquêtes'), []],
            ]],
            [_('Aires culturelles'), None, []],
            [_('Langue'), None, []],
            [_('Mot-clé'), None, []],
            [_('Thématique'), None, []],
            [_('Musique'), False, [
                [_("Genre d'autre expression vocale"), _('Genre vocal'), []],
                [_('Genre de musique instrumentale'), _('Genre de musique'), []],
                [_('Nature des émissions vocales'), None, []],
                [_('Instruments-Voix'), _('Voix/Instruments'), []],
                [_('Classification Hornbostel-Sachs'), None, []],
                [_('Fonction'), None, []],
                [_('Organisation musicale'), None, []],
                [_('Formation (musicale)'), _('Formation'), []],
            ]],
            [_('Chanson'), False, [
                [_('Genre de chanson'), None, []],
                [_('Coupe'), None, []],
                [_('Catalogages Laforte'), None, []],
            ]],
            [_('Conte'), False, [
                [_('Genre de conte'), None, []],
            ]],
            [_('Danses'), _('Genre de danse'), []],
            [_('Contexte d’enregistrement'), None, []],
            [_('Type de média'), None, []],
            [_('Édition'), False, [
                [_('Droits légaux'), None, []],
                [_('Éditeur'), None, []],
                [_('Meta donnée auteur'), None, []],
            ]],
        ]],
        [_('Recherche avancée'), None, []],
    ]

    # Test top level menu labels
    top_level_menu_labels = [menu[0] for menu in all_menus]
    top_level_menus = francoralite_context.find_elements(
        by_css_selector='#menu nav > ul > li')
    assert [element.text for element in top_level_menus] == top_level_menu_labels

    # Click on each menu item
    browse_menu(francoralite_context, all_menus)


def test_homepage_partners(francoralite_context):
    francoralite_context.open_homepage()

    # Test title
    assert 'Francoralité' in francoralite_context.browser.title

    url_partners = (
        "https://www.collexpersee.eu/",
    )

    for partner in url_partners:
        assert francoralite_context.scroll_to_element(by_link_url=partner)


def browse_menu(francoralite_context, children, pointer_path=[]):
    for link, target, subchildren in children:
        if target is not False and link is not _('Aires culturelles'):
            # Move pointer to the top-left logo
            francoralite_context.move_to_element(by_css_selector='img')
            # Move pointer to open the sub-menu
            for label in pointer_path:
                francoralite_context.move_to_element(by_link_text=label)
            # Goto to the linked page
            francoralite_context.scroll_to_element(by_link_text=link).click()
            # Test the right label
            francoralite_context.verify_title(target or link)
        if subchildren:
            # Build new pointer path: add current item and its first child
            new_pointer_path = pointer_path + [link, subchildren[0][0]]
            # Verify sub-menus
            browse_menu(francoralite_context, subchildren, new_pointer_path)
