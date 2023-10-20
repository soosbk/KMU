from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import api_views


urlpatterns = [
    path('questions/', api_views.QuestionAPIView.as_view()),
    path('questions/<int:question_id>/', api_views.QuestionAPIView2.as_view()),
    path('answers/', api_views.AnswerAPIView.as_view()),
    path('answers/<int:answer_id>/',
         api_views.AnswerAPIView2.as_view()),
]

