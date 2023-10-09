from django.urls import path
from . import views

app_name='account'
urlpatterns = [
    path('login/',views.login_view,name="loginn"),
    path('signup/',views.profileregister,name="signup"),
    path('logout/',views.logout_view,name="logoutt"),
    path('profile/',views.profile_view,name="profile"),
    path('profileedit/',views.ProfileEdit,name='edit')

]