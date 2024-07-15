from django.urls import path , include
from .views import NewsList , NewsDetail, UserDetail ,UserList
from rest_framework.authtoken.views import obtain_auth_token
#from api.views import RevokeToken
# from rest_framework_simplejwt import views as jwt_views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path("news/",NewsList.as_view(), name="list"),
    path("news/<int:pk>/",NewsDetail.as_view(), name="detail"),
    path("user/",UserList.as_view(), name="user-list"),
    path("user/<int:pk>/",UserDetail.as_view(), name="user-detail"),
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]
