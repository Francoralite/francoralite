# -*- coding: utf-8 -*-
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Luc LEGER / Coopérative ARTEFACTS <artefacts.lle@gmail.com>

from rest_framework import serializers

from django.contrib.auth.models import User


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('username', 'email', 'id')
        # fields = '__all__'
        fields = (
            'username',
            'first_name',
            'last_name',
            'is_active',
            'email',
            'is_superuser',
            'is_staff',
            'last_login',
            'password',
            'id',
            'date_joined',)
