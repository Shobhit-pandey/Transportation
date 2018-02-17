from django.conf.urls import url

from transport import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^list/', views.list, name='list'),
    url(r'^addtruck/', views.addtruck, name='addtruck'),
    url(r'^notification/', views.notification, name='notification'),
    url(r'^past-notification/', views.past_notification, name='past_notification'),
    url(r'^notification_insurance/(?P<pk1>[\w-]+)/$', views.notification_insurance_readed, name='notification_insurance_readed'),
    url(r'^notification_fitness/(?P<pk2>[\w-]+)/$', views.notification_fitness_readed, name='notification_fitness_readed'),
    url(r'^notification_pollution/(?P<pk3>[\w-]+)/$', views.notification_pollution_readed, name='notification_pollution_readed'),
]
