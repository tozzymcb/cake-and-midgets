"""
WSGI config for pub project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys
import site

STAGE=False
if STAGE:
    vepath = '/home/chris/virtualenvs/cake/lib/python2.6/site-packages'
else:
    vepath = '/home/chris/virtualenvs/cake/lib/python2.6/site-packages'
prev_sys_path = list(sys.path)
# add the site-packages of our virtualenv as a site dir
site.addsitedir(vepath)

os.environ['PYTHON_EGG_CACHE'] = '/home/chris/public_html/cake-and-midgets/apache/egg-cache'
# add the app's directory to the PYTHONPATH
sys.path.append('/home/chris/public_html/cake-and-midgets/')
# reorder sys.path so new directories from the addsitedir show up first
new_sys_path = [p for p in sys.path if p not in prev_sys_path]
for item in new_sys_path:
    sys.path.remove(item)
sys.path[:0] = new_sys_path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cakeandmidgets.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
