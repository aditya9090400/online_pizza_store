from django.urls import path
from authentication.views import UserCreationView

urlpatterns = [
    path('signup/', UserCreationView.as_view(), name='sign_up'),
]
