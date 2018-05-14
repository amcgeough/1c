from django.urls import path

from . import views


# app_name = 'questions'
# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]


# API Endpoint
urlpatterns = [
    path('', views.ListTodo.as_view()),
    path('choice', views.ListTodo2.as_view()),
    path('<int:pk>/', views.DetailTodo.as_view()),
]
