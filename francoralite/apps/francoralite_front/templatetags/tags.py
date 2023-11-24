import subprocess
import os
from django.template import Library

register = Library()

try:
    head = subprocess.Popen(
        "git rev-parse --short HEAD",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        encoding="utf-8",
    )
    VERSION = head.stdout.readline().strip()
except:
    VERSION = "inconnu"

hostname = os.getenv('HOSTNAME')



@register.simple_tag()
def git_short_version():
    return VERSION


@register.simple_tag()
def host_name():
    return hostname