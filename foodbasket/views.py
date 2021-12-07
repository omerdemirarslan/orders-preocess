from django.http import HttpResponse

from .helpers.messages import HOME_PAGE


def home_page_view(request):
    """
    This Function Return HTTP Response and Method Contaion Simple Explain For Foodbasket Requests
    :param request:
    :return:
    """
    return HttpResponse(HOME_PAGE, content_type='text/plain')
