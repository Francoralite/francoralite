# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


class SessionHistoryMiddleware(object):

    def process_view(self, request, view_func, view_args, view_kwargs):
        session = request.session
        referer = request.META.get("HTTP_REFERER")

        if "referers" not in session:
            session["referers"] = [referer]
        else:
            session["referers"] = [referer] + session["referers"]
        # Purge list
        session["referers"] = session["referers"][0:10]
