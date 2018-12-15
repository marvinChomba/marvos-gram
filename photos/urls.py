from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r"^$", views.index, name = 'index'),
    url(r"^ajax/like/$",views.like, name = 'like'),
    url(r"^ajax/comment/$",views.comment, name = "comment"),
    url(r"^ajax/follow/$", views.follow, name = "follow"),
    url(r"^add/image$", views.add_image, name = "add_image")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)