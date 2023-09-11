from django.urls import path
from core import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('Login/',views.Login,name='Login'),
    path('Logout/',views.Logout,name='Logout'),
    path('setting/',views.setting,name='setting'),
    path('Profile1/',views.Profile1,name='Profile1'),
    
    
    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)