from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='account_login'),
    path('logout/', views.LogoutView.as_view(), name='account_logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.ProfileEditView.as_view(), name='profile_edit'),
    path('signup/', views.SignupView.as_view(), name='account_signup'),
    # path('cus_signup/', views.CusSignupView.as_view(), name='account_cus_signup'),
    # path('cus_login/', views.CusLoginView.as_view(), name='account_cus_login'),
]