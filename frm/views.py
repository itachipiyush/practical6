# views.py
from django.shortcuts import render
from .forms import MyForm

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the form data
            member_id = form.cleaned_data['id']
            email_id = form.cleaned_data['email']
            course = form.cleaned_data['course']
            staff = form.cleaned_data['staff']
            # Perform further actions or save the data
    else:
        form = MyForm()
    return render(request, 'first_form.html', {'form': form})

def index(request):
    return render(request, 'C:/Users/HP/Desktop/piyush django/form1/templates/index.html', )