from itertools import combinations
from functools import reduce
import pytest

from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase


@pytest.mark.django_db
class TestAdvancedSearch(APITestCase):
    """
    This class tests advanced search
    """

    fixtures = ["francoralite.json"]

    def _test_advanced_search_implementation(self, params, records, locations=None):
        response = self.client.get("/advancedsearch/?" + params)
        self.assertEqual(response.status_code, HTTP_200_OK)

        response_records = response.data["results"]["records"]
        self.assertEqual(len(response_records), len(records))

        if locations is not None:
            response_locations = response.data["results"]["locations"]
            self.assertEqual(len(response_locations), len(locations))

        response_records_ids = tuple(r["id"] for r in response_records)
        if isinstance(records, (tuple, list)):
            self.assertEqual(tuple(response_records_ids), tuple(records))
        elif isinstance(records, (frozenset, set, dict)):
            self.assertEqual(set(response_records_ids), set(records))
        else:
            raise NotImplementedError

    def _test_advanced_search(self, params, collections, items, locations=None):
        self._test_advanced_search_implementation(params, collections, locations)
        self._test_advanced_search_implementation(params + "&request_type=collection", collections, locations)
        self._test_advanced_search_implementation(params + "&request_type=item", items, locations)

    def _test_all_combinations(self, name, results_per_values):
        all_collections = frozenset((1, 2, 3, 4))
        all_items = frozenset((1, 2, 3, 4))
        all_values = tuple(results_per_values)

        and_operator = lambda x, y: x.intersection(y)
        or_operator = lambda x, y: x.union(y)

        for length in range(1, len(results_per_values) + 1):
            for values in combinations(all_values, length):
                params = "&".join("%s=%s" % (name, value) for value in values)

                selected_collections = tuple(
                    frozenset(results.get("collections", {}))
                    for value, results in results_per_values.items()
                    if value in values
                )
                and_collections = reduce(and_operator, selected_collections)
                or_collections = reduce(or_operator, selected_collections)
                nor_collections = all_collections.difference(or_collections)

                selected_items = tuple(
                    frozenset(results.get("items", {}))
                    for value, results in results_per_values.items()
                    if value in values
                )
                and_items = reduce(and_operator, selected_items)
                or_items = reduce(or_operator, selected_items)
                nor_items = all_items.difference(or_items)

                self._test_advanced_search(
                    params=params,  # without explicit operator, it is AND too
                    collections=and_collections,
                    items=and_items,
                )

                self._test_advanced_search(
                    params=params + ("&%s_operator=and" % name),
                    collections=and_collections,
                    items=and_items,
                )

                self._test_advanced_search(
                    params=params + ("&%s_operator=or" % name),
                    collections=or_collections,
                    items=or_items,
                )

                self._test_advanced_search(
                    params=params + ("&%s_operator=nor" % name),
                    collections=nor_collections,
                    items=nor_items,
                )

    # ------------------------------------------------------------------------

    def test_empty_params(self):
        """
        A function that runs the 'test_advanced_search' method with empty parameters.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """
        self._test_advanced_search(
            params="code_internal_operator=or&code_external_operator=or&title=&description=&informer_civility_operator=or&informer_operator=or&collector_civility_operator=or&collector_operator=or&date_start=&date_end=&location_operator=or&cultural_area_operator=or&media_type_operator=or&language_operator=or&recording_context_operator=or&usefulness_operator=or&dance_operator=or&thematic_operator=or&domain_song_operator=or&timbre_operator=or&timbre_ref_operator=or&coupe_operator=or&domain_vocal_operator=or&coirault_operator=or&domain_music_operator=or&instrument_operator=or&domain_tale_operator=or&text=&incipit=&refrain=&jingle=",
            collections={},
            items={},
            locations={},
        )

    def test_void(self):
        """
        A function that runs the 'test_advanced_search' method with void.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """
        self._test_advanced_search(
            params="",
            collections={},
            items={},
            locations={},
        )

    def test_code_external(self):
        """
        - code external : 56-10-138
        - code external : MUS1969.33.2
        """
        self._test_all_combinations(
            "code_external",
            {
                "56-10-138": {"collections": {4}, "items": {4}},
                "MUS1969.33.2": {"items": {2, 3}},
            },
        )

    def test_code_internal(self):
        """
        - code internal : UPOI
        - code internal : UPOI_ATP
        - code internal : UPOI_ATP_0001
        - code internal : UPOI_ATP_0001_0001
        - code internal : UPOI_ATP_0001_0001_002
        """
        self._test_all_combinations(
            "code_internal",
            {
                "UPOI": {"collections": {1, 2, 3, 4}, "items": {1, 2, 3, 4}},
                "UPOI_ATP": {"collections": {2, 3, 4}, "items": {1, 2, 4}},
                "UPOI_ATP_0001": {"collections": {2, 3}, "items": {1, 2}},
                "UPOI_ATP_0001_0001": {"collections": {2}, "items": {1, 2}},
                "UPOI_ATP_0001_0001_002": {"collections": {2}, "items": {2}},
            },
        )

    def test_coirault(self):
        """
        - coirault : 1 - À l’arrivée du doux printemps
        - coirault : 2 - Joli mois de mai, que tu es agréable
        """
        self._test_all_combinations(
            "coirault",
            {
                1: {"collections": {1, 2}, "items": {1, 3}},
                2: {"collections": {1, 2}, "items": {2, 3}},
            },
        )

    def test_collector(self):
        """
        - collector : 1 - Astérix Le Gaulois
        - collector : 3 - Sr Jeanne d'Arc Lortie
        - collector : 6 - Jeanne-Marie Bourreau
        - collector : 8 - Mlle Claudie Marcel-Dubois
        """
        self._test_all_combinations(
            "collector",
            {
                1: {},
                3: {"collections": {1}},
                6: {"collections": {2, 3}},
                8: {"collections": {4}, "items": {1, 2, 4}},
            },
        )

    def test_collector_civility(self):
        """
        - civility : 1 - (Mme)
        - civility : 2 - Mlle
        - civility : 3 - Monsieur
        - civility : 4 - Sr
        """
        self._test_all_combinations(
            "collector_civility",
            {
                1: {"collections": {4}, "items": {1, 2, 4}},
                2: {"collections": {4}, "items": {1, 2, 4}},
                3: {},
                4: {"collections": {1}},
                5: {},
            },
        )

    def test_coupe(self):
        """
        - coupe : 1 - AABB
        - coupe : 2 - ABCD
        """
        self._test_all_combinations(
            "coupe",
            {
                1: {"collections": {2}, "items": {1, 2}},
                2: {"collections": {1}, "items": {3}},
            },
        )

    def test_cultural_area(self):
        """
        - cultural area : Poitou
        - cultural area : Saintonge, Poitou
        - cultural area : Vendée
        """
        self._test_all_combinations(
            "cultural_area",
            {
                "Poitou": {"collections": {3}},
                "Saintonge, Poitou": {"collections": {2}, "items": {1, 2}},
                "Vendée": {"collections": {4}, "items": {4}},
            },
        )

    def test_dance(self):
        """
        - dance : 1 - polka
        - dance : 2 - valse
        - dance : 3 - mazurka
        """
        self._test_all_combinations(
            "dance",
            {
                1: {"collections": {2}, "items": {1, 2}},
                2: {"collections": {2}, "items": {2}},
                3: {},
            },
        )

    def test_date(self):
        self._test_advanced_search(
            params="date_start=1969-09-05&date_end=1969-09-07",
            collections={3},
            items={},
        )

        self._test_advanced_search(
            params="date_start=1969-09-01&date_end=1969-09-07",
            collections={2, 3},
            items={1, 2},
        )

        self._test_advanced_search(
            params="date_start=1969-09-05",
            collections={3},
            items={},
        )

        self._test_advanced_search(
            params="date_end=1969-09-05",
            collections={1, 2, 4},
            items={1, 2, 3, 4},
        )

    def test_description(self):
        self._test_all_combinations(
            "description",
            {
                "violon": {"collections": {2, 3}, "items": {2, 3}},
                "extrait": {"collections": {1, 4}},
                "chanson": {"items": {4}},
                "raconte": {"items": {1}},
            },
        )

    def test_domain_music(self):
        """
        - domain music : 1 - air de musique
        - domain music : 2 - air de chanson
        """
        self._test_all_combinations(
            "domain_music",
            {
                1: {},
                2: {"collections": {4}, "items": {4}},
            },
        )

    def test_domain_song(self):
        """
        - domain song : 1 - relations sociales
        - domain song : 2 - mariage
        - domain song : 3 - éducation
        """
        self._test_all_combinations(
            "domain_song",
            {
                1: {},
                2: {"collections": {4}, "items": {4}},
                3: {"collections": {4}, "items": {4}},
            },
        )

    def test_domain_tale(self):
        """
        - domain tale : 1 - conte facétieux
        - domain tale : 2 - récit
        """
        self._test_all_combinations(
            "domain_tale",
            {
                1: {},
                2: {"collections": {1, 2}, "items": {1, 2, 3}},
            },
        )

    def test_domain_vocal(self):
        """
        - domain vocal : 1 - comptine
        """
        self._test_all_combinations(
            "domain_vocal",
            {
                1: {},
            },
        )

    def test_incipit(self):
        self._test_advanced_search(
            params="incipit=école%20du%20roi",
            collections={},
            items={4},
        )

        # TODO critère unique : autres textes (ajouter du texte sur d’autres items pour améliorer les tests)

        self._test_advanced_search(
            params="incipit=ordinateur",
            collections={},
            items={},
        )

    def test_informer(self):
        """
        - informer : 1 - Astérix Le Gaulois
        - informer : 2 - Sr Cecilia Mc Graw
        - informer : 4 - Monsieur Charles Aubrière
        - informer : 5 - (Mme) Mme Aubrière
        - informer : 9 - Mlle Michèle Bouchereau
        """
        self._test_all_combinations(
            "informer",
            {
                1: {},
                2: {"collections": {1}},
                4: {"collections": {2, 3}, "items": {1, 2}},
                5: {"collections": {2, 3}},
                9: {"collections": {4}, "items": {4}},
            },
        )

    def test_informer_civility(self):
        """
        - civility : 1 - (Mme)
        - civility : 2 - Mlle
        - civility : 3 - Monsieur
        - civility : 4 - Sr
        """
        self._test_all_combinations(
            "informer_civility",
            {
                1: {"collections": {2, 3}},
                2: {"collections": {4}, "items": {4}},
                3: {"collections": {2, 3}, "items": {1, 2}},
                4: {"collections": {1}},
                5: {},
            },
        )

    def test_instrument(self):
        """
        - instrument : 1 - violon
        - instrument : 2 - voix d'homme
        - instrument : 3 - voix de fille
        """
        self._test_all_combinations(
            "instrument",
            {
                1: {"collections": {3}},
                2: {"collections": {2, 3}, "items": {2}},
                3: {"collections": {4}, "items": {4}},
            },
        )

    def test_jingle(self):
        pass  # TODO critère unique : textes différents (cf incipit)

    def test_keyword(self):
        """
        - keyword : 1 - violon
        - keyword : 2 - biographie
        """
        self._test_all_combinations(
            "keyword",
            {
                1: {"collections": {1, 2}, "items": {1, 2, 3}},
                2: {"collections": {1, 2}, "items": {2, 3}},
            },
        )

    def test_language(self):
        """
        - language : 1 - Anglais
        - language : 2 - Créoles et pidgins basés sur l'anglais
        - language : 3 - Créoles et pidgins basés sur le français
        - language : 4 - Français
        - language : 5 - Poitevin-saintongeais
        """
        self._test_all_combinations(
            "language",
            {
                1: {"items": {4}},
                2: {},
                3: {"collections": {4}, "items": {2}},
                4: {"collections": {1, 2, 4}, "items": {1, 4}},
                5: {"collections": {2}},
            },
        )

    def test_laforte(self):
        """
        - laforte : I.A01 - Gabriel (archange)
        - laforte : I.A02 - La fuite en Égypte : Le blé
        """
        self._test_all_combinations(
            "laforte",
            {
                1: {"collections": {2}, "items": {1, 2}},
                2: {"collections": {2}, "items": {2}},
            },
        )

    def test_location(self):
        """
        - location : 1 - Poitiers
        - location : 2 - Nouveau Brunswick
        - location : 3 - La Biroire
        - location : 4 - L'Épine
        """
        self._test_all_combinations(
            "location",
            {
                1: {},
                2: {"collections": {1}, "items": {3}},
                3: {"collections": {2, 3}, "items": {1, 2}},
                4: {"collections": {4}, "items": {4}},
            },
        )

    def test_media_type(self):
        """
        - media type : 1 - cassette audio
        - media type : 2 - bande dat
        - media type : 3 - son uniquement
        """
        self._test_all_combinations(
            "media_type",
            {
                1: {},
                2: {"collections": {1, 2, 3}, "items": {1, 2, 3}},
                3: {"collections": {4}, "items": {4}},
            },
        )

    def test_recording_context(self):
        """
        - recording context : 1 - collectage
        - recording context : 2 - bal
        - recording context : 3 - enquête
        - recording context : 6 - TODO à créer dans les fixtures et nom à mettre ici
        """
        self._test_all_combinations(
            "recording_context",
            {
                1: {"collections": {2, 3}, "items": {1, 2}},
                2: {},
                3: {"collections": {1}, "items": {3}},
                6: {"collections": {4}, "items": {4}},
            },
        )

    def test_refrain(self):
        self._test_advanced_search(
            params="refrain=rose%20au%20bois",
            collections={},
            items={4},
        )

        # TODO critère unique : autres textes (cf incipit)

    def test_text(self):
        pass  # TODO critère unique : textes différents (cf incipit)

    def test_thematic(self):
        """
        - thématique : 1 - danse
        - thématique : 2 - récit
        """
        self._test_all_combinations(
            "thematic",
            {
                1: {"collections": {2, 4}, "items": {2, 4}},
                2: {"collections": {2}, "items": {1, 2}},
            },
        )

    def test_timbre(self):
        """
        - thématique : timbre_1
        - thématique : timbre_2
        """
        self._test_all_combinations(
            "timbre",
            {
                "timbre_1": {"collections": {2}, "items": {1, 2}},
                "timbre_2": {"collections": {4}, "items": {4}},
            },
        )

    def test_timbre_ref(self):
        """
        - thématique : timbre_ref_1
        - thématique : timbre_ref_2
        """
        self._test_all_combinations(
            "timbre_ref",
            {
                "timbre_ref_1": {"collections": {2}, "items": {1, 2}},
                "timbre_ref_2": {"collections": {4}, "items": {4}},
            },
        )

    def test_title(self):
        self._test_all_combinations(
            "title",
            {
                "Charles": {"collections": {2, 3}, "items": {2, 3}},
                "roi": {"collections": {2, 3}, "items": {4}},
                "violon": {"collections": {3}, "items": {1}},
                "rose": {"items": {4}},
            },
        )

    def test_usefulness(self):
        """
        - fonction : 1 - écouter
        - fonction : 2 - danser
        """
        self._test_all_combinations(
            "usefulness",
            {
                1: {"collections": {2, 4}, "items": {1, 4}},
                2: {"collections": {1, 2}, "items": {1, 3}},
            },
        )

    # ------------------------------------------------------------------------

    def test_multi_criteria(self):
        """
        - dance : 2 - valse
        - instrument : 2 - voix d'homme
        """
        self._test_advanced_search(
            params="dance=2&instrument=2",
            collections={2},
            items={2},
        )

        """
        - dance : 1 - polka
        - instrument : 2 - voix d'homme
        """
        self._test_advanced_search(
            params="dance=1&instrument=2",
            collections={2},
            items={2},
        )

        """
        - dance : 2 - valse
        - instrument : 1 - violon
        """
        self._test_advanced_search(
            params="dance=2&instrument=1",
            collections={},
            items={},
        )

        """
        - collector : 6 - Jeanne-Marie Bourreau
        - instrument : 1 - violon
        """
        self._test_advanced_search(
            params="collector=6&instrument=1",
            collections={3},
            items={},
        )

        """
        - coupe : 1 - AABB
        - instrument : 2 - voix d'homme
        """
        self._test_advanced_search(
            params="coupe=1&instrument=2",
            collections={2},
            items={2},
        )

        """
        - date : début et fin
        - domain_tale : 2 - récit
        """
        self._test_advanced_search(
            params="date_start=1969-09-01&date_end=1969-09-07&domain_tale=2",
            collections={2},
            items={1, 2},
        )

        """
        - code_internal : UPOI_ATP_0001_0001
        - text : empty value
        """
        self._test_advanced_search(
            params="code_internal=UPOI_ATP_0001_0001&text=",
            collections={2},
            items={1, 2},
        )
