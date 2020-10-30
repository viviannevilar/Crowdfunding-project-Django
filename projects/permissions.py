from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsOwnerDraft(permissions.BasePermission):
    """
    everyone can see published projects (safe method)
    non authors cannot see or change drafts (not pub).
    authors can see and change drafts, cannot change published projects.

    author      pub         safe            True
    author      pub         not safe        False   
    author      not pub     safe            True
    author      not pub     not safe        True
    not author  pub         safe            True
    not author  pub         not safe        False
    not author  not pub     safe            False
    not author  not pub     not safe        False
    """

    def has_object_permission(self, request, view, obj):
        if (obj.pub_date != None) and (request.method in permissions.SAFE_METHODS):
            return True
        elif (obj.pub_date == None):
            if obj.owner == request.user:
                return True
            message = 'This project has not been published yet. Only owners can see draft projects.'
            return False
        message = 'Published projects cannot be changed.'
        return False


 