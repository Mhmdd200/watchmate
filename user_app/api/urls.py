from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from user_app.api.views import registration_views
urlpatterns = [
    path('login/', obtain_auth_token,name='login'),
    path('sign-up/', registration_views, name='registration-views')
]