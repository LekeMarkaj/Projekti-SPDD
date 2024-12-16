from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from django.contrib.auth import logout

from core.views import index, about
from userprofile.views import signup, custom_logout

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),

    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),

    path('dashboard/', include('dashboard.urls')),

    path('dashboard/leads', include('lead.urls')),

    path('admin/', admin.site.urls),
]
