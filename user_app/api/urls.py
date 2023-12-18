from django.urls import path, include
# from user_app.api.views import user_list, user_details
from user_app.api.views import UserList, UserDetails

urlpatterns = [
    path('list/', UserList.as_view(), name='users-list'),
    path('<int:pk>/', UserDetails.as_view(), name='user-details'),
]