from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission control
    """
    def has_object_permission(self, request, view, obj):
        """
        Returns `True` if method is safe
        :param request: request object
        :param view: view object
        :param obj:
        :return: is request_method safe?
        """
        if request.method in permissions.SAFE_METHODS:
            return True
