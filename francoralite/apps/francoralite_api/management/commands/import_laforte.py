# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.core.management.base import BaseCommand
from django.db import Error
from django.utils.translation import gettext_lazy as _
from ...models.ref_laforte import RefLaforte
import csv


class Command(BaseCommand):
    help = _("Import data from LaForte")

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.cpt = 0

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_file",
            nargs=1,
            type=str,
            help="CSV LaForte file to be import in database",
        )

    def handle(self, *args, **options):
        with open(options["csv_file"][0], "r") as file:
            reader = csv.DictReader(file, delimiter="\t")
            for row in reader:
                RefLaforte.objects.get_or_create(
                    number=row["tome"] + "." + row["numéro"],
                    defaults={"name": row["description"]},
                )
        self.cpt = RefLaforte.objects.all().count()
        self.stdout.write("Imported %s RefLaforte" % self.cpt)
