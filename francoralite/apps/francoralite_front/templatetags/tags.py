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
get_latest_tagged_commit = ["git", "rev-list", "--tags", "--max-count=1"]
latest_tagged_commit = (
    subprocess.check_output(get_latest_tagged_commit).decode().strip()
)

with subprocess.Popen(
    [
        "git",
        "describe",
        "--tags",
        latest_tagged_commit,
        "--abbrev=0",
    ],
    stdout=subprocess.PIPE,
) as proc:
    last_tag = proc.stdout.read().decode().strip()

with subprocess.Popen(
    ["git", "show", "-s", "--format=%ai"], stdout=subprocess.PIPE
) as proc:
    last_tag_date = proc.stdout.read().strip().decode()[:10]

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
