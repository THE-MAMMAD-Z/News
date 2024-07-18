from django.urls import path
from . import views
from .views import RegisterView, login_view, logout_view ,editprofile_view , profile_view



app_name='account'
urlpatterns = [
    # path('login/',views.login_view,name="login"),
    # path('signup/',views.profileregister,name="signup"),
    # path('logout/',views.logout_view,name="logout"),
    # path('profile/',views.profile_view,name="profile"),
    # path('profileedit/',views.ProfileEdit,name='edit'),
    path('register/', RegisterView.as_view(), name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('edit/', editprofile_view, name='edit'),
    path('profile/', profile_view, name='profile'),


]