from django.urls import reverse
from django.test import RequestFactory
from routing.views import sum_route, sum_get_method, echo
from pytest import mark


class TestViews:

    sum_test_data = [(3, -1, 2), (1, 1, 2), (0, 0, 0), (-1, 1, 0)]

    @mark.parametrize("x,y,expected", sum_test_data)
    def test_sum_route(self, x, y, expected):
        path = reverse('sum_route', args=(3, -1))
        request = RequestFactory().get(path)
        response = sum_route(request, x, y)
        print(response.get('Content-Type'))
        assert int(response.status_code) == 200 and int(response.get('Content-Type')) == expected

    def test_sum_get_route(self):
        path = reverse("sum_get_route")
        query_params = '?'
        for qp in 'a=1', 'b=2':
            query_params += '&{}'.format(qp)
        request = RequestFactory().get(path + query_params)
        response = sum_get_method(request)
        print(response.get('Content-Type'))
        assert int(response.status_code) == 200 and int(response.get('Content-Type')) == 3

    def test_echo_get(self):
        path = reverse('echo')
        query_params = '?a=1'
        request = RequestFactory().get(path+query_params)
        response = echo(request)
        print(response)
        assert int(response.status_code) == 200 and response.content == b'GET a: 1 statement is empty\n'

    def test_echo_get_two_query_params(self):
        path = reverse('echo')
        query_params = '?a=1&c=3'
        request = RequestFactory().get(path+query_params)
        request.META['HTTP_X-PRINT-STATEMENT'] = 'test'
        response = echo(request)
        assert int(response.status_code) == 200 and response.content == b'GET c: 3 a: 1 statement is test\n'
