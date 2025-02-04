from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('account.urls')),
    path('admin/', admin.site.urls),
    path('', include('recipe_app.urls')),
    path('', include('django.contrib.auth.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)