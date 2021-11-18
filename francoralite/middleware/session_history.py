# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>


class SessionHistoryMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        session = request.session
        referer = request.META.get("HTTP_REFERER")
        
        if referer is None:
            return

        if "referers" not in session:
            session["referers"] = [referer]
        else:
            session["referers"] = [referer] + session["referers"]
        # Purge list
        session["referers"] = session["referers"][0:10]
