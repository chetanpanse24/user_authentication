from django.urls import path, include
from .views import signup, index, update_profile

app ="loginapp"
urlpatterns = [
    path('', index, name = "index"),
    path('signup/', signup, name = "signup"),
    path('update_profile/', update_profile, name = "update_profile" ),
    path('accounts/', include('django.contrib.auth.urls')),
    
]