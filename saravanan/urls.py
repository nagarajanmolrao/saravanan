from django.conf.urls import url
import saravanan.views

urlpatterns = [
    url(r'^api/saravanan$', saravanan.views.saravanan_list),
    url(r'^api/saravanan/(?P<pk>[0-9]+)$', saravanan.views.saravanan_detail),
    url(r'^api/saravanan/activated$', saravanan.views.saravanan_list_activated)
]
