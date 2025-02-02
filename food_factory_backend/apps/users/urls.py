from django.urls import path
from .views import UserInsertView

urlpatterns = [
    path('insert/', UserInsertView.as_view(), name='user-insert'),
]
