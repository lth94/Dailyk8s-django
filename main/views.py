from django.shortcuts import render
import random
from .models import Problem
from userstat.models import Solved

# Create your views here.
def index(request):
    parm = request.GET.get("pnum", "")
    print(parm)
    if parm == "" :
        items = list(Problem.objects.all())
        ran = random.choice(items)
    else :
        ran = Problem.objects.get(pk=parm)
    pnum = ran.pk
    problem = ran.problem
    answer = ran.answer

    return render(request,'main/index.html', {'pnum': pnum, 'problem': problem, 'answer': answer})

def result(request):
    pnum = request.GET['pnum']
    problem = Problem.objects.get(pk=pnum)
    answer = problem.answer
    question = problem.problem
    return render(request, 'main/result.html', {'pnum': pnum, 'problem': question, 'answer': answer})

def posting(request):
    if request.method == 'GET':
        return render(request, 'main/posting.html')
    else :
        newProblem = Problem(problem=request.POST.get('problem'), answer=request.POST.get('answer'))
        newProblem.save()
        return render(request, 'main/index.html')