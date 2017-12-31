from django.conf.urls import url
from . import views

app_name = 'jobs'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/(?P<username>\w+)/$', views.user_profile, name='user_profile'),
    url(r'^offers/$', views.job_offers, name='job_offers'),
    url(r'offers/add/$', views.job_offer_add, name='job_offer_add'),
    url(r'offers/(?P<offer_id>[0-9]+)/$', views.offer_detail, name='offer_detail'),
    url(r'offers/(?P<offer_id>[0-9]+)/apply/$', views.job_apply, name='job_apply'),
    url(r'^users/(?P<username>\w+)/$', views.user_profile, name='user_profile'),
    url(r'^users/(?P<username>\w+)/applications', views.user_applications, name='user_applications'),
    url(r'^users/(?P<username>\w+)/offers', views.user_offers, name='user_offers'),
    url(r'^users/(?P<username>\w+)/candidates', views.candidates, name='candidates'),
    url(r'applications/(?P<application_id>[0-9]+)/$', views.application_detail, name='application_detail'),
]