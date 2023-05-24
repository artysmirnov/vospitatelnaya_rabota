from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>', views.EventDetailView.as_view(), name='event-detail')
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
