from django.urls import path
from . import views

urlpatterns = [path('', views.PostListView.as_view()),
               path('<int:pk>/', views.PostDetail.as_view()),
               path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments'),
               path('register/', views.register, name='register'),
               path('login/', views.login, name='login'),
               path('logout/', views.logout, name='logout'),
]