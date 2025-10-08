

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

# List all contacts
def home(request):
    query = request.GET.get('q')
    if query:
        contacts = Contact.objects.filter(name__icontains=query)
    else:
        contacts = Contact.objects.all()
    return render(request, 'home.html', {'contacts': contacts})

# Add new contact
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'add_contact.html', {'form': form})

# Update contact
def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'edit_contact.html', {'form': form})

# Delete contact
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('home')
    return render(request, 'delete_contact.html', {'contact': contact})


def search_contact(request):
    query = request.GET.get('q')
    results = Contact.objects.filter(name__icontains=query) if query else []
    return render(request, 'search_results.html', {'results': results, 'query': query})

