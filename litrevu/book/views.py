from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . import forms
from book.models import Review, Ticket, UserFollows
from django.db.models import CharField, Value
from authentication.models import User


@login_required
def home(request):
    reviews = Review.objects.filter(user__followed_by__user=request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = Ticket.objects.filter(user__followed_by__user=request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    full_data = list(reviews) + list(tickets)
    sorted_full_data = sorted(full_data, key=lambda x: x.time_created, reverse=True)
    return render(request, 'book/home.html', context={'items': sorted_full_data})


@login_required
def posts(request):
    reviews = Review.objects.filter(user=request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = Ticket.objects.filter(user=request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    full_data = list(reviews) + list(tickets)
    sorted_full_data = sorted(full_data, key=lambda x: x.time_created, reverse=True)
    return render(request, 'book/posts.html', context={'items': sorted_full_data})

@login_required
def subscriptions(request):
    return render(request, 'book/subscriptions.html')

@login_required
def ticket_creation(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    return render(request, 'book/ticketCreation.html', context={'form': form})


@login_required
def ticket_answer(request, pk):
    review_form = forms.ReviewForm()
    ticket = Ticket.objects.filter(pk=pk)[0]
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    context = {
        'review_form': review_form,
        'ticket': ticket,
    }
    return render(request, 'book/ticketAnswer.html', context=context)

@login_required
def ticket_asking(request):
    review_form = forms.ReviewForm()
    ticket_form = forms.TicketForm()
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if all([review_form.is_valid(), ticket_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    context = {
        'review_form': review_form,
        'ticket_form': ticket_form,
    }
    return render(request, 'book/ticketAsking.html', context=context)

@login_required
def follow_user(request, id):
    user = User.objects.get(pk=id)
    UserFollows.objects.create(user=request.user, followed_user=user)
    return redirect("subscriptions")

@login_required
def unfollow_user(request, id):
    user = User.objects.get(pk=id)
    user_follow =UserFollows.objects.get(user=request.user, followed_user=user)
    user_follow.delete()
    return redirect("subscriptions")


@login_required
def subscriptions(request):
    query = request.GET.get("search")
    users = []
    if query:
        users = User.objects.filter(username__icontains=query)
    if query == "":
        users = User.objects.all()

    user_follows = []
    for user_follow in UserFollows.objects.filter(user=request.user):
        user_follows.append(user_follow.followed_user)
    results = []
    for user in users:
        if user not in user_follows:
            results.append(user)
    followers = UserFollows.objects.filter(followed_user=request.user)
    following = UserFollows.objects.filter(user=request.user)

    context = {
        "user_search": results,
        "followers": followers,
        "following": following,
    }

    return render(request, 'book/subscriptions.html', context)

@login_required
def delete_ticket(request, id):
    ticket = Ticket.objects.get(pk=id)
    if request.user == ticket.user :
        ticket.delete()
    return redirect("posts")

@login_required
def delete_review(request, id):
    review = Review.objects.get(pk=id)
    if request.user == review.user :
        review.delete()
    return redirect("posts")

@login_required
def modify_ticket(request, id):
    ticket = Ticket.objects.get(pk=id)
    if request.user != ticket.user :
        return redirect("posts")
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'book/ticketCreation.html', context={'form': forms.TicketForm(instance=ticket)})

@login_required
def modify_review(request, id):
    review = Review.objects.get(pk=id)
    ticket = review.ticket
    if request.user != review.user :
        return redirect("posts")
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('home')
    context = {
        'review_form': forms.ReviewForm(instance=review),
        'ticket': ticket,
    }
    return render(request, 'book/ticketAnswer.html', context=context)
    
