from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    მხოლოდ ტანსაცმლის შემქმნელს ვაძლევთ მისი მონაცემების შეცვლის უფლებას.
    """

    def has_object_permission(self, request, view, obj):
        # ვამოწმებთ არის თუ არა request-ის მეთოდი უსაფრთხო, ანუ უბრალოდ
        # წაკითხვის უფლება ნებისმიერ მომხმარებელს უნდა ჰქონდეს
        if request.method in permissions.SAFE_METHODS:
            return True

        # მონაცემების შეცვლა მხოლოდ მის შემქმნელს უნდა შეეძლოს
        return obj.designer == request.user
