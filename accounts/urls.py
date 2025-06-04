from django.urls import path, include

from . import views

app_name = 'accounts'

urlpatterns = [
    path( 'sign_up/', views.sign_up, name='sign_up' ),
    path( 'profile/', views.profile, name='profile' ),
    path( 'edit/', views.profile_edit, name='profile_edit' ),

]
