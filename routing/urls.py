from django.conf.urls import url
import routing.views as rviews

urlpatterns = [
    url(r'^simple_route/$', rviews.simple_route, name='simple_route'),
    url(r'^slug_route/?P<param>[a-z0-9-_]{1,16}/$', rviews.slug_route, name='slug_route'),
    url(r'^sum_route/?P<x>[-?\d+]/?P<y>[-?\d+]/$', rviews.sum_route, name='sum_route'),
    url(r'^sum_get_route/$', rviews.sum_get_method, name='sum_get_route'),
    url(r'^sum_post_route/$', rviews.sum_post_method, name='sum_post_route'),
]


#     url(r'^simple_route/$', simple_route),
#     url(r'^slug_route/([a-z0-9-_]{1,16})/$', slug_route),
#     url(r'^sum_route/(-?\d+)/(-?\d+)/$', sum_route),
#     url(r'^sum_get_method/$', sum_get_method),
#     url(r'^sum_post_method/$', sum_post_method),
