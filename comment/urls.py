from django.urls import path
from . import views

urlpatterns = [
    path('comment/add/news/<int:pk>/' , views.news_cm_add , name = 'news_cm_add'),
    path('comment/list/' , views.comments_list , name = 'comments_list'),
    path('comment/del/<int:pk>/' , views.comments_del , name = 'comments_del'),
    path('comment/confirme/<int:pk>/' , views.comments_confirme , name = 'comments_confirme'),
]
