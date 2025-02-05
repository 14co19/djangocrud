from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F

from .models import Question, Choice
from django.template import loader

# Create your views here.
def index(request):
    question = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template("polls/index.html")
    data = {
        "latest_question": question,
    }
    return render(request, 'polls/index.html', data)
    # return HttpResponse(template.render(data, request))

def detail(request, question_id):
    ques = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {"question": ques})

def result(request, question_id):
    ques = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": ques})

def vote(request, question_id):
    ques = get_object_or_404(Question, pk=question_id)

    try:
        selectedChoice = ques.choice_set.get(pk=request.POST['choice'])

    except(KeyError, Choice.DoesNotExist):
        return render(
            request,
            'polls/detail.html',
            {
                "question": ques,
                "error_message": "You didn't select a choice"
            }
        )
    else:
        selectedChoice.votes = F('votes')
        selectedChoice.save

        return HttpResponseRedirect(reverse("polls:result", args=(question_id,)))