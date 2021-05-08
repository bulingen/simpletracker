from django.test import TestCase
from unittest import mock
from django.http.response import HttpResponse, FileResponse
from django.http.request import HttpRequest
from .views import track_get_image, COOKIE_NAME


DUMMY_REFERER = 'http://localhost:8000/test'
DUMMY_COOKIE = 'cookie value'


def create_request(referer=None, cookie=None):
    request = HttpRequest()
    request.META['HTTP_REFERER'] = referer
    request.COOKIES[COOKIE_NAME] = cookie
    return request


class PageviewTestCases(TestCase):
    def test__when_no_referer__should_not_set_cookie(self):
        request_without_referer = create_request()
        response = track_get_image(request_without_referer)
        actual = response.cookies.get(COOKIE_NAME)
        expected = None
        self.assertEqual(actual, expected)

    @mock.patch('simpletracker.views.log_pageview')
    def test__when_no_referer__should_not_log(self, log_pageview_mock):
        request_without_referer = create_request()
        track_get_image(request_without_referer)
        log_pageview_mock.assert_not_called()

    def test__when_referer_set__should_set_cookie(self):
        request_with_referer = create_request(referer=DUMMY_REFERER)
        response = track_get_image(request_with_referer)
        actual = response.cookies.get(COOKIE_NAME)
        not_expected = None
        self.assertNotEqual(actual, not_expected)

    @mock.patch('simpletracker.views.log_pageview')
    def test__when_referer_set__should_log(self, log_pageview_mock):
        request_with_referer = create_request(referer=DUMMY_REFERER)
        track_get_image(request_with_referer)
        log_pageview_mock.assert_called_once()

    def test__when_request_has_cookie__should_not_set_new(self):
        request_with_cookie = create_request(cookie=DUMMY_COOKIE)
        response = track_get_image(request_with_cookie)
        actual = response.cookies.get(COOKIE_NAME)
        expected = None
        self.assertEqual(actual, expected)
