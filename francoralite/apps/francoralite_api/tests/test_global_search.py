import pytest

from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase


@pytest.mark.django_db
class TestGlobalSearch(APITestCase):
    """
    This class tests global search
    """

    fixtures = ["francoralite.json"]

    def _test_global_search_implementation(self, query, records):
        response = self.client.get("/globalsearch/?q=" + query)
        self.assertEqual(response.status_code, HTTP_200_OK)

        # check results from reference set
        entities = set(record['entity'] for record in response.data)
        results = {
            entity: set(
                record['id']
                for record in response.data
                if record['entity'] == entity
            ) for entity in entities
        }
        self.assertEqual(results, records)

        # check no duplicated results
        records_count = sum(len(ids) for ids in records.values())
        self.assertEqual(len(response.data), records_count)

    def test_empty_query(self):
        self._test_global_search_implementation('', {
            'Authority': {1, 4, 5, 6, 9},
            'Location': {1, 2, 3, 4},
            'Fond': {1, 2},
            'Mission': {1, 2, 3},
            'Collection': {1, 2, 3, 4},
            'Item': {1, 2, 3, 4},
        })

    def test_simple_query(self):
        self._test_global_search_implementation('violon', {
            'Collection': {3},
            'Item': {1, 2, 3},
        })

    def test_unknown_query(self):
        self._test_global_search_implementation('unknown-value', {})
