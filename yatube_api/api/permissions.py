from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

    # в случае если делаю так(или вообще убираю has_object_permission):
    # def has_object_permission(self, request, view, obj):
    #     return obj.author == request.user
    # то тесты сыпятся, не понимаю как исправить или что-то надо добавить во вьюсеты,
    # уже всяко пробовал
