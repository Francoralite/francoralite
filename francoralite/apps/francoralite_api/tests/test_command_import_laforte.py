# Assuming the integration test file is in the same directory as the code snippet provided
# You can create an integration test with Pytest by creating a new file, for example test_ref_laforte_integration.py, and adding the following code:

# test_ref_laforte_integration.py

import pytest
from django.core.management import call_command
from io import StringIO
from ..models.ref_laforte import RefLaforte

@pytest.mark.django_db
def test_ref_laforte_integration():
    out = StringIO()
    call_command("import_laforte", "./francoralite/apps/francoralite_api/tests/fake_data/test_laforte.csv", stdout=out)
    assert "Imported 4 RefLaforte" in out.getvalue()
