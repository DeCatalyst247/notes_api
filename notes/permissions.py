# notes/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission: 
    - Anyone can read (GET, HEAD, OPTIONS)
    - Only the owner can edit or delete
    """

    def has_object_permission(self, request, view, obj):
        # Allow read-only requests for everyone
        if request.method in SAFE_METHODS:
            return True
        
        # Only allow edits/deletes for the owner
        return obj.owner== request.user