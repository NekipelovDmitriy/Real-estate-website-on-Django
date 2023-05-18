from django.shortcuts import render, redirect
from .models import Agent, Listing
from .forms import AgentForm, ListingForm


def home(request):
    listings = Listing.objects.all()
    agents = Agent.objects.all()
    context = {
        'agents': agents,
        'listings': listings
    }
    return render(request, 'home.html', context)


def listing_list(request):
    listings = Listing.objects.all()
    context = {
        'listings': listings
    }
    return render(request, 'listings.html', context)


def listing_retrieve(request, pk):
    listing =Listing.objects.select_related('agent').get(id=pk)
    
    context = {
        'listing': listing
    }
    return render(request, 'listing.html', context)


def listing_create(request):
    form = ListingForm()
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listings')

    context = {
        'form': form
    }
    return render(request, 'listing_create.html', context)


def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listing', listing.id)
    context = {
        'form': form
    }
    return render(request, 'listing_create.html', context)


def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect('listings')


def agents_list(request):
    agents = Agent.objects.all()
    context = {
        'agents': agents
    }
    return render(request, 'agents/agents.html', context)


def agent_create(request):
    form = AgentForm()
    if request.method == 'POST':
        form = AgentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('agents_list')    
    context = {
        'form': form
    }
    return render(request, 'agents/agent_form.html', context)