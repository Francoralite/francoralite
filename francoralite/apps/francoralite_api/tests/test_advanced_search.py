import pytest

from rest_framework.test import APITestCase
from rest_framework import status


@pytest.mark.django_db
class TestAdvancedSearch(APITestCase):
    """
    This class tests advanced search
    """

    fixtures = ['francoralite.json']

    def test_location(self):
        url = "/advancedsearch/?location=3"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 2)
        self.assertEqual(len(response.data['results']['items']), 2)
        self.assertEqual(len(response.data['results']['locations']), 2)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 2)  # collection 2
        self.assertEqual(response.data['results']['collections'][1]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][1]['id'], 3)  # collection 3
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 1)  # item 1
        self.assertEqual(response.data['results']['items'][1]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][1]['id'], 2)  # item 2

    def test_dance(self):
        url = "/advancedsearch/?dance=1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 2)
        self.assertEqual(len(response.data['results']['locations']), 1)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 2)  # collection 2
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 1)  # item 1
        self.assertEqual(response.data['results']['items'][1]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][1]['id'], 2)  # item 2

        url = "/advancedsearch/?dance=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 1)
        self.assertEqual(len(response.data['results']['locations']), 1)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 2)  # collection 2
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 2)  # item 2

        url = "/advancedsearch/?dance=3"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 0)
        self.assertEqual(len(response.data['results']['items']), 0)
        self.assertEqual(len(response.data['results']['locations']), 0)

    def test_collector(self):
        url = "/advancedsearch/?collector=3"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 0)
        self.assertEqual(len(response.data['results']['locations']), 1)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 1)  # collection 1

        url = "/advancedsearch/?collector=6"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 2)
        self.assertEqual(len(response.data['results']['items']), 0)
        self.assertEqual(len(response.data['results']['locations']), 2)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 2)  # collection 2
        self.assertEqual(response.data['results']['collections'][1]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][1]['id'], 3)  # collection 3

        url = "/advancedsearch/?collector=8"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 3)
        self.assertEqual(len(response.data['results']['locations']), 1)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 4)  # collection 4
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 4)  # item 4
        self.assertEqual(response.data['results']['items'][1]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][1]['id'], 1)  # item 1
        self.assertEqual(response.data['results']['items'][2]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][2]['id'], 2)  # item 2

    def test_informer(self):
        url = "/advancedsearch/?informer=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 0)
        self.assertEqual(len(response.data['results']['locations']), 1)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 1)  # collection 1

        url = "/advancedsearch/?informer=4"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 2)
        self.assertEqual(len(response.data['results']['items']), 2)
        self.assertEqual(len(response.data['results']['locations']), 2)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 2)  # collection 2
        self.assertEqual(response.data['results']['collections'][1]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][1]['id'], 3)  # collection 3
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 1)  # item 1
        self.assertEqual(response.data['results']['items'][1]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][1]['id'], 2)  # item 2

    def test_coupe(self):
        url = "/advancedsearch/?coupe=1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 2)
        self.assertEqual(len(response.data['results']['locations']), 1)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 2)  # collection 2
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 1)  # item 1
        self.assertEqual(response.data['results']['items'][1]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][1]['id'], 2)  # item 2

        url = "/advancedsearch/?coupe=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 1)
        self.assertEqual(len(response.data['results']['locations']), 1)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 1)  # collection 1
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]["id"],3)  # item 3

    def test_refrain(self):
        url = "/advancedsearch/?refrain=rose%20au%20bois"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 0)
        self.assertEqual(len(response.data['results']['items']), 1)
        self.assertEqual(len(response.data['results']['locations']), 0)
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 4)  # item 4

    def test_incipit(self):
        url = "/advancedsearch/?incipit=école%20du%20roi"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 0)
        self.assertEqual(len(response.data['results']['items']), 1)
        self.assertEqual(len(response.data['results']['locations']), 0)
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 4)  # item 4

        url = "/advancedsearch/?incipit=ordinateur"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 0)
        self.assertEqual(len(response.data['results']['items']), 0)
        self.assertEqual(len(response.data['results']['locations']), 0)

    def test_timbre(self):
        url = "/advancedsearch/?timbre=timbre_1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 0)
        self.assertEqual(len(response.data['results']['items']), 2)
        self.assertEqual(len(response.data['results']['locations']), 0)
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 1)  # item 1
        self.assertEqual(response.data['results']['items'][1]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][1]['id'], 2)  # item 2

        url = "/advancedsearch/?timbre=timbre_2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 0)
        self.assertEqual(len(response.data['results']['items']), 1)
        self.assertEqual(len(response.data['results']['locations']), 0)
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 4)  # item 4

    def test_timbre_ref(self):
        url = "/advancedsearch/?timbre_ref=timbre_ref_1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 0)
        self.assertEqual(len(response.data['results']['items']), 2)
        self.assertEqual(len(response.data['results']['locations']), 0)
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 1)  # item 1
        self.assertEqual(response.data['results']['items'][1]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][1]['id'], 2)  # item 2

        url = "/advancedsearch/?timbre_ref=timbre_ref_2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 0)
        self.assertEqual(len(response.data['results']['items']), 1)
        self.assertEqual(len(response.data['results']['locations']), 0)
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 4)  # item 4

    def test_usefulness(self):
        url = "/advancedsearch/?usefulness=1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 2)
        self.assertEqual(len(response.data['results']['items']), 2)
        self.assertEqual(len(response.data['results']['locations']), 2)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 4)  # collection 4
        self.assertEqual(response.data['results']['collections'][1]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][1]['id'], 2)  # collection 2
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 4)  # item 4
        self.assertEqual(response.data['results']['items'][1]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][1]['id'], 1)  # item 1

    def test_thematic(self):
        url = "/advancedsearch/?thematic=1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 2)
        self.assertEqual(len(response.data['results']['items']), 2)
        self.assertEqual(len(response.data['results']['locations']), 2)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 4)  # collection 4
        self.assertEqual(response.data['results']['collections'][1]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][1]['id'], 2)  # collection 2
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 4)  # item 4
        self.assertEqual(response.data['results']['items'][1]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][1]['id'], 2)  # item 2

    def test_domain_music(self):
        url = "/advancedsearch/?domain_music=1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 0)
        self.assertEqual(len(response.data['results']['items']), 0)
        self.assertEqual(len(response.data['results']['locations']), 0)

        url = "/advancedsearch/?domain_music=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 1)
        self.assertEqual(len(response.data['results']['locations']), 1)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 4)  # collection 4
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 4)  # item 4

    def test_domain_song(self):
        url = "/advancedsearch/?domain_song=1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 0)
        self.assertEqual(len(response.data['results']['items']), 0)
        self.assertEqual(len(response.data['results']['locations']), 0)

        url = "/advancedsearch/?domain_song=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 1)
        self.assertEqual(len(response.data['results']['locations']), 1)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 4)  # collection 4
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 4)  # item 4

    def test_domain_tale(self):
        url = "/advancedsearch/?domain_tale=1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 0)
        self.assertEqual(len(response.data['results']['items']), 0)
        self.assertEqual(len(response.data['results']['locations']), 0)

        url = "/advancedsearch/?domain_tale=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 2)
        self.assertEqual(len(response.data['results']['items']), 3)
        self.assertEqual(len(response.data['results']['locations']), 2)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 1)  # collection 1
        self.assertEqual(response.data['results']['collections'][1]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][1]['id'], 2)  # collection 2
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 3)  # item 3
        self.assertEqual(response.data['results']['items'][1]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][1]['id'], 1)  # item 1
        self.assertEqual(response.data['results']['items'][2]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][2]['id'], 2)  # item 2

    def test_domain_vocal(self):
        url = "/advancedsearch/?domain_vocal=1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 0)
        self.assertEqual(len(response.data['results']['items']), 0)
        self.assertEqual(len(response.data['results']['locations']), 0)

    def test_date(self):
        url = "/advancedsearch/?date_start=1969-09-05&date_end=1969-09-07"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 0)
        self.assertEqual(len(response.data['results']['locations']), 1)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 3)  # collection 3

        url = "/advancedsearch/?date_start=1969-09-01&date_end=1969-09-07"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 2)
        self.assertEqual(len(response.data['results']['items']), 2)
        self.assertEqual(len(response.data['results']['locations']), 2)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 2)  # collection 2
        self.assertEqual(response.data['results']['collections'][1]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][1]['id'], 3)  # collection 3
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 1)  # item 1
        self.assertEqual(response.data['results']['items'][1]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][1]['id'], 2)  # item 2

        url = "/advancedsearch/?date_start=1969-09-05"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 0)
        self.assertEqual(len(response.data['results']['locations']), 1)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 3)  # collection 3

        url = "/advancedsearch/?date_end=1969-09-05"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 3)
        self.assertEqual(len(response.data['results']['items']), 4)
        self.assertEqual(len(response.data['results']['locations']), 3)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 1)  # collection 1
        
    def test_media_type(self):
        url = "/advancedsearch/?media_type=1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 0)
        self.assertEqual(len(response.data['results']['items']), 0)
        self.assertEqual(len(response.data['results']['locations']), 0)
        
        
        url = "/advancedsearch/?media_type=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 3)
        self.assertEqual(len(response.data['results']['items']), 3)
        self.assertEqual(len(response.data['results']['locations']), 3)
        
        url = "/advancedsearch/?media_type=3"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 1)
        self.assertEqual(len(response.data['results']['locations']), 1)
        
    def test_recording_context(self):
        url = "/advancedsearch/?recording_context=1"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 2)
        self.assertEqual(len(response.data['results']['items']), 2)
        self.assertEqual(len(response.data['results']['locations']), 2)
        
        url = "/advancedsearch/?recording_context=3"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 1)
        self.assertEqual(len(response.data['results']['locations']), 1)
        
        url = "/advancedsearch/?recording_context=6"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 1)
        self.assertEqual(len(response.data['results']['locations']), 1)
        

    def test_multi_criteria(self):
        """
        - instrument : 2 - voix d'homme
        """
        url = "/advancedsearch/?instrument=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 2)
        self.assertEqual(len(response.data['results']['items']), 1)
        self.assertEqual(len(response.data['results']['locations']), 2)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 2)  # collection 2
        self.assertEqual(response.data['results']['collections'][1]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][1]['id'], 3)  # collection 3
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 2)  # item 2

        """
        - instrument : 2 - voix d'homme
        - instrument : 1 - violon
        """
        url = "/advancedsearch/?instrument=2&instrument=1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 0)
        self.assertEqual(len(response.data['results']['locations']), 1)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 3)  # collection 3

        """
        - dance : 2 - valse
        - instrument : 2 - voix d'homme
        """
        url = "/advancedsearch/?dance=2&instrument=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 1)
        self.assertEqual(len(response.data['results']['locations']), 1)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 2)  # Collection 2
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 2)  # item 2

        """
        - dance : 1 - polka
        - instrument : 2 - voix d'homme
        """
        url = "/advancedsearch/?dance=1&instrument=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 1)
        self.assertEqual(len(response.data['results']['locations']), 1)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 2)  # Collection 2
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 2)  # item 2

        """
        - dance : 2 - valse
        - instrument : 1 - violon
        """
        url = "/advancedsearch/?dance=2&instrument=1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 0)
        self.assertEqual(len(response.data['results']['items']), 0)
        self.assertEqual(len(response.data['results']['locations']), 0)

        """
        - collector : 6 - Jeanne-Marie Bourreau
        - instrument : 1 - violon
        """
        url = "/advancedsearch/?collector=6&instrument=1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 0)
        self.assertEqual(len(response.data['results']['locations']), 1)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 3)  # Collection 3

        """
        - informer : 4 - Charles Aubrière
        - informer : 5 - Mme Aubrière
        """
        url = "/advancedsearch/?informer=4&informer=5"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 2)
        self.assertEqual(len(response.data['results']['items']), 0)
        self.assertEqual(len(response.data['results']['locations']), 2)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 2)  # Collection 2
        self.assertEqual(response.data['results']['collections'][1]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][1]['id'], 3)  # Collection 3

        """
        - informer : 4 - Charles Aubrière
        - informer : 2 - Cecilia Mc Graw
        """
        url = "/advancedsearch/?informer=4&informer=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 0)
        self.assertEqual(len(response.data['results']['items']), 0)
        self.assertEqual(len(response.data['results']['locations']), 0)

        """
        - coupe : 1 - AABB
        - instrument : 2 - voix d'homme
        """
        url = "/advancedsearch/?coupe=1&instrument=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 1)
        self.assertEqual(len(response.data['results']['locations']), 1)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 2)  # Collection 2
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 2)  # item 2

        """
        - fonction : 1 - ecouter
        - fonction : 2 - danser
        """
        url = "/advancedsearch/?usefulness=1&usefulness=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 1)
        self.assertEqual(len(response.data['results']['locations']), 1)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 2)  # collection 2
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 1)  # item 1

        """
        - thématique : 1 - danse
        - thématique : 2 - récit
        """
        url = "/advancedsearch/?thematic=1&thematic=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 1)
        self.assertEqual(len(response.data['results']['locations']), 1)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 2)  # collection 2
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 2)  # item 2

        """
        - domain song : 2
        - domain song : 3
        """
        url = "/advancedsearch/?domain_song=2&domain_song=3"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 1)
        self.assertEqual(len(response.data['results']['locations']), 1)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 4)  # collection 4
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 4)  # item 4

        """
        - date
        - Récit : 2
        """
        url = "/advancedsearch/?date_start=1969-09-01&date_end=1969-09-07&domain_tale=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 2)
        self.assertEqual(len(response.data['results']['locations']), 1)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 2)  # collection 2
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 1)  # item 1
        self.assertEqual(response.data['results']['items'][1]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][1]['id'], 2)  # item 2

    def test_multi_criteria_or(self):
        """
        - instrument : 2 - voix d'homme
        - instrument : 1 - violon
        """
        url = "/advancedsearch/?instrument=2&instrument=1&or_operators=instrument"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 2)
        self.assertEqual(len(response.data['results']['items']), 1)
        self.assertEqual(len(response.data['results']['locations']), 2)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 2)  # collection 2
        self.assertEqual(response.data['results']['collections'][1]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][1]['id'], 3)  # collection 3
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 2)  # item 2

        """
        - dance : 2 - valse
        - dance : 1 - polka
        """
        url = "/advancedsearch/?dance=2&dance=1&or_operators=dance"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 1)
        self.assertEqual(len(response.data['results']['items']), 2)
        self.assertEqual(len(response.data['results']['locations']), 1)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 2)  # collection 2
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 1)  # item 1
        self.assertEqual(response.data['results']['items'][1]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][1]['id'], 2)  # item 2

        """
        - collector : 3 - Jeanne d'Arc Lortie
        - collector : 6 - Jeanne-Marie Bourreau
        """
        url = "/advancedsearch/?collector=3&collector=6&or_operators=collector"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 3)
        self.assertEqual(len(response.data['results']['items']), 0)
        self.assertEqual(len(response.data['results']['locations']), 3)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 1)  # collection 1
        self.assertEqual(response.data['results']['collections'][1]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][1]['id'], 2)  # collection 2
        self.assertEqual(response.data['results']['collections'][2]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][2]['id'], 3)  # collection 3

        """
        - informer : 4 - Charles Aubrière
        - informer : 2 - Cecilia Mc Graw
        """
        url = "/advancedsearch/?informer=2&informer=4&or_operators=informer"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 3)
        self.assertEqual(len(response.data['results']['items']), 2)
        self.assertEqual(len(response.data['results']['locations']), 3)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 1)  # collection 1
        self.assertEqual(response.data['results']['collections'][1]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][1]['id'], 2)  # collection 2
        self.assertEqual(response.data['results']['collections'][2]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][2]['id'], 3)  # collection 3
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 1)  # item 1
        self.assertEqual(response.data['results']['items'][1]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][1]['id'], 2)  # item 2

        """
        - coupe : 1 - Charles Aubrière
        - coupe : 2 - Cecilia Mc Graw
        """
        url = "/advancedsearch/?coupe=1&coupe=2&or_operators=coupe"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 2)
        self.assertEqual(len(response.data['results']['items']), 3)
        self.assertEqual(len(response.data['results']['locations']), 2)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 1)  # collection 1
        self.assertEqual(response.data['results']['collections'][1]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][1]['id'], 2)  # collection 2
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 3)  # item 3
        self.assertEqual(response.data['results']['items'][1]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][1]['id'], 1)  # item 1
        self.assertEqual(response.data['results']['items'][2]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][2]['id'], 2)  # item 2

        """
        - fonction : 1 - ecouter
        - fonction : 2 - danser
        """
        url = "/advancedsearch/?usefulness=1&usefulness=2&or_operators=usefulness"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 3)
        self.assertEqual(len(response.data['results']['items']), 3)
        self.assertEqual(len(response.data['results']['locations']), 3)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 1)  # collection 1
        self.assertEqual(response.data['results']['collections'][1]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][1]['id'], 4)  # collection 4
        self.assertEqual(response.data['results']['collections'][2]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][2]['id'], 2)  # collection 2
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 3)  # item 3
        self.assertEqual(response.data['results']['items'][1]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][1]['id'], 4)  # item 4
        self.assertEqual(response.data['results']['items'][2]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][2]['id'], 1)  # item 1

        """
        - thématique : 1 - danse
        - thématique : 2 - récit
        """
        url = "/advancedsearch/?thematic=1&thematic=2&or_operators=thematic"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']['collections']), 2)
        self.assertEqual(len(response.data['results']['items']), 3)
        self.assertEqual(len(response.data['results']['locations']), 2)
        self.assertEqual(response.data['results']['collections'][0]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][0]['id'], 4)  # collection 4
        self.assertEqual(response.data['results']['collections'][1]['entity'], 'Collection')
        self.assertEqual(response.data['results']['collections'][1]['id'], 2)  # collection 2
        self.assertEqual(response.data['results']['items'][0]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][0]['id'], 4)  # item 4
        self.assertEqual(response.data['results']['items'][1]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][1]['id'], 1)  # item 1
        self.assertEqual(response.data['results']['items'][2]['entity'], 'Item')
        self.assertEqual(response.data['results']['items'][2]['id'], 2)  # item 2
