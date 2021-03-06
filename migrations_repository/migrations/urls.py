from django.conf.urls import url
from .import views

app_name = 'migrations'

urlpatterns =[

    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<plan_id>[0-9]+)/$', views.detail, name='detail') ,
    url(r'^create_plan/$', views.create_plan, name='create_plan'),
    url(r'^(?P<plan_id>[0-9]+)/create_circuit/$', views.create_circuit, name='create_circuit'),
]
