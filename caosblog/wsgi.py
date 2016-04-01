from django.core.wsgi import get_wsgi_application
from socket import gethostname

import os
import sys

sys.path.insert(0, os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2]))

# cpl == Core Services Managed, Production, Linux.
if(gethostname()[:3]) == 'cpl':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "caosblog.settings.production")
# csl == Core Services Managed, Staging, Linux.
elif(gethostname()[:3]) == 'csl':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "caosblog.settings.stage")
# else use dev settings.
# cdl == Core Services Managed, Development, Linux. vag == Vagrant.
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "caosblog.settings.dev")

application = get_wsgi_application()
