from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from user_app.models import User
from .serializers import UserSerializer
from rest_framework.views import APIView


class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class UserDetails(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'Error': 'User is not found !!!'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# or

# # Create your views here.
# @api_view(['GET', 'POST'])
# def user_list(request):
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def user_details(request, pk):
#     if request.method == 'GET':
#         try:
#             user = User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return Response({'Error': 'User is not found !!!'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#
#     if request.method == 'PUT':
#         user = User.objects.get(pk=pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == 'DELETE':
#         user = User.objects.get(pk=pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
