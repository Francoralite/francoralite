import pytest

from rest_framework.test import APITestCase
from rest_framework import status


@pytest.mark.django_db
class TestAdvancedSearch(APITestCase):
    """
    This class tests advanced search
    """

    fixtures = ['francoralite.json']

    def _test_informer(self):
        url = "/advancedsearch/?informer=4"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["id"], 2)  # collection 2
        self.assertEqual(response.data[1]["id"], 1)  # item 1
        self.assertEqual(response.data[2]["id"], 2)  # item 2

    def _test_collector(self):
        url = "/advancedsearch/?collector=8"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["id"], 1)  # item 1
        self.assertEqual(response.data[1]["id"], 2)  # item 2

        url = "/advancedsearch/?collector=6"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["id"], 2)  # collection 2

    def test_location(self):
        url = "/advancedsearch/?location=3"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 2)  # collection 2
        self.assertEqual(response.data[1]["entity"], "Collection")
        self.assertEqual(response.data[1]["id"], 3)  # collection 3
        self.assertEqual(response.data[2]["entity"], "Item")
        self.assertEqual(response.data[2]["id"], 1)  # item 1
        self.assertEqual(response.data[3]["entity"], "Item")
        self.assertEqual(response.data[3]["id"], 2)  # item 2

    def test_dance(self):
        url = "/advancedsearch/?dance=1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 2)  # collection 2
        self.assertEqual(response.data[1]["entity"], "Item")
        self.assertEqual(response.data[1]["id"], 1)  # item 1
        self.assertEqual(response.data[2]["entity"], "Item")
        self.assertEqual(response.data[2]["id"], 2)  # item 2

        url = "/advancedsearch/?dance=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 2)  # collection 2
        self.assertEqual(response.data[1]["entity"], "Item")
        self.assertEqual(response.data[1]["id"], 2)  # item 2

        url = "/advancedsearch/?dance=3"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
        
    def test_collector(self):
        url = "/advancedsearch/?collector=3"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 1)  # collection 1
        
        url = "/advancedsearch/?collector=8"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 4)  # collection 4
        self.assertEqual(response.data[1]["entity"], "Item")
        self.assertEqual(response.data[1]["id"], 4)  # item 4
        self.assertEqual(response.data[2]["entity"], "Item")
        self.assertEqual(response.data[2]["id"], 1)  # item 1
        self.assertEqual(response.data[3]["entity"], "Item")
        self.assertEqual(response.data[3]["id"], 2)  # item 2
        
    def test_informer(self):
        url = "/advancedsearch/?informer=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 1)  # collection 1
        
        url = "/advancedsearch/?informer=4"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 2)  # collection 2
        self.assertEqual(response.data[1]["entity"], "Collection")
        self.assertEqual(response.data[1]["id"], 3)  # collection 3
        self.assertEqual(response.data[2]["entity"], "Item")
        self.assertEqual(response.data[2]["id"], 1)  # item 1
        self.assertEqual(response.data[3]["entity"], "Item")
        self.assertEqual(response.data[3]["id"], 2)  # item 2
        
    def test_coupe(self):
        url = "/advancedsearch/?coupe=1"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 2)  # collection 2
        self.assertEqual(response.data[1]["entity"], "Item")
        self.assertEqual(response.data[1]["id"], 1)  # item 1
        self.assertEqual(response.data[2]["entity"], "Item")
        self.assertEqual(response.data[2]["id"], 2)  # item 2
        
        url = "/advancedsearch/?coupe=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 1)  # collection 1
        self.assertEqual(response.data[1]["entity"], "Item")
        self.assertEqual(response.data[1]["id"],3)  # item 3
        
    def test_refrain(self):
        url = "/advancedsearch/?refrain=rose%20au%20bois"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["entity"], "Item")
        self.assertEqual(response.data[0]["id"], 4)  # item 4
    
    def test_incipit(self):
        url = "/advancedsearch/?incipit=école%20du%20roi"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["entity"], "Item")
        self.assertEqual(response.data[0]["id"], 4)  # item 4
        
        url = "/advancedsearch/?incipit=ordinateur"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
        
    def test_timbre(self):
        url = "/advancedsearch/?timbre=timbre_1"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["entity"], "Item")
        self.assertEqual(response.data[0]["id"], 1)  # item 1
        self.assertEqual(response.data[1]["entity"], "Item")
        self.assertEqual(response.data[1]["id"], 2)  # item 2
        
        url = "/advancedsearch/?timbre=timbre_2"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["entity"], "Item")
        self.assertEqual(response.data[0]["id"], 4)  # item 4
        
    def test_timbre_ref(self):
        url = "/advancedsearch/?timbre_ref=timbre_ref_1"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["entity"], "Item")
        self.assertEqual(response.data[0]["id"], 1)  # item 1
        self.assertEqual(response.data[1]["entity"], "Item")
        self.assertEqual(response.data[1]["id"], 2)  # item 2
        
        url = "/advancedsearch/?timbre_ref=timbre_ref_2"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["entity"], "Item")
        self.assertEqual(response.data[0]["id"], 4)  # item 4
        
    def test_usefulness(self):
        url = "/advancedsearch/?usefulness=1"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 4)  # collection 4
        self.assertEqual(response.data[1]["entity"], "Collection")
        self.assertEqual(response.data[1]["id"], 2)  # collection 2
        self.assertEqual(response.data[2]["entity"], "Item")
        self.assertEqual(response.data[2]["id"], 4)  # item 4
        self.assertEqual(response.data[3]["entity"], "Item")
        self.assertEqual(response.data[3]["id"], 1)  # item 1
        
    def test_thematic(self):
        url = "/advancedsearch/?thematic=1"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 4)  # collection 4
        self.assertEqual(response.data[1]["entity"], "Collection")
        self.assertEqual(response.data[1]["id"], 2)  # collection 2
        self.assertEqual(response.data[2]["entity"], "Item")
        self.assertEqual(response.data[2]["id"], 4)  # item 4
        self.assertEqual(response.data[3]["entity"], "Item")
        self.assertEqual(response.data[3]["id"], 2)  # item 2

    def test_multi_criteria(self):
        """
        - instrument : 2 - voix d'homme
        """
        url = "/advancedsearch/?instrument=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 2)  # collection 2
        self.assertEqual(response.data[1]["entity"], "Collection")
        self.assertEqual(response.data[1]["id"], 3)  # collection 3
        self.assertEqual(response.data[2]["entity"], "Item")
        self.assertEqual(response.data[2]["id"], 2)  # item 2

        """
        - instrument : 2 - voix d'homme
        - instrument : 1 - violon
        """
        url = "/advancedsearch/?instrument=2&instrument=1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 3)  # collection 3

        """
        - dance : 2 - valse
        - instrument : 2 - voix d'homme
        """
        url = "/advancedsearch/?dance=2&instrument=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 2)  # Collection 2
        self.assertEqual(response.data[1]["entity"], "Item")
        self.assertEqual(response.data[1]["id"], 2)  # item 2

        """
        - dance : 1 - polka
        - instrument : 2 - voix d'homme
        """
        url = "/advancedsearch/?dance=1&instrument=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 2)  # Collection 2
        self.assertEqual(response.data[1]["entity"], "Item")
        self.assertEqual(response.data[1]["id"], 2)  # item 2

        """
        - dance : 2 - valse
        - instrument : 1 - violon
        """
        url = "/advancedsearch/?dance=2&instrument=1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
        
        """
        - collector : 6 - Jeanne-Marie Bourreau
        - instrument : 1 - violon
        """
        url = "/advancedsearch/?collector=6&instrument=1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 3)  # Collection 3
        
        """
        - informer : 4 - Charles Aubrière
        - informer : 5 - Mme Aubrière
        """
        url = "/advancedsearch/?informer=4&informer=5"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 2)  # Collection 2
        self.assertEqual(response.data[1]["entity"], "Collection")
        self.assertEqual(response.data[1]["id"], 3)  # Collection 3
        
        """
        - informer : 4 - Charles Aubrière
        - informer : 2 - Cecilia Mc Graw
        """
        url = "/advancedsearch/?informer=4&informer=2"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
        
        """
        - coupe : 1 - AABB
        - instrument : 2 - voix d'homme
        """
        url = "/advancedsearch/?coupe=1&instrument=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 2)  # Collection 2
        self.assertEqual(response.data[1]["entity"], "Item")
        self.assertEqual(response.data[1]["id"], 2)  # item 2
        
        """
        - fonction : 1 - ecouter
        - fonction : 2 - danser
        """
        url = "/advancedsearch/?usefulness=1&usefulness=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 2)  # collection 2
        self.assertEqual(response.data[1]["entity"], "Item")
        self.assertEqual(response.data[1]["id"], 1)  # item 1
        
        """
        - thématique : 1 - danse
        - thématique : 2 - récit
        """
        url = "/advancedsearch/?thematic=1&thematic=2"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 2)  # collection 2
        self.assertEqual(response.data[1]["entity"], "Item")
        self.assertEqual(response.data[1]["id"], 2)  # item 2

    def test_multi_criteria_or(self):
        """
        - instrument : 2 - voix d'homme
        - instrument : 1 - violon
        """
        url = "/advancedsearch/?instrument=2&instrument=1&or_operators=instrument"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 2)  # collection 2
        self.assertEqual(response.data[1]["entity"], "Collection")
        self.assertEqual(response.data[1]["id"], 3)  # collection 3
        self.assertEqual(response.data[2]["entity"], "Item")
        self.assertEqual(response.data[2]["id"], 2)  # item 2

        """
        - dance : 2 - valse
        - dance : 1 - polka
        """
        url = "/advancedsearch/?dance=2&dance=1&or_operators=dance"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 2)  # collection 2
        self.assertEqual(response.data[1]["entity"], "Item")
        self.assertEqual(response.data[1]["id"], 1)  # item 1
        self.assertEqual(response.data[2]["entity"], "Item")
        self.assertEqual(response.data[2]["id"], 2)  # item 2
        
        """
        - collector : 3 - Jeanne d'Arc Lortie
        - collector : 6 - Jeanne-Marie Bourreau
        """
        url = "/advancedsearch/?collector=3&collector=6&or_operators=collector"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 1)  # collection 1
        self.assertEqual(response.data[1]["entity"], "Collection")
        self.assertEqual(response.data[1]["id"], 2)  # collection 2
        self.assertEqual(response.data[2]["entity"], "Collection")
        self.assertEqual(response.data[2]["id"], 3)  # collection 3
        
        """
        - informer : 4 - Charles Aubrière
        - informer : 2 - Cecilia Mc Graw
        """
        url = "/advancedsearch/?informer=2&informer=4&or_operators=informer"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 1)  # collection 1
        self.assertEqual(response.data[1]["entity"], "Collection")
        self.assertEqual(response.data[1]["id"], 2)  # collection 2
        self.assertEqual(response.data[2]["entity"], "Collection")
        self.assertEqual(response.data[2]["id"], 3)  # collection 3
        self.assertEqual(response.data[3]["entity"], "Item")
        self.assertEqual(response.data[3]["id"], 1)  # item 1
        self.assertEqual(response.data[4]["entity"], "Item")
        self.assertEqual(response.data[4]["id"], 2)  # item 2
        
        """
        - coupe : 1 - Charles Aubrière
        - coupe : 2 - Cecilia Mc Graw
        """
        url = "/advancedsearch/?coupe=1&coupe=2&or_operators=coupe"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 1)  # collection 1
        self.assertEqual(response.data[1]["entity"], "Collection")
        self.assertEqual(response.data[1]["id"], 2)  # collection 2
        self.assertEqual(response.data[2]["entity"], "Item")
        self.assertEqual(response.data[2]["id"], 3)  # item 3
        self.assertEqual(response.data[3]["entity"], "Item")
        self.assertEqual(response.data[3]["id"], 1)  # item 1
        self.assertEqual(response.data[4]["entity"], "Item")
        self.assertEqual(response.data[4]["id"], 2)  # item 2
        
        
        """
        - fonction : 1 - ecouter
        - fonction : 2 - danser
        """
        url = "/advancedsearch/?usefulness=1&usefulness=2&or_operators=usefulness"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 1)  # collection 1
        self.assertEqual(response.data[1]["entity"], "Collection")
        self.assertEqual(response.data[1]["id"], 4)  # collection 4
        self.assertEqual(response.data[2]["entity"], "Collection")
        self.assertEqual(response.data[2]["id"], 2)  # collection 2
        self.assertEqual(response.data[3]["entity"], "Item")
        self.assertEqual(response.data[3]["id"], 3)  # item 3
        self.assertEqual(response.data[4]["entity"], "Item")
        self.assertEqual(response.data[4]["id"], 4)  # item 4
        self.assertEqual(response.data[5]["entity"], "Item")
        self.assertEqual(response.data[5]["id"], 1)  # item 1
        
        """
        - thématique : 1 - danse
        - thématique : 2 - récit
        """
        url = "/advancedsearch/?thematic=1&thematic=2&or_operators=thematic"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.data[0]["entity"], "Collection")
        self.assertEqual(response.data[0]["id"], 4)  # collection 4
        self.assertEqual(response.data[1]["entity"], "Collection")
        self.assertEqual(response.data[1]["id"], 2)  # collection 2
        self.assertEqual(response.data[2]["entity"], "Item")
        self.assertEqual(response.data[2]["id"], 4)  # item 4
        self.assertEqual(response.data[3]["entity"], "Item")
        self.assertEqual(response.data[3]["id"], 1)  # item 1
        self.assertEqual(response.data[4]["entity"], "Item")
        self.assertEqual(response.data[4]["id"], 2)  # item 2
