from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reviews.urls')),
    path('accounts/', include('allauth.urls')),
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# admin
admin.site.site_header = 'Phone Review Admin'
admin.site.site_title = 'Phone Reviews Admin Portal'
admin.site.index_title = 'Welcome to Phone Reviews Admin Portal'
