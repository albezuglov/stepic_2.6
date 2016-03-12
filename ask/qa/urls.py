from django.conf.urls import include, url
from .views import *

urlpatterns = [
   #url('^(?P<question_id>\w+)/$', views.test, name='qa-test')
   url('^$', posts_list, name='postslist'),
   url('^popular/$', posts_list, name='posts-by-rating', kwargs={'sort_by': 'rating'}),
   url('^question/(?P<id>\d+)/$', question, name='question'),
   url('^ask/$', ask_form, name='ask-form'),
   url('^answer/$', answer_form, name='answer-form'),
]
