#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # Add the project to the python path
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'project'))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
