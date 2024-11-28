from rest_framework.permissions import BasePermission

class IsAdminOrModerator(BasePermission):
    """
    Custom permission to allow only Admins and Moderators to access.
    """
    def has_permission(self, request, view):
        return request.user.role in ['Admin', 'Moderator']
