from django.conf import settings
from rest_framework import exceptions
from rest_framework.authentication import CSRFCheck, TokenAuthentication


class CookieTokenAuthentication(TokenAuthentication):
    def authenticate(self, request):
        header_authentication = super().authenticate(request)

        if header_authentication is not None:
            return header_authentication

        token = request.COOKIES.get(settings.AUTH_TOKEN_COOKIE_NAME)

        if not token:
            return None

        self.enforce_csrf(request)

        return self.authenticate_credentials(token)

    def enforce_csrf(self, request):
        csrf_check = CSRFCheck(lambda request: None)
        csrf_check.process_request(request)
        failure_reason = csrf_check.process_view(request, None, (), {})

        if failure_reason:
            raise exceptions.PermissionDenied(f"CSRF Failed: {failure_reason}")