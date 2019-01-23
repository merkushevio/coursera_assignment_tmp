from django.urls import reverse
from django.test import RequestFactory
from routing.views import sum_route
from pytest import mark


class TestViews:

    sum_test_data = [(3, -1, 2), (1, 1, 2), (0, 0, 0), (-1, 1, 0)]

    @mark.parametrize("x,y,expected", sum_test_data)
    def test_sum_route(self, x, y, expected):
        path = reverse('sum_route', args=(3, -1))
        request = RequestFactory().get(path)
        response = sum_route(request, x, y)
        assert int(response.status_code) == 200
