from django.contrib.auth.models import User
from django.core.cache import cache
from rest_framework.permissions import BasePermission

from app.utils import get_session


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        session = get_session(request)

        try:
            user_id = cache.get(session)
            user = User.objects.get(pk=user_id)
        except:
            return False

        return user.is_active


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        session = get_session(request)

        if session is None or session not in cache:
            return False

        try:
            user_id = cache.get(session)
            user = User.objects.get(pk=user_id)
        except:
            return False

        return user.is_superuser
