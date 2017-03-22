from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from traffic import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="traffic/index.html")),
    url(r'^api/aadfs$', views.AADFList.as_view())
    # url(r'^api/(?P<pk>[0-9]+)/$', views.AADFDetails.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)