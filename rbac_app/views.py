from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, status

from .forms import RegisterForm
from .models import User, Resource
from .serializers import UserSerializer, RegisterSerializer, ResourceSerializer
from .permissions import IsAdminOrModerator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Register View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# Get User Info
class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

# Resource Views (Admin or Moderator Access)
class ResourceListCreateView(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAdminOrModerator]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

@login_required
def dashboard(request):
    # Get the role of the current logged-in user
    user_role = request.user.role

    # Query resources created by users with the same role as the logged-in user
    resources = Resource.objects.filter(created_by__role=user_role)

    return render(request, 'rbac_app/dashboard.html', {'resources': resources})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = RegisterForm()
    return render(request, 'rbac_app/register.html', {'form': form})