import pytest

from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase


@pytest.mark.django_db
class TestAdvancedSearch(APITestCase):
    """
    This class tests advanced search
    """

    fixtures = ['francoralite.json']

    def _test_advanced_search(self, params, collections, items):
        response = self.client.get('/advancedsearch/?' + params)
        self.assertEqual(response.status_code, HTTP_200_OK)

        response_collections = response.data['results']['collections']
        response_items = response.data['results']['items']
        response_locations = response.data['results']['locations']

        self.assertEqual(len(response_collections), len(collections))
        self.assertEqual(len(response_items), len(items))
        self.assertEqual(len(response_locations), len(collections))

        response_collections_ids = tuple(c['id'] for c in response_collections)
        response_items_ids = tuple(i['id'] for i in response_items)

        if isinstance(collections, (tuple, list)):
            self.assertEqual(tuple(response_collections_ids), tuple(collections))
        elif isinstance(collections, (frozenset, set, dict)):
            self.assertEqual(set(response_collections_ids), set(collections))
        else:
            raise NotImplementedError

        if isinstance(items, (tuple, list)):
            self.assertEqual(tuple(response_items_ids), tuple(items))
        elif isinstance(items, (frozenset, set, dict)):
            self.assertEqual(set(response_items_ids), set(items))
        else:
            raise NotImplementedError

    # ------------------------------------------------------------------------

    def test_code_external(self):
        self._test_advanced_search(
            params='code_external=56-10-138',
            collections={4},  # TODO à vérifier
            items={4},  # TODO à vérifier
        )

        self._test_advanced_search(
            params='code_external=MUS1969.33.2',
            collections={},
            items={2, 3},  # TODO à vérifier
        )

        #TODO opérateur AND

        #TODO opérateur OR

        #TODO opérateur NOR

    def test_code_internal(self):
        self._test_advanced_search(
            params='code_internal=UPOI',
            collections={1, 2, 3, 4},  # TODO à vérifier
            items={1, 2, 3, 4},  # TODO à vérifier
        )

        self._test_advanced_search(
            params='code_internal=UPOI_ATP',
            collections={2, 3, 4},  # TODO à vérifier
            items={1, 2, 4},  # TODO à vérifier
        )

        self._test_advanced_search(
            params='code_internal=UPOI_ATP_0001',
            collections={2, 3},  # TODO à vérifier
            items={1, 2},  # TODO à vérifier
        )

        self._test_advanced_search(
            params='code_internal=UPOI_ATP_0001_0001',
            collections={2},  # TODO à vérifier
            items={1, 2},  # TODO à vérifier
        )

        self._test_advanced_search(
            params='code_internal=UPOI_ATP_0001_0001_002',
            collections={2},  # TODO à vérifier
            items={2},  # TODO à vérifier
        )

        #TODO opérateur AND

        #TODO opérateur OR

        #TODO opérateur NOR

    def test_coirault(self):
        self._test_advanced_search(
            params='coirault=1',
            collections={1, 2},  # TODO à vérifier
            items={1, 3},  # TODO à vérifier
        )

        self._test_advanced_search(
            params='coirault=2',
            collections={1, 2},  # TODO à vérifier
            items={2, 3},  # TODO à vérifier
        )

        self._test_advanced_search(
            params='coirault=1&coirault=2',
            collections={1, 2},  # TODO à vérifier
            items={3},  # TODO à vérifier
        )

        self._test_advanced_search(
            params='coirault=1&coirault=2&coirault_operator=or',
            collections={1, 2},  # TODO à vérifier
            items={1, 2, 3},  # TODO à vérifier
        )

        #TODO opérateur NOR

    def test_collector(self):
        """
        - collector : 3 - Jeanne d'Arc Lortie
        """
        self._test_advanced_search(
            params='collector=3',
            collections={1},
            items={},
        )

        """
        - collector : 6 - Jeanne-Marie Bourreau
        """
        self._test_advanced_search(
            params='collector=6',
            collections={2, 3},
            items={},
        )

        """
        - collector : 8 - Marcel-Dubois Claudie
        """
        self._test_advanced_search(
            params='collector=8',
            collections={4},
            items={1, 2, 4},
        )

        #TODO opérateur AND

        """
        - collector : 3 - Jeanne d'Arc Lortie
        - collector : 6 - Jeanne-Marie Bourreau
        """
        self._test_advanced_search(
            params='collector=3&collector=6&collector_operator=or',
            collections={1, 2, 3},
            items={},
        )

        #TODO opérateur NOR

    def test_collector_civility(self):
        pass

        #TODO 3 fois le critère unique : Mr, Mme, Mlle

        #TODO opérateur AND

        #TODO opérateur OR

        #TODO opérateur NOR

    def test_coupe(self):
        """
        - coupe : 1 - AABB
        """
        self._test_advanced_search(
            params='coupe=1',
            collections={2},
            items={1, 2},
        )

        """
        - coupe : 2 - ABCD
        """
        self._test_advanced_search(
            params='coupe=2',
            collections={1},
            items={3},
        )

        #TODO opérateur AND

        """
        - coupe : 1 - AABB
        - coupe : 2 - ABCD
        """
        self._test_advanced_search(
            params='coupe=1&coupe=2&coupe_operator=or',
            collections={1, 2},
            items={1, 2, 3},
        )

        #TODO opérateur NOR

    def test_cultural_area(self):
        pass

        #TODO critère unique : 2 fois avec textes différents

        #TODO opérateur AND

        #TODO opérateur OR

        #TODO opérateur NOR

    def test_dance(self):
        """
        - dance : 1 - polka
        """
        self._test_advanced_search(
            params='dance=1',
            collections={2},
            items={1, 2},
        )

        """
        - dance : 2 - valse
        """
        self._test_advanced_search(
            params='dance=2',
            collections={2},
            items={2},
        )

        """
        - dance : 3 - mazurka
        """
        self._test_advanced_search(
            params='dance=3',
            collections={},
            items={},
        )

        #TODO opérateur AND

        """
        - dance : 2 - valse
        - dance : 1 - polka
        """
        self._test_advanced_search(
            params='dance=2&dance=1&dance_operator=or',
            collections={2},
            items={1, 2},
        )

        #TODO opérateur NOR

    def test_date(self):
        self._test_advanced_search(
            params='date_start=1969-09-05&date_end=1969-09-07',
            collections={3},
            items={},
        )

        self._test_advanced_search(
            params='date_start=1969-09-01&date_end=1969-09-07',
            collections={2, 3},
            items={1, 2},
        )

        self._test_advanced_search(
            params='date_start=1969-09-05',
            collections={3},
            items={},
        )

        self._test_advanced_search(
            params='date_end=1969-09-05',
            collections={1, 2, 4},  # TODO à vérifier
            items={1, 2, 3, 4},  # TODO à vérifier
        )

    def test_domain_music(self):
        """
        - domain music : 1 - air de musique
        """
        self._test_advanced_search(
            params='domain_music=1',
            collections={},
            items={},
        )

        """
        - domain music : 2 - air de chanson
        """
        self._test_advanced_search(
            params='domain_music=2',
            collections={4},
            items={4},
        )

        #TODO opérateur AND

        #TODO opérateur OR

        #TODO opérateur NOR

    def test_domain_song(self):
        """
        - domain song : 1 - relations sociales
        """
        self._test_advanced_search(
            params='domain_song=1',
            collections={},
            items={},
        )

        """
        - domain song : 2 - mariage
        """
        self._test_advanced_search(
            params='domain_song=2',
            collections={4},
            items={4},
        )

        """
        - domain song : 2 - mariage
        - domain song : 3 - éducation
        """
        self._test_advanced_search(
            params='domain_song=2&domain_song=3',
            collections={4},
            items={4},
        )

        #TODO opérateur OR

        #TODO opérateur NOR

    def test_domain_tale(self):
        """
        - domain tale : 1 - conte facétieux
        """
        self._test_advanced_search(
            params='domain_tale=1',
            collections={},
            items={},
        )

        """
        - domain tale : 2 - récit
        """
        self._test_advanced_search(
            params='domain_tale=2',
            collections={1, 2},
            items={1, 2, 3},
        )

        #TODO opérateur AND

        #TODO opérateur OR

        #TODO opérateur NOR

    def test_domain_vocal(self):
        """
        - domain vocal : 1 - comptine
        """
        self._test_advanced_search(
            params='domain_vocal=1',
            collections={},
            items={},
        )

        #TODO critère unique : autre id

        #TODO opérateur AND

        #TODO opérateur OR

        #TODO opérateur NOR

    def test_incipit(self):
        self._test_advanced_search(
            params='incipit=école%20du%20roi',
            collections={},
            items={4},
        )

        self._test_advanced_search(
            params='incipit=ordinateur',
            collections={},
            items={},
        )

        #TODO opérateur AND

        #TODO opérateur OR

        #TODO opérateur NOR

    def test_informer(self):
        """
        - informer : 2 - Cecilia Mc Graw
        """
        self._test_advanced_search(
            params='informer=2',
            collections={1},
            items={},
        )

        """
        - informer : 4 - Charles Aubrière
        """
        self._test_advanced_search(
            params='informer=4',
            collections={2, 3},
            items={1, 2},
        )

        """
        - informer : 4 - Charles Aubrière
        - informer : 5 - Mme Aubrière
        """
        self._test_advanced_search(
            params='informer=4&informer=5',
            collections={2, 3},
            items={},
        )

        """
        - informer : 4 - Charles Aubrière
        - informer : 2 - Cecilia Mc Graw
        """
        self._test_advanced_search(
            params='informer=4&informer=2',
            collections={},
            items={},
        )

        """
        - informer : 4 - Charles Aubrière
        - informer : 2 - Cecilia Mc Graw
        """
        self._test_advanced_search(
            params='informer=4&informer=2&informer_operator=or',
            collections={1, 2, 3},
            items={1, 2},
        )

        #TODO opérateur NOR

    def test_informer_civility(self):
        pass

        #TODO 3 fois le critère unique : Mr, Mme, Mlle

        #TODO opérateur AND

        #TODO opérateur OR

        #TODO opérateur NOR

    def test_instrument(self):
        """
        - instrument : 1 - violon
        """
        self._test_advanced_search(
            params='instrument=1',
            collections={3},
            items={},
        )

        """
        - instrument : 2 - voix d'homme
        """
        self._test_advanced_search(
            params='instrument=2',
            collections={2, 3},
            items={2},
        )

        """
        - instrument : 3 - voix de fille
        """
        self._test_advanced_search(
            params='instrument=3',
            collections={4},
            items={4},
        )

        """
        - instrument : 1 - violon
        - instrument : 2 - voix d'homme
        """
        self._test_advanced_search(
            params='instrument=1&instrument=2',
            collections={3},
            items={},
        )

        """
        - instrument : 1 - violon
        - instrument : 3 - voix de fille
        """
        self._test_advanced_search(
            params='instrument=1&instrument=3',
            collections={},
            items={},
        )

        """
        - instrument : 2 - voix d'homme
        - instrument : 3 - voix de fille
        """
        self._test_advanced_search(
            params='instrument=2&instrument=3',
            collections={},
            items={},
        )

        """
        - instrument : 1 - violon
        - instrument : 2 - voix d'homme
        - instrument : 3 - voix de fille
        """
        self._test_advanced_search(
            params='instrument=1&instrument=2&instrument=3',
            collections={},
            items={},
        )

        """
        - instrument : 1 - violon
        - instrument : 2 - voix d'homme
        """
        self._test_advanced_search(
            params='instrument=1&instrument=2&instrument_operator=or',
            collections={2, 3},
            items={2},
        )

        """
        - instrument : 1 - violon
        - instrument : 3 - voix de fille
        """
        self._test_advanced_search(
            params='instrument=1&instrument=3&instrument_operator=or',
            collections={3, 4},
            items={4},
        )

        """
        - instrument : 2 - voix d'homme
        - instrument : 3 - voix de fille
        """
        self._test_advanced_search(
            params='instrument=2&instrument=3&instrument_operator=or',
            collections={2, 3, 4},
            items={2, 4},
        )

        """
        - instrument : 1 - violon
        - instrument : 2 - voix d'homme
        - instrument : 3 - voix de fille
        """
        self._test_advanced_search(
            params='instrument=1&instrument=2&instrument=3&instrument_operator=or',
            collections={2, 3, 4},
            items={2, 4},
        )

        """
        - instrument : 1 - violon
        """
        self._test_advanced_search(
            params='instrument=1&instrument_operator=nor',
            collections={1, 2, 4},
            items={1, 2, 3, 4},
        )

        """
        - instrument : 2 - voix d'homme
        """
        self._test_advanced_search(
            params='instrument=2&instrument_operator=nor',
            collections={1, 4},
            items={1, 3, 4},
        )

        """
        - instrument : 3 - voix de fille
        """
        self._test_advanced_search(
            params='instrument=3&instrument_operator=nor',
            collections={1, 2, 3},
            items={1, 2, 3},
        )

        """
        - instrument : 1 - violon
        - instrument : 2 - voix d'homme
        """
        self._test_advanced_search(
            params='instrument=1&instrument=2&instrument_operator=nor',
            collections={1, 4},
            items={1, 3, 4},
        )

        """
        - instrument : 1 - violon
        - instrument : 3 - voix de fille
        """
        self._test_advanced_search(
            params='instrument=1&instrument=3&instrument_operator=nor',
            collections={1, 2},
            items={1, 2, 3},
        )

        """
        - instrument : 2 - voix d'homme
        - instrument : 3 - voix de fille
        """
        self._test_advanced_search(
            params='instrument=2&instrument=3&instrument_operator=nor',
            collections={1},
            items={1, 3},
        )

        """
        - instrument : 1 - violon
        - instrument : 2 - voix d'homme
        - instrument : 3 - voix de fille
        """
        self._test_advanced_search(
            params='instrument=1&instrument=2&instrument=3&instrument_operator=nor',
            collections={1},
            items={1, 3},
        )

    def test_jingle(self):
        pass

        #TODO critère unique : 2 fois avec textes différents

        #TODO opérateur AND

        #TODO opérateur OR

        #TODO opérateur NOR

    def test_location(self):
        """
        - location : 3 - La Biroire
        """
        self._test_advanced_search(
            params='location=3',
            collections={2, 3},
            items={1, 2},
        )

        #TODO critère unique : autre id

        #TODO opérateur AND

        #TODO opérateur OR

        #TODO opérateur NOR

    def test_media_type(self):
        """
        - media type : 1 - cassette audio
        """
        self._test_advanced_search(
            params='media_type=1',
            collections={},
            items={},
        )

        """
        - media type : 2 - bande dat
        """
        self._test_advanced_search(
            params='media_type=2',
            collections={1, 2, 3},  # TODO à vérifier
            items={1, 2, 3},  # TODO à vérifier
        )

        """
        - media type : 3 - son uniquement
        """
        self._test_advanced_search(
            params='media_type=3',
            collections={4},  # TODO à vérifier
            items={4},  # TODO à vérifier
        )

        #TODO opérateur AND

        #TODO opérateur OR

        #TODO opérateur NOR

    def test_recording_context(self):
        """
        - recording context : 1 - collectage
        """
        self._test_advanced_search(
            params='recording_context=1',
            collections={2, 3},  # TODO à vérifier
            items={1, 2},  # TODO à vérifier
        )

        """
        - recording context : 3 - enquête
        """
        self._test_advanced_search(
            params='recording_context=3',
            collections={1},  # TODO à vérifier
            items={3},  # TODO à vérifier
        )

        """
        - recording context : 6 - TODO à créer dans les fixtures et nom à mettre ici
        """
        self._test_advanced_search(
            params='recording_context=6',
            collections={4},  # TODO à vérifier
            items={4},  # TODO à vérifier
        )

        #TODO opérateur AND

        #TODO opérateur OR

        #TODO opérateur NOR

    def test_refrain(self):
        self._test_advanced_search(
            params='refrain=rose%20au%20bois',
            collections={},
            items={4},
        )

        #TODO critère unique : autre texte

        #TODO opérateur AND

        #TODO opérateur OR

        #TODO opérateur NOR

    def test_text(self):
        pass

        #TODO critère unique : 2 fois avec id différents

        #TODO opérateur AND

        #TODO opérateur OR

        #TODO opérateur NOR

    def test_thematic(self):
        """
        - thématique : 1 - danse
        """
        self._test_advanced_search(
            params='thematic=1',
            collections={2, 4},
            items={2, 4},
        )

        #TODO critère unique : id = 2

        """
        - thématique : 1 - danse
        - thématique : 2 - récit
        """
        self._test_advanced_search(
            params='thematic=1&thematic=2',
            collections={2},
            items={2},
        )

        """
        - thématique : 1 - danse
        - thématique : 2 - récit
        """
        self._test_advanced_search(
            params='thematic=1&thematic=2&thematic_operator=or',
            collections={2, 4},
            items={1, 2, 4},
        )

        #TODO opérateur NOR

    def test_timbre(self):
        self._test_advanced_search(
            params='timbre=timbre_1',
            collections={2},
            items={1, 2},
        )

        self._test_advanced_search(
            params='timbre=timbre_2',
            collections={4},  #TODO à vérifier
            items={4},
        )

        #TODO opérateur AND

        #TODO opérateur OR

        #TODO opérateur NOR

    def test_timbre_ref(self):
        self._test_advanced_search(
            params='timbre_ref=timbre_ref_1',
            collections={2},
            items={1, 2},
        )

        self._test_advanced_search(
            params='timbre_ref=timbre_ref_2',
            collections={4},  #TODO à vérifier
            items={4},
        )

        #TODO opérateur AND

        #TODO opérateur OR

        #TODO opérateur NOR

    def test_usefulness(self):
        """
        - fonction : 1 - écouter
        """
        self._test_advanced_search(
            params='usefulness=1',
            collections={2, 4},
            items={1, 4},
        )

        #TODO critère unique : id = 2

        """
        - fonction : 1 - écouter
        - fonction : 2 - danser
        """
        self._test_advanced_search(
            params='usefulness=1&usefulness=2',
            collections={2},
            items={1},
        )

        """
        - fonction : 1 - écouter
        - fonction : 2 - danser
        """
        self._test_advanced_search(
            params='usefulness=1&usefulness=2&usefulness_operator=or',
            collections={1, 2, 4},
            items={1, 3, 4},
        )

        #TODO opérateur NOR

    # ------------------------------------------------------------------------

    def test_multi_criteria(self):
        """
        - dance : 2 - valse
        - instrument : 2 - voix d'homme
        """
        self._test_advanced_search(
            params='dance=2&instrument=2',
            collections={2},
            items={2},
        )

        """
        - dance : 1 - polka
        - instrument : 2 - voix d'homme
        """
        self._test_advanced_search(
            params='dance=1&instrument=2',
            collections={2},
            items={2},
        )

        """
        - dance : 2 - valse
        - instrument : 1 - violon
        """
        self._test_advanced_search(
            params='dance=2&instrument=1',
            collections={},
            items={},
        )

        """
        - collector : 6 - Jeanne-Marie Bourreau
        - instrument : 1 - violon
        """
        self._test_advanced_search(
            params='collector=6&instrument=1',
            collections={3},
            items={},
        )

        """
        - coupe : 1 - AABB
        - instrument : 2 - voix d'homme
        """
        self._test_advanced_search(
            params='coupe=1&instrument=2',
            collections={2},
            items={2},
        )

        """
        - date : début et fin
        - domain_tale : 2 - récit
        """
        self._test_advanced_search(
            params='date_start=1969-09-01&date_end=1969-09-07&domain_tale=2',
            collections={2},
            items={1, 2},
        )

        """
        - code_internal : UPOI_ATP_0001_0001
        - text : empty value
        """
        self._test_advanced_search(
            params='code_internal=UPOI_ATP_0001_0001&text=',
            collections={2},  # TODO à vérifier
            items={1, 2},  # TODO à vérifier
        )
