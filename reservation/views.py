from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets,generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer,BookingSerializer,MenuItemSerializer
from .models import Booking,MenuItem
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated users

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = [IsAuthenticated]  # Restrict access to authenticated users

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]  # Require authentication
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "This view is protected"})