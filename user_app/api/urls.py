from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from user_app.api.views import registration_views, logout_views
#from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
urlpatterns = [
    path('login/', obtain_auth_token,name='login'),
    path('sign-up/', registration_views, name='registration-views'),
    path('logout/', logout_views, name='logout_views'),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]