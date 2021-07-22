import sys
import subprocess
import django
from rest_framework import views
from rest_framework.response import Response

import os


class VersionsView(views.APIView):

    def get(self, request, format=None):
        data = {}

        # Git
        try:
            head = subprocess.Popen("git rev-parse HEAD",
                shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            VERSION = head.stdout.readline().strip()
        except subprocess.CalledProcessError:
            VERSION = u'inconnu'
        data["git_commit"] = VERSION

        # Python
        data["python"] = sys.version

        # Django
        data["django"] = django.VERSION

        return Response(data)