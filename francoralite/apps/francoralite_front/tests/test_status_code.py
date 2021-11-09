from django.test import Client


def test_authority_not_found(francoralite_selenium_context):
    client = Client()
    url_prefix = francoralite_selenium_context.URL_PREFIX

    # Back
    response = client.get(url_prefix+ '/api/authority/1234')
    assert response.status_code == 404
    assert response.json().get('detail') == 'Not found.'

    # Front
    response = client.get(url_prefix+ '/authority/1234')
    assert response.status_code == 404
    assert 'Cette personne n’existe pas.' in response.content.decode('utf8')
