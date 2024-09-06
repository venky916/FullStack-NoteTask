from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

@api_view(['GET', 'POST'])
def notes(request):
    if request.method == 'GET':
        title_substring = request.GET.get('title', None)
        if title_substring:
            notes = Note.objects.filter(title__icontains=title_substring)
        else:
            notes = Note.objects.all()
        
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH'])
def note_detail(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return Response({'error': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Fetch the note by ID
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        # Update the note by ID
        partial = request.method == 'PATCH'  # Allow partial update only for PATCH requests
        serializer = NoteSerializer(note, data=request.data, partial=partial)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
