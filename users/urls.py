from django.urls import path
from.import views

urlpatterns=[
    path('register/',views.register,name='register'),
    path('export_to_csv/',views.export_to_csv,name='export_to_csv'),
    path('login/',views.logins,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profiles,name='profile'),

]