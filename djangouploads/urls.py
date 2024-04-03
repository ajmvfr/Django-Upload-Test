
from django.contrib import admin
from django.urls import path
from djangouploads import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/<int:movie_id>', views.movie, name='movie'),
    path('movies/upload',views.upload, name='upload'),
    path('', views.home, name='home')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
