from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from movies.views import HomepageView, ResultsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', HomepageView.as_view(), name='homepage'),
    path('movies/results/', ResultsView.as_view(), name='results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)