
def test_view_err500(request):
    """
    A function to handle the request and perform some operation that may raise an error 500.
    """
    return 42/0
