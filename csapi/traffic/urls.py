from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from traffic import views

urlpatterns = [
    url(r'^aadfs$', views.AADFList.as_view()),
    #url(r'^api/aadfs$', views.AADFList.as_view()),
    # url(r'^api/(?P<pk>[0-9]+)/$', views.AADFDetails.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)