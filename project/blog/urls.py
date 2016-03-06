from django.conf.urls import patterns, include, url
from blog.models import Question
from blog.views import QuestionListView, QuestionAddView, QuestionModView, \
QuestionDelView, AnswerAddView

urlpatterns = patterns('blog.views', 
    url(r'^$', 'home', name='home'),   
    url(r'^questionlist/$', QuestionListView.as_view(), name='questionList'),
    url(r'^questionadd/$', QuestionAddView.as_view(), name='questionAdd'),
    url(r'^questionmod/(?P<pk>\d+)/$', QuestionModView.as_view(), name='questionMod'),
    url(r'^questiondel/(?P<pk>\d+)/$', QuestionDelView.as_view(), name='questionDel'),
    url(r'^answerquestion/(?P<question_pk>\d+)/$', AnswerAddView.as_view(),\
    name='answerQuestion'),
    url(r'^answerplus/(?P<ansId>\d+)/$', 'answerPlus', name='answerPlus'),
    url(r'^answerminus/(?P<ansId>\d+)/$', 'answerMinus', name='answerMinus'),
)