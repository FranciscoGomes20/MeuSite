from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import decorator_from_middleware
from django.middleware.csrf import CsrfViewMiddleware


VERSION = (0, 1, 0)
__version__ = '.'.join(map(str, VERSION))


class CsrfProtectFormMiddleware(CsrfViewMiddleware):
    def __init__(self, get_response=None):
        self.CSRF_PROTECT_FORM_CONTENT_TYPE = getattr(settings, 'CSRF_PROTECT_FORM_CONTENT_TYPE', ['application/x-www-form-urlencoded', 'multipart/form-data', 'text/plain'])
        super(CsrfProtectFormMiddleware, self).__init__(get_response)

    def process_request(self, request):
        if request.content_type not in self.CSRF_PROTECT_FORM_CONTENT_TYPE:
            request.csrf_processing_done = True
        super(CsrfProtectFormMiddleware, self).process_request(request)

    def process_response(self, request, response):
        if getattr(response, 'csrf_cookie_set', False) and response['Content-Type'] not in self.CSRF_PROTECT_FORM_CONTENT_TYPE:
            response.cookies.pop(settings.CSRF_COOKIE_NAME)
        return response


def csrf_protect_form(view):
    view = decorator_from_middleware(CsrfProtectFormMiddleware)(view)
    view = csrf_exempt(view)
    return view
