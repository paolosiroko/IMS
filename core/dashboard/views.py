from django.shortcuts import render
from  django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from  .models import Stock

class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')


@login_required()
def dashboard(request):
    labels = []
    data = []

    stockqueryset = Stock.objects.filter(is_deleted=False).order_by('-quantity')
    for item in stockqueryset:
        labels.append(item.name)
        data.append(item.quantity)
        # sales = SaleBill.objects.order_by('-time')[:3]
        # purchases = PurchaseBill.objects.order_by('-time')[:3]
    context = {
        'labels': labels,
        'data': data,
        # 'sales': sales,
        # 'purchases': purchases
     }

    return render(request, 'home.html', context)


class StockListView(LoginRequiredMixin, ListView):
    model = Stock
    context_object_name = 'stocks'
    template_name = 'inventory.html'
