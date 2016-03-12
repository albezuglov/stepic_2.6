from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import *

# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK')


def defaultOk(request, *args, **kwargs):
    return HttpResponse('OK')


def posts_list(request, *args, **kwargs):
    #questions = Post.objects.all().order_by("-added_at")
    sort_by = kwargs.get('sort_by', '-id')
    post_list = Question.objects.all().order_by("-rating" if sort_by == "rating" else "-id")
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'posts_list.html', {'posts': posts})


def question(request, *args, **kwargs):
    try:
        q_id = kwargs['id']
        q = Question.objects.get(pk=q_id)
    except (KeyError, Question.DoesNotExist ):
        raise Http404("Question not found")

    form = AnswerForm(initial={'question': str(q.pk)})
    return render(request, 'question.html', {'question': q, 'form': form})
   
 
def ask_form(request, *args, **kwargs):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()

    return render(request, 'ask_form.html', {'form': form})


def answer_form(request, *args, **kwargs):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            url = answer.question.get_absolute_url()
        else:
            q = form.cleaned_data['question']
            url = q.get_absolute_url() 
        return HttpResponseRedirect(url)
    else:
        raise Http404('No answer page here')
