# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from django.utils.translation import gettext_lazy as _

from francoralite.apps.francoralite_front import tools


class ProportionalColoredBarLoader(object):
    url_pattern = NotImplemented
    attribute_name = NotImplemented
    available_values = NotImplemented

    def __init__(self, url_pattern=None):
        if url_pattern:
            self.url_pattern = url_pattern

    def complete(self, item):
        url = self.url_pattern.format(**item)
        api_response = tools.request_api(url)

        total_count = float(sum(api_response.values())) if api_response else 0

        item[self.attribute_name] = colored_bar = []

        for code, color, label in self.available_values:
            count = api_response.get(code, 0)
            if count <= 0:
                continue

            ratio = (count / total_count) if total_count else 0

            colored_bar.append({
                'label': label,
                'color': color,
                'count': count,
                'ratio': ratio,
                'percent': ratio * 100,
            })


class DomainsBarLoader(ProportionalColoredBarLoader):
    attribute_name = 'domains'
    available_values = (
        ('T', '#636EF4', _('Témoignage')),
        ('C', '#EF553B', _('Chanson')),
        ('A', '#00CC96', _('Autre expression vocale')),
        ('I', '#AB63FA', _('Expression instrumentale')),
        ('R', '#FFA15A', _('Conte ou récit légendaire')),
    )
