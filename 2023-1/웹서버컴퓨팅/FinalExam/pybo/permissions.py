from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

from pybo.models import Question, Answer


class AuthorWritePermission(IsAuthenticated):
    def has_permission(self, request, view):
        # 사용자 권한에 대한 로직을 구현합니다.
        if request.method == "GET":
            return True
        elif request.method in ['POST','PUT', 'PATCH', 'DELETE']:
            return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        if request.method in ['POST', 'PUT', 'PATCH', "DELETE"]:
            return obj.author == request.user
        
