from rest_framework import status, permissions

class IsOwnerOrIsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            message = "로그인한 유저만 접근 가능합니다. 로그인해주세요 "
            raise Exception(status_code=status.HTTP_401_UNAUTHORIZED, detail=message)
        return bool(request.user and request.user.is_authenticated)
        
    def has_object_permission(self, request, view, obj): # 수정권한
        return bool((obj.user == request.user) or request.user.is_staff)