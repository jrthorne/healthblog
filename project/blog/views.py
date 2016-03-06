from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.forms.models import model_to_dict
from django.utils.text import slugify
from blog.models import Question, Answer

# Create your views here.
##################################################################
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
    
    def get_context_data(self, **kwargs):
        context = super(LoginRequiredMixin, self).get_context_data(**kwargs)
        # no idea why this is required, but using the LoginRequiredMixin causes "request"
        # not to be set in the template
        context['request'] = self.request
        return context
    
# end LoginRequiredMixin

##################################################################
class QuestionListView(LoginRequiredMixin, ListView):
    model = Question
    # Note that I use the default for template_name

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        # add extra context here
        return context


class QuestionAddView(LoginRequiredMixin, CreateView):
    model = Question


class QuestionModView(LoginRequiredMixin, CreateView):
    model = Question

    def get_object(self, *args, **kwargs):
        thisQuestion = super(QuestionMod, self).get_object(*args, **kwargs)
        thisQuestion.authorized_owner_or_404(self.request.user)
        return thisQuestion


class QuestionDelView(LoginRequiredMixin, DeleteView):
    model = Question
    success_url = reverse_lazy('questionList')        


##################################################################