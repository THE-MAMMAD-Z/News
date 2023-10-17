from django.urls import path , include
from .views import ArticleList , ArticleListtest , ArticleDetail, UserDetail ,UserList
from rest_framework.authtoken.views import obtain_auth_token
#from api.views import RevokeToken
# from rest_framework_simplejwt import views as jwt_views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path("test/",ArticleListtest.as_view(), name="test"),
    path("",ArticleList.as_view(), name="list"),
    path("<int:pk>/",ArticleDetail.as_view(), name="detail"),
    path("user/",UserList.as_view(), name="user-list"),
    path("user/<int:pk>/",UserDetail.as_view(), name="user-detail"),
    # path("api-token/",obtain_auth_token , name="generate_auth_token"),
    # path("api/revoke/",RevokeToken.as_view())
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    #path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]
