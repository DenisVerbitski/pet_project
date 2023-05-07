from django.urls import path, include  
from django.contrib import admin  
  
  
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('blog/', include('blog.urls', namespace='blog')), 
    path('user/', include('django.contrib.auth.urls')),
    path('user/', include('user.urls')), 
]