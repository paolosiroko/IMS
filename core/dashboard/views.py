from django.shortcuts import render, redirect, get_object_or_404
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
from  .models import Stock,PurchaseItem,SalesItem
from .forms import CreateForm,UpdateForm,PurchaseCreateForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .filters import StockFilter

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
    template_name = 'inventory.html'
    paginate_by =10

    def get(self, request, *args, **kwargs):
        stocks = Stock.objects.all().order_by('id')
        myFilter = StockFilter(request.GET, queryset=stocks)
        stocks = myFilter.qs
        paginator = Paginator(stocks, self.paginate_by)
        page = request.GET.get('page')
        try:
            stocks = paginator.page(page)
        except PageNotAnInteger:
            stocks = paginator.page('1')
        except EmptyPage:
            stocks = paginator.page(paginator.num_page)

        context = {'stocks': stocks,
                   'myFilter': myFilter
                   }
        return render(request, self.template_name, context=context)



class StockCreateView(CreateView):
    model = Stock
    form_class = CreateForm
    success_url = reverse_lazy('inventory')
    template_name = 'form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateView, self).form_valid(form)

class StockUpdateView(UpdateView):
    model = Stock
    form_class = UpdateForm
    success_url = reverse_lazy('inventory')
    template_name = 'form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UpdateView, self).form_valid(form)


class DeleteStockView(DeleteView):
    model = Stock
    context_object_name = 'stock'
    success_url = reverse_lazy('inventory')


class PurchaseView(ListView):
    model = PurchaseItem
    template_name = "purchases/purchases_list.html"
    context_object_name = 'bills'
    paginate_by = 10


class PurchaseBillView(ListView):
    model = PurchaseItem
    template_name = "bill/purchase_bill.html"
    # bill_base = "bill/bill_base.html"

    def get(self, request, billno):
        context = {
            'bill': PurchaseItem.objects.get()
        }
        return render(request, self.template_name, context)

class PurchaseCreateView(CreateView):
    model = Stock
    form_class = PurchaseCreateForm
    success_url = reverse_lazy('purchases-list')
    template_name = 'form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateView, self).form_valid(form)


class SalesView(ListView):
    model = SalesItem
    template_name = "sales/sales_list.html"
    context_object_name = 'sales'
    paginate_by = 10


class SalesBillView(ListView):
    model = PurchaseItem
    template_name = "bill/sales_bill.html"

    def get(self, request, billno):
        context = {
            'bill': SalesItem.objects.get()
        }
        return render(request, self.template_name, context)

