from django.conf.urls import include, url
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

import notesserver.views

schema_view = get_schema_view(
   openapi.Info(
      title="Edx Notes API",
      default_version='v1',
      description="Edx Notes API docs",
   ),
   public=False,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    url(r'^heartbeat/$', notesserver.views.heartbeat, name='heartbeat'),
    url(r'^selftest/$', notesserver.views.selftest, name='selftest'),
    url(r'^robots.txt$', notesserver.views.robots, name='robots'),
    url(r'^$', notesserver.views.root, name='root'),
    url(r'^api/', include('notesapi.urls', namespace='api')),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
