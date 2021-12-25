from rest_framework.serializers import ValidationError
from rest_framework import status
# def custom_exception_handler(exc,context):
#     handlers={
#         'ValidationError':_handle_generic_error,
#         'Http404':_handle_generic_error,
#         'PermissionDenied':_handle_generic_error,
#         #'NotAuthenticated':_handle_authentication_error,
#         'DoesnotExist':_handle_generic_error
#     }
#     reponse= exception_handler(exc,context)
#     exception_class=exc.__class__.__name__
#     if exception_class in handlers:
#         return handlers[exception_class](exc, context, response)
#     return response

# def _handle_generic_error(exc, context, response):
#     return response




class CustomAPIException(ValidationError):
    """
    raises API exceptions with custom messages and custom status codes
    """

    default_code = 'error'

    def __init__(self, detail, status_code=None):
        self.detail = detail
        if status_code is not None:
            self.status_code = status_code