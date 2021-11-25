from django.test import Client
from django.utils.translation import gettext as _


def test_authority_found(francoralite_context):
    url_prefix = francoralite_context.URL_PREFIX
    client = Client()

    # Back (lecture)
    response = client.get(url_prefix + '/api/authority/1')
    assert response.status_code == 200

    # Front (lecture)
    response = client.get(url_prefix + '/authority/1')
    assert response.status_code == 200


def test_authority_not_found(francoralite_context):
    url_prefix = francoralite_context.URL_PREFIX
    client = Client()

    # Back (lecture)
    response = client.get(url_prefix + '/api/authority/1234')
    assert response.status_code == 404
    assert response.json().get('detail') == 'Not found.'

    # Front (lecture)
    response = client.get(url_prefix + '/authority/1234')
    assert response.status_code == 404
    assert _('Cette personne n’existe pas.') in response.content.decode('utf8')

    
def test_authority_not_authorized(francoralite_context):
    url_prefix = francoralite_context.URL_PREFIX
    client = Client()

    # Back (écriture)
    response = client.patch(url_prefix + '/api/authority/1')
    assert response.status_code == 403
    assert response.json().get('detail') == 'You do not have permission to perform this action.'

    # Front (lecture)
    response = client.get(url_prefix + '/authority/edit/1')
    assert response.status_code == 403
    assert _('Accès interdit.') in response.content.decode('utf8')
    
    # Front (écriture)
    response = client.post(url_prefix + '/authority/edit/1')
    assert response.status_code == 403
    assert _('Accès interdit.') in response.content.decode('utf8')
