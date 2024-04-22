from enums_test import EnumsTest


class TestCulturalArea(EnumsTest):
    second_text_field = 'geojson'
    second_text_value = '{"foo": "bar", "spam": 42}'
    clear_fields_on_add = True
    entity = 'cultural_area'
    title = 'Aires culturelles'
    data = [
        {"id":"1", "name":"Poitou", "geojson":'{"type": "Polygon", '
            '"coordinates": [[[1.021729, 46.562637], [0.587769, 46.984], '
            '[-0.22522, 47.06638], [-2.312622, 47.017716], '
            '[-1.653442, 46.327965], ...'},
        {"id":"2", "name":"Saintonge, Poitou", "geojson":"null"},
        {"id":"3", "name":"Vendée", "geojson":"null"},
    ]
    new_data = {"name":"Québec", "geojson":'{"key": "value", "number": 42}'}

