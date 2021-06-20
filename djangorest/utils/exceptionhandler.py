from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    handlers = {
        'NotFound': _handle_invalidparam,
        'ParseError': _handle_invalidstatus,
    }

    response = exception_handler(exc, context)

    if response:
        response.data['status_code'] = response.status_code

    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)

    return response

def _handle_invalidstatus(exc, context, response):  
    return response

def _handle_invalidparam(exc, context, response):
    return response