# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers


class SimpleSerializer(serializers.Serializer):

    def to_representation(self, instance):
        if isinstance(instance, str):
            return instance
        else:
            raise Exception('Unknown instance type: %s' % type(instance))
