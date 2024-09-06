from django.urls import path
from .views import notes,note_detail

urlpatterns = [
    path('notes', notes, name='notes'),  # Handles GET and POST
    path('notes/<int:pk>/', note_detail, name='note_detail'),  # Handles both GET and PUT
]
