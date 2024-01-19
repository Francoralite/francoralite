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
        head = subprocess.Popen("git rev-parse HEAD", 
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        data["git_commit"] = head.stdout.readline().strip()

        # Python
        data["python"] = sys.version

        # Django
        data["django"] = django.VERSION

        return Response(data)