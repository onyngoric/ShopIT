from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('view', views.view, name='view'),
    path('details',views.details,name='details'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('home', views.home2, name='index'),    
    path('post', views.post,name='postad'),
    path('active_post', views.activepost, name='active_post'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)