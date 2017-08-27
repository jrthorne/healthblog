from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.utils.text import slugify
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from .models import Question, Answer

@login_required()
def answer_vote_minus(request, ansId):
    """
    TODO: make an API called by the page with AJAX
    """
    myAns = get_object_or_404(Answer, pk=ansId)
    myAns.votes -= 1
    myAns.save()
    redirectTo = reverse('answer_question', args=[myAns.question.pk])
    return HttpResponseRedirect(redirectTo)


@login_required()
def answer_vote_plus(request, ansId):
    """
    TODO: make an API called by the page with AJAX
    """
    myAns = get_object_or_404(Answer, pk=ansId)
    myAns.votes += 1
    myAns.save()
    redirectTo = reverse('answer_question', args=[myAns.question.pk])
    return HttpResponseRedirect(redirectTo)


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

    def get_context_data(self, **kwargs):
        context = super(LoginRequiredMixin, self).get_context_data(**kwargs)
        """ no idea why this is required, but using the
        LoginRequiredMixin causes "request" not to be set
        in the template"""
        context['request'] = self.request
        return context


class AnswerAddView(LoginRequiredMixin, CreateView):
    model = Answer
    fields = ['answer']
    success_url = reverse_lazy('question_list')

    def get_context_data(self, **kwargs):
        context = super(AnswerAddView, self).get_context_data(**kwargs)
        myQuestion = Question.objects.get(pk=self.kwargs['question_pk'])
        context['question'] = myQuestion
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user.poster
        myQuestion = Question.objects.get(pk=self.kwargs['question_pk'])
        form.instance.question = myQuestion
        return super(AnswerAddView, self).form_valid(form)


class QuestionListView(LoginRequiredMixin, ListView):
    model = Question
    # Note that I use the default for template_name

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        """need to sort by highest answer vote. This is slow, but okay
        for this case"""
        question_list = []
        for q in self.object_list.all():
            qdict = model_to_dict(q)
            qdict['vote_max'] = q.vote_max
            qdict['num_ans'] = q.num_ans
            question_list.append(qdict)
        context['question_list'] = sorted(question_list,
                                         key=lambda t: t['vote_max'],
                                         reverse=True)

        return context


class QuestionAddView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['title', 'description']
    success_url = reverse_lazy('question_list')

    def form_valid(self, form):
        form.instance.original_poster = self.request.user.poster
        return super(QuestionAddView, self).form_valid(form)


class QuestionModView(LoginRequiredMixin, UpdateView):
    model = Question
    fields = ['title', 'description']
    success_url = reverse_lazy('question_list')

    def get_object(self, *args, **kwargs):
        thisQuestion = super(QuestionModView, self).get_object(*args, **kwargs)
        thisQuestion.authorized_owner_or_404(self.request.user)
        return thisQuestion


class QuestionDelView(LoginRequiredMixin, DeleteView):
    model = Question
    success_url = reverse_lazy('question_list')


@ensure_csrf_cookie
def home(request):
    context = RequestContext(request,
                             {'request': request,
                              'user': request.user})
    return render_to_response('blog/home.html',
                              context_instance=context)
