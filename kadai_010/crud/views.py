from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from crud.models import Product
from django.urls import reverse_lazy


class TopView(TemplateView):
    template_name = 'top.html'


class ProductListView(ListView):
    model = Product
    context_object_name = 'object_list'
    template_name = 'crud/product_list.html'
    paginate_by = 3

    def get_queryset(self):
        # 名前ソート
        return Product.objects.order_by('id')


class ProductCreatView(CreateView):
    model = Product
    template_name = 'crud/product_form.html'
    fields = '__all__'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'crud/product_update_form.html'
    fields = '__all__'


class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'object_list'
    template_name = 'crud/product_delete_form.html'
    success_url = reverse_lazy('list')


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'object_list'
    template_name = 'crud/product_detail_form.html'
