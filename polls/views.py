from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question
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
    response = "You're looking at the result of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting for question %s." %question_id)