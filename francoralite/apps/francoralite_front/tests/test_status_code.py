from django.test import Client


def test_authority_found(francoralite_context):
    url_prefix = francoralite_context.URL_PREFIX
    client = Client()

    # Back
    response = client.get(url_prefix + '/api/authority/1')
    assert response.status_code == 200

    # Front
    response = client.get(url_prefix + '/authority/1')
    assert response.status_code == 200


def test_authority_not_found(francoralite_context):
    url_prefix = francoralite_context.URL_PREFIX
    client = Client()

    # Back
    response = client.get(url_prefix + '/api/authority/1234')
    assert response.status_code == 404
    assert response.json().get('detail') == 'Not found.'

    # Front
    response = client.get(url_prefix + '/authority/1234')
    assert response.status_code == 404
    assert 'Cette personne n’existe pas.' in response.content.decode('utf8')
