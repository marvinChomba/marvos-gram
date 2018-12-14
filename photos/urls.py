from django.conf.urls import url
from django.conf.urls.static import static
from djanfo.conf import settings

urlpatterns = []

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)