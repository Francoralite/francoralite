from enums_test import EnumsTest


class TestCivility(EnumsTest):
    second_text_field = 'geojson'
    second_text_value = '{"foo": "bar", "spam": 42}'
    clear_fields_on_add = True
    entity = 'cultural_area'
    title = 'Aires culturelles'
    data = [
        {"id":"1", "name":"Poitou", "geojson":"null"},
        {"id":"2", "name":"Saintonge, Poitou", "geojson":"null"},
        {"id":"3", "name":"Vendée", "geojson":"null"},
    ]
    new_data = {"name":"Québec", "geojson":'{"key": "value", "number": 42}'}
