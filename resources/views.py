from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Resource
from .forms import ResourceForm

def resource_list(request):
    resources = Resource.objects.all().order_by('-created_at')
    return render(request, 'resources/resource_list.html', {'resources': resources})

@login_required
def share_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.posted_by = request.user
            resource.save()
            return redirect('resource_list')
    else:
        form = ResourceForm()
    return render(request, 'resources/share_resource.html', {'form': form})

@login_required
def share_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.posted_by = request.user
            resource.save()
            # Reputation +3
            request.user.reputation += 3
            request.user.save()
            return redirect('resource_list')
    else:
        form = ResourceForm()
    return render(request, 'resources/share_resource.html', {'form': form})
