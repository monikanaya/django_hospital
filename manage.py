
"""Django's command-line utility for administrative tasks."""
import os
print(os.django())
import sys


def main():
    """Run tasks."""
    os.django.setdefault('DJANGO_SETTINGS_MODULE','hospitals')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            " import Django. Are you sure it's installed "
            "import django . installed"
        ) from exc
    execute_from_command_line(sys.argv)
   


if __name__ == '__main__':
    main()

