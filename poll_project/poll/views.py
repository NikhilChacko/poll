from django.shortcuts import render, redirect
from .forms import CreatePollForm
from .models import Poll
from django.http import HttpResponse

def home(request):
    polls = Poll.objects.all()
    context = {
        'polls':polls
    }
    return render(request, 'poll/home.html', context)

def create(request):

    if request.method=='POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            # print(form.cleaned_data['question'])

    else:
        form = CreatePollForm()
    context = {
        'form': form

    }
    return render(request, 'poll/create.html', context)

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method =='POST':

        selected_option = request.POST['poll']

        if selected_option =='op1':
            poll.op1_count+=1

        elif selected_option=='op2':
            poll.op2_count += 1

        elif selected_option == 'op3':
            poll.op3_count += 1

        else:
            return HttpResponse(400, 'invlid form')

        poll.save()

        return redirect('results',poll.id)

    context = {
        'poll':poll
    }
    return render(request, 'poll/vote.html', context)

def result(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    context = {
        'poll':poll
    }
    return render(request, 'poll/results.html', context)