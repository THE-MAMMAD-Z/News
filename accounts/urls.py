from django.urls import path
from . import views

app_name='account'
urlpatterns = [
    path('login/',views.login_view,name="loginn"),
    path('signup/',views.signup_view,name="signup"),
    path('logout/',views.logout_view,name="logoutt"),
    # path('profileRegister',views.profileregister,name="profileregister"),
    # path('profileedit/',views.ProfileEdit,name='profileedit')

]