from rest_framework import permissions


class IsOwnerOrReadOnlyAndCreate(permissions.BasePermission):
    """Права на обновление и удаление только владельцу"""

    def has_object_permission(self, request, view, obj):
        if request.method in (*permissions.SAFE_METHODS, "CREATE"):
            return True

        return obj.owner == request.user
