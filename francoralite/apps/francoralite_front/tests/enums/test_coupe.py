from enums_test import enums_test

tests = enums_test(
    entity = 'coupe',
    data = [
        {"id":"1", "name":"AABB", "notes":"AABB"},
    ],
    new_data = {"name":"AAB", "notes":"AAB"},
)


def test_coupe_list(francoralite_context):
    tests.list_test(context=francoralite_context)

    
def test_coupe_detail(francoralite_context):
    tests.details_test(context=francoralite_context)
    
    
def test_coupe_add(francoralite_context):
    tests.add_test(context=francoralite_context)
    
    
def test_coupe_update(francoralite_context):
    tests.update_test(context=francoralite_context)


def test_coupe_err_409(francoralite_context):
    tests.err_409_test(context=francoralite_context)
