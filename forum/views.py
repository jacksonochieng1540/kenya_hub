from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm



def question_list(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'forum/question_list.html', {'questions': questions})

@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            # Reputation +5
            request.user.reputation += 5
            request.user.save()
            return redirect('question_list')
    else:
        form = QuestionForm()
    return render(request, 'forum/ask_question.html', {'form': form})


def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = question.answers.all()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.save()
            # Reputation reward for answering
            question.author.reputation += 2
            question.author.save()
            return redirect('question_detail', pk=question.pk)
    else:
        form = AnswerForm()
    return render(request, 'forum/question_detail.html', {
        'question': question,
        'answers': answers,
        'form': form
    })


@login_required
def answer_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            # Reputation +10
            request.user.reputation += 10
            request.user.save()
            return redirect('question_detail', pk=pk)
    else:
        form = AnswerForm()
    return render(request, 'forum/question_detail.html', {'question': question, 'form': form})
