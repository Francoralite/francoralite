from django.test import Client


def test_authority_not_found(francoralite_selenium_context):
    client = Client()
    url_prefix = francoralite_selenium_context.URL_PREFIX

    # Back
    response = client.get(url_prefix+ '/api/authority/1234')
    assert response.status_code == 404

    # Front
    response = client.get(url_prefix+ '/authority/1234')
    assert response.status_code == 404
    assert b"Cette personne n&#x27;existe pas." in response.content
