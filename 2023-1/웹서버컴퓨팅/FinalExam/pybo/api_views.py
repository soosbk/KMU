from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .permissions import AuthorWritePermission
from .serializers import QuestionSerializer, AnswerSerializer
from .models import Question, Answer


class QuestionAPIView(APIView):
    def get(self, request):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(data=serializer.data)
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            serializer = QuestionSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save(author=request.user)
                return Response(data=serializer.data)




class QuestionAPIView2(APIView):
    def get_object(self, question_id):
        return get_object_or_404(Question, id=question_id)

    def get(self, request, question_id):
        question = self.get_object(question_id)

        serializer = QuestionSerializer(question)
        return Response(data=serializer.data)

    def put(self, request, question_id):
        question = self.get_object(question_id)

        # Authentication
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        # Permission
        elif question.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        serializer = QuestionSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save(author=request.user)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, question_id):
        question = self.get_object(question_id)

        # Authentication
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        # Permission
        elif question.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AnswerAPIView(APIView):
    def get(self, request):
        queryset = Answer.objects.all()
        serializer = AnswerSerializer(queryset, many=True)
        return Response(data=serializer.data)
    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            serializer = AnswerSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save(author=request.user)
                return Response(data=serializer.data)


class AnswerAPIView2(APIView):
    def get_object(self, answer_id):
        return get_object_or_404(Answer, id=answer_id)

    def get(self, request, answer_id):
        answer = self.get_object(answer_id)
        serializer = AnswerSerializer(answer)
        return Response(data=serializer.data)

    def put(self, request, answer_id):
        answer = self.get_object(answer_id)

        # Authentication
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        # Permission
        elif answer.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = AnswerSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save(author=request.user)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, answer_id):
        answer = self.get_object(answer_id)

        # Authentication
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        # Permission
        elif answer.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

