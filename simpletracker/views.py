from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.utils.crypto import get_random_string
from urllib.parse import urlparse


COOKIE_NAME = 'visitor_id'
COOKIE_AGE = 3600 * 24 * 365


def create_visitor_id():
    return get_random_string(length=5, allowed_chars=u'abcdefghijklmnopqrstuvwxyz0123456789')


def get_page_from_url(url):
    parsed_url = urlparse(url)
    page = parsed_url.path

    if parsed_url.query:
        page += '?' + parsed_url.query

    return page


def log_pageview(page, visitor_id):
    now = datetime.utcnow().replace(microsecond=0)
    timestamp_string = "{}UTC".format(now)
    print(timestamp_string, page, visitor_id)


def contact(request):
    return render(request, "contact.html")


def track_get_image(request):
    image_data = open("images/transparent.gif", "rb").read()
    response = HttpResponse(image_data, content_type="image/gif")

    referer = request.META.get('HTTP_REFERER')

    if not referer:
        return response

    visitor_id = request.COOKIES.get(COOKIE_NAME)

    if not visitor_id:
        visitor_id = create_visitor_id()
        response.set_cookie(COOKIE_NAME, value=visitor_id, max_age=COOKIE_AGE)

    page = get_page_from_url(referer)

    log_pageview(page, visitor_id)

    return response
