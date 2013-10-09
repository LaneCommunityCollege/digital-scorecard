from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('scorecard.views',
    url(r'^$', 'index'),
    url(r'^(?P<themeid>\d+)$', 'theme'),
    url(r'^(?P<themeid>\d+)/(?P<objectiveid>\d+)/(?P<outcomeid>\d+)$', 'outcome'),
    url(r'^(?P<pageurl>[\w\s_-]+)$', 'staticpage'),
)
