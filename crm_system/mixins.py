from django.contrib import messages
from django.db.models import ProtectedError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect


class ProtectedDeleteMixin:
    """Не даёт удалить объект, на который есть ссылки, без падения в 500."""

    def post(self, request: HttpRequest, *args: object, **kwargs: object) -> HttpResponse:
        """Удаляет объект, перехватывая ProtectedError при наличии ссылок."""
        try:
            return super().post(request, *args, **kwargs)  # type: ignore[misc]
        except ProtectedError:
            messages.error(
                request,
                "Нельзя удалить запись: на неё ссылаются другие данные.",
            )
            return redirect(self.success_url)  # type: ignore[attr-defined]
