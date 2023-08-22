
from django.contrib import admin
from django.urls import path, include
from skladik.views import custom_404_view
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('skladik.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]

handler404 = custom_404_view
handler500 = 'skladik.views.error_500'
if settings.DEBUG:
 urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
