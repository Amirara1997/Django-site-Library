
from django.contrib import admin
from django.urls import path, include
from hunter import views
from django.conf import settings
from django.conf.urls.static import static
from buyer import views2
from buyer import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('',views.home2, name='home2'),
    path('accounts/', include('accounts.urls')),
    path('hunter/', include('hunter.urls')),
    path('buyer/', include('buyer.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
