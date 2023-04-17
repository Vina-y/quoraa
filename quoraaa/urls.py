from quoraaa import views
from django.urls import path

urlpatterns=[
    path('',views.render_login,name='render_login'),
    path('perform_login',views.perform_login,name='perform_login'),
    path('dashboard_page/',views.perform_login,name='dashboard_page'),
    path('register/',views.register_page,name='register'),
    path('perform_registration/',views.perform_registration,name='perform_registration'),
    path('post_question/',views.post_question,name='post_question'),
    path('post_answer/<int:id>',views.post_answer,name='post_answer'),
    path('view_answer/<int:id>',views.view_answer,name='view_answer'),
    path('like_answer/<int:id>/<str:st>',views.like_answer,name='like_answer'),
    path('logout_view/',views.logout_view,name='logout_view'),
    path('home/',views.home,name='home'),

]