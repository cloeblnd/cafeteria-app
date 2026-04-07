from django.shortcuts import render, redirect
from .models import Product, Transaction
from .forms import StudentForm


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction_list.html', {'transactions': transactions})

def student_add(request):
    if request.method == 'POST':
        # Traiter le formulaire
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

    


