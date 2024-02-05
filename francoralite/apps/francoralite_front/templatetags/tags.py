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

# --- GIT Label---
# Use Popen for running git commands and capturing output
# Get the latest commit hash that was tagged
try:
    head = subprocess.Popen(
        "git rev-list --tags --max-count=1",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        encoding="utf-8",
    )
    latest_tagged_commit = head.stdout.readline().strip()
except:
    latest_tagged_commit = ""


try:
    head = subprocess.Popen(
        f"git tag --list",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        encoding="utf-8",
    )
    last_tag = head.stdout.readlines()[-1].strip()
except:
    last_tag = ""

try:
    head = subprocess.Popen(
        "git show -s --format=%ai",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        encoding="utf-8",
    )
    last_tag_date = head.stdout.readline().strip()[:10]
except:
    last_tag_date = ""


# Print the tag and its date
LABEL = last_tag
LABEL_DATE = last_tag_date


hostname = os.getenv("HOSTNAME")


@register.simple_tag()
def git_short_version():
    return VERSION


@register.simple_tag()
def git_label():
    return f"{LABEL} ({LABEL_DATE})"


@register.simple_tag()
def host_name():
    return hostname
