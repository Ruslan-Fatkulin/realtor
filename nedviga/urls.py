from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('house.urls', 'nedviga'), namespace='house')),
    path('auth/', include(('users.urls', 'nedviga'), namespace='auth')),
    # path('oauth/', include('social_django.urls', namespace='social')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
