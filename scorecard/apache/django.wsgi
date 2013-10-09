import os
import sys

activate_this = '/opt/digitalscorecard/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

paths = ['/var/www/digitalscorecard'] #['/var/www/digitalscorecard/scorecard', '/var/www/digitalscorecard']

for path in paths:
        if path not in sys.path:
                sys.path.append(path)

import django.core.handlers.wsgi
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = django.core.handlers.wsgi.WSGIHandler()
