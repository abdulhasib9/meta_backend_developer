from django.shortcuts import render
from .forms import review_form
# Create your views here.
def customer_review(request):
    forms = review_form()
    return render(request,'cars/customer_review.html',context={'form':forms})