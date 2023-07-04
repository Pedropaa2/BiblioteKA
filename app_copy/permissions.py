from rest_framework.permissions import BasePermission
from rest_framework import permissions
from rest_framework.views import Request, View

class AssociateOnlyPermission(permissions.BasePermission):
  def has_permission(self, request: Request, view: View) -> bool:
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.associate
        )


