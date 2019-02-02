from datetime import datetime

from django.db.models import Q, Count, Avg
from pytz import UTC

from db.models import User, Blog, Topic


def create():
    user1 = User(first_name='u1', last_name='u1')
    user2 = User(first_name='u2', last_name='u2')
    user3 = User(first_name='u3', last_name='u3')
    user1.save()
    user2.save()
    user3.save()

    blog1 = Blog(title='blog1', author=user1)
    blog2 = Blog(title='blog2', author=user1)
    blog1.subscribers.add(user1, user2)
    blog2.subscribers.add(user2)
    blog1.save()
    blog2.save()

    topic1 = Topic(title='topic1', blog=blog1, author=user1)
    topic2 = Topic(title='topic2_content', blog=blog1, author=user3, created=datetime.strptime('2017-01-01', 'yyyy-mm-dd'))

    topic2.save()
    topic1.likes.add(user1, user2, user3)
    topic1.save()


def edit_all():
    users = User.objects.all()
    for user in users:
        user.first_name = 'uu1'
        user.save()


def edit_u1_u2():
    users = User.objects.get(Q(first_name='u1') | Q(first_name='u2'))
    for user in users:
        user.first_name = 'uu1'
        user.save()


def delete_u1():
    User.objects.get(first_name='u1').delete()


def unsubscribe_u2_from_blogs():
    Blog.subscribers.though.objects.filter(user__first_name='u2').delete()


def get_topic_created_grated():
    return Topic.objects.filter(created__gt=datetime.strptime('2018-01-01', 'yyyy-mm-dd'))


def get_topic_title_ended():
    return Topic.objects.filter(title__endswith='content')


def get_user_with_limit():
    return User.objects.all().order_by('id')[:2]

# 7. Получить количество топиков в каждом блоге, назвать поле topic_count, отсортировать по topic_count по возрастанию
# (функция get_topic_count).
#
# 8. Получить среднее количество топиков в блоге (функция get_avg_topic_count).
#
# 9. Найти блоги, в которых топиков больше одного (функция get_blog_that_have_more_than_one_topic).
#
# 10. Получить все топики автора с first_name u1 (функция get_topic_by_u1).
#
# 11. Найти пользователей, у которых нет блогов, отсортировать по возрастанию id (функция get_user_that_dont_have_blog).
#
# 12. Найти топик, который лайкнули все пользователи (функция get_topic_that_like_all_users).
#
# 13. Найти топики, у которы нет лайков (функция get_topic_that_dont_have_like).


def get_topic_count():
    return Blog.objects.annotate(topic_count=Count('topics')).order_by('topic_count')


def get_avg_topic_count():
    return Blog.objects.all().aggregate(Avg('topics'))


def get_blog_that_have_more_than_one_topic():
    return Blog.objects.annotate(topic_count=Count('topics')).filter(topic_count__gt=0)


def get_topic_by_u1():
    return Topic.objects.filter(author__first_name='u1')


def get_user_that_dont_have_blog():
    pass


def get_topic_that_like_all_users():
    pass


def get_topic_that_dont_have_like():
    pass
