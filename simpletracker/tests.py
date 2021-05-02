from django.test import TestCase
from unittest import mock
from django.http.response import HttpResponse, FileResponse
from django.http.request import HttpRequest
from .views import track_get_image, log_pageview, COOKIE_NAME


def create_request_with_referer():
    request = HttpRequest()
    request.META['HTTP_REFERER'] = 'http://localhost:8000/test'
    return request


class PageviewTestCases(TestCase):
    def test__when_no_referer__should_not_set_cookie(self):
        request_without_referer = HttpRequest()
        response = track_get_image(request_without_referer)
        actual = response.cookies.get(COOKIE_NAME)
        expected = None
        self.assertEqual(actual, expected)

    @mock.patch('simpletracker.views.log_pageview')
    def test_when_no_referer__should_not_log(self, log_pageview_mock):
        request_without_referer = HttpRequest()
        track_get_image(request_without_referer)
        log_pageview_mock.assert_not_called()

    def test__when_referer_set__should_set_cookie(self):
        request_with_referer = create_request_with_referer()
        response = track_get_image(request_with_referer)
        actual = response.cookies.get(COOKIE_NAME)
        not_expected = None
        self.assertNotEqual(actual, not_expected)

    @mock.patch('simpletracker.views.log_pageview')
    def test_when_referer_set__should_log(self, log_pageview_mock):
        request_with_referer = create_request_with_referer()
        track_get_image(request_with_referer)
        log_pageview_mock.assert_called_once()
