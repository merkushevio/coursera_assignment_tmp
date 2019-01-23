from django.urls import reverse, resolve


class TestUrls:

    def test_simple_route(self):
        path = reverse('simple_route')
        assert resolve(path).view_name == 'simple_route'

    def test_slug_route(self):
        path = reverse('slug_route', args=('123456789',))
        assert resolve(path).view_name == 'slug_route'

    def test_sum_route(self):
        path = reverse('sum_route', args=(3, -1))
        assert resolve(path).view_name == 'sum_route'

