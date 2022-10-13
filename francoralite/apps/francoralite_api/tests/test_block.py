"""
Block tests
"""

import factory
import pytest

from django.urls import reverse
from parameterized import parameterized
from rest_framework import status
from rest_framework.test import APITestCase

from .factories.block import BlockFactory
from ..models.block import Block

from .keycloak import get_token

# Expected structure for Block objects
BLOCK_STRUCTURE = [
    ('id', int),
    ('type', (str, type(None))),
    ('title', str),
    ('content', str),
    ('order', int),
    ('show', bool),
]

# Expected keys for Block objects
BLOCK_FIELD = sorted([item[0] for item in BLOCK_STRUCTURE])


@pytest.mark.django_db
class TestBlockList(APITestCase):
    """
    This class manage all Block tests
    """

    def setUp(self):
        """
        Run needed commands to have a fully working project
        """
        get_token(self, username="administrateur")

        Block.objects.all().delete()  # remove block created by migration 0009
        BlockFactory.create_batch(6)

    def test_can_get_block_list(self):
        """
        Ensure Block objects exists
        """
        url = reverse('block-list')

        # ORM side
        blocks = Block.objects.all()
        self.assertEqual(len(blocks), 6)

        # API side
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    @parameterized.expand(BLOCK_STRUCTURE)
    def test_has_valid_block_values(self, attribute, attribute_type):
        """
        Ensure Block objects have valid values
        """

        url = reverse('block-list')
        response = self.client.get(url)

        self.assertIsInstance(response.data, list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for block in response.data:
            # Check only expected attributes returned
            self.assertEqual(
                sorted(block.keys()), BLOCK_FIELD)

            # Ensure type of each attribute
            self.assertIsInstance(block[attribute], attribute_type)
            self.assertIsNot(block[attribute], '')

    def test_get_a_block(self):
        """
        Ensure we can get a Block objects using an existing id
        """

        item = Block.objects.first()
        url = reverse('block-detail', kwargs={'pk': item.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

    def test_create_a_block(self):
        """
        Ensure we can create a Block object
        """

        data = factory.build(dict, FACTORY_CLASS=BlockFactory)
        url = reverse('block-list')
        response = self.client.post(url, data, format='json')

        # Check only expected attributes returned
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), BLOCK_FIELD)

        url = reverse(
            'block-detail',
            kwargs={'pk': response.data['id']}
        )
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response_get.data, dict)

    def test_update_a_block(self):
        """
        Ensure we can update a Block object
        """

        item = Block.objects.first()
        self.assertNotEqual(item.title, 'foobar_test_put')

        # Get existing object from API
        url_get = reverse('block-detail', kwargs={'pk': item.id})
        data = self.client.get(url_get).data

        data['title'] = 'foobar_test_put'
        url = reverse('block-detail', kwargs={'pk': item.id})
        response = self.client.put(url, data, format='json')

        # Ensure new value returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), BLOCK_FIELD)
        self.assertEqual(response.data['title'], 'foobar_test_put')

    def test_patch_a_block(self):
        """
        Ensure we can patch a Block object
        """

        item = Block.objects.first()
        self.assertNotEqual(item.title, 'foobar_test_patch')

        data = {'title': 'foobar_test_patch'}
        url = reverse('block-detail', kwargs={'pk': item.id})
        response = self.client.patch(url, data, format='json')

        # Ensure new value returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertEqual(sorted(response.data.keys()), BLOCK_FIELD)
        self.assertEqual(response.data['title'], 'foobar_test_patch')

    def test_delete_a_block(self):
        """
        Ensure we can delete a Block object
        """

        item = Block.objects.first()

        # Delete this object
        url = reverse('block-detail', kwargs={'pk': item.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Ensure Block removed
        url_get = reverse('block-detail', kwargs={'pk': item.id})
        response_get = self.client.get(url_get)
        self.assertEqual(response_get.status_code, status.HTTP_404_NOT_FOUND)
