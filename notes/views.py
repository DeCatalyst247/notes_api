from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
import requests


# Create your views here.
from rest_framework import viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    # FILTER configuration
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # allow exact filtering by fields via ?title=Hello or ?owner__username=rasaq
    filterset_fields = ['title', 'owner__username']
    # allow search across fields via ?search=keyword
    search_fields = ['title', 'content']
    # allow ordering via ?ordering=created_at or ?ordering=-updated_at
    ordering_fields = ['created_at', 'updated_at', 'title']
    # default ordering if not specified
    ordering = ['-updated_at']
    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

@api_view(['GET'])
def get_daily_quote(request):
    """
    Fetches a random inspirational quote from a third-party API
    and returns it as part of the response.
    """
    try:
        # Step 1: Make an HTTP request to a free public quote API
        response = requests.get("https://api.quotable.io/random")
        data = response.json()

        # Step 2: Extract the quote and author
        quote = data.get("content")
        author = data.get("author")

        # Step 3: Return it in DRF Response
        return Response({
            "quote": quote,
            "author": author,
            "message": "Here’s your daily inspiration 🌞"
        })

    except Exception as e:
        return Response({"error": str(e)}, status=500)   