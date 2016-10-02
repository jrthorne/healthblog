from django.conf.urls import patterns, include, url
from blog.models import Question
from blog.views import QuestionListView, QuestionAddView, QuestionModView, \
QuestionDelView, AnswerAddView

urlpatterns = patterns('blog.views', 
    url(r'^$', 'home', name='home'),   
    url(r'^questionlist/$', QuestionListView.as_view(), name='question_list'),
    url(r'^questionadd/$', QuestionAddView.as_view(), name='question_add'),
    url(r'^questionmod/(?P<pk>\d+)/$', QuestionModView.as_view(), name='question_mod'),
    url(r'^questiondel/(?P<pk>\d+)/$', QuestionDelView.as_view(), name='question_del'),
    url(r'^answerquestion/(?P<question_pk>\d+)/$', AnswerAddView.as_view(),\
    name='answer_question'),
    url(r'^answervoteplus/(?P<ansId>\d+)/$', 'answer_vote_plus', name='answer_vote_plus'),
    url(r'^answervoteminus/(?P<ansId>\d+)/$', 'answer_vote_minus', name='answer_vote_minus'),
)