from django.urls import path
from.import views

urlpatterns=[
    path('',views.home,name='home'),
    path('create/',views.create,name='create'),
    path('followers/',views.followers_view,name='followers'),
    path('following/',views.following_view,name='following'),
    # path('chat/<str:username>',views.chat,name='chat'),
    path('about/',views.about,name='about'),
    path('search/',views.search,name='search'),
    path('like/<int:id>/',views.likee,name='like'),
    path('detail/<int:id>/',views.detail,name='detail'),
    path('update/<int:id>/',views.post_update,name='update'),
    path('delete/<int:id>/',views.post_delete,name='delete'),
    path('posts/<str:username>/',views.userposts,name='userposts'),
    path('profile/<str:username>/',views.view_profile,name='view_profile'),
    path('new_followers/<str:username>/',views.create_followers,name='create_follower'),
    path('comment/<int:id>/',views.create_comment,name='new_comment'),
    path('all_comment/<int:id>/',views.all_comments,name='all_comment'),
    path('delete/<int:id>/',views.delete,name='delete'),
]