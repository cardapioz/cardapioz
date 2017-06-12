#!/usr/bin/env python3.6
#
#
#   SE O MUP PODE CONCORRER COM O UBER
#   A GENTE PODE CORRER COM IFOOD
#
#   MAS MAURICIO EUGÊNIO A GENTE NÃO PODE DIZER ISSO
#
#   ENTÃO COLOCA ASSIM: O MUNDO DOS NEGOCIOS POSSUI ESPAÇO PARA TODOS.
#
#

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cardapioz.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
