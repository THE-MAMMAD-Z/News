from django.urls import path
from . import views

app_name='account'
urlpatterns = [
    path('login/',views.login_view,name="login"),
    path('signup/',views.profileregister,name="signup"),
    path('logout/',views.logout_view,name="logout"),
    path('profile/',views.profile_view,name="profile"),
    path('profileedit/',views.ProfileEdit,name='edit'),


]