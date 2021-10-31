from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render     # get_object_or_404

from .models import Product


# Featured View
# ListView
class ProductFeaturedListView(ListView):
    # queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()


# DetailView
class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/  featured_detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()


# List-View
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(ProductListView, self).get_context_data(**kwargs)
    #     print(context)
    #     return context

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.all()


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)


# SLugView
class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/detail.html"

    # def get_object(self, *args, **kwargs):
    #     request = self.request
    #     slug = self.kwargs.get('slug')
    #     instance = get_object_or_404(Product, slug=slug)
    #     try:
    #         instance = Product.objects.get(slug=slug, active=True)
    #     except Product.DoesNotExist:
    #         raise Http404("Not found..")
    #     except Product.MultipleObjectsReturned:
    #         qs = Product.objects.filter(slug=slug, active=True)
    #         instance = qs.first()
    #     except:
    #         raise Http404("Uhhhhmmm")
    #     return instance


# Detail-View
class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        print(context)
        return context

    # def get_object(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     instance = Product.objects.get_by_id(pk)
    #     if instance is None:
    #         raise Http404("Product does not exist here Nigger!!")
    #     return instance


def product_detail_view(request, pk=None):
    # instance = Product.objects.get(pk=pk)  # id
    # instance = get_object_or_404(Product, pk=pk)
    # try:
    #     instance = Product.objects.get(id=pk)
    # except:
    #     print("no product here")
    # Custom_Model_Manager
    # instance = Product.objects.get_by_id(pk)
    # if instance is None:
    #     raise Http404("Product does not exist here Nigger!!")
    # print(instance)

    # LOOK_UP
    # qs = Product.objects.filter(id=pk)
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product does not exist here Nigger!!")
    # print(instance)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product does not exist here Nigggggeeeeeer!!")

    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)
