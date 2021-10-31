# from django.conf import settings
# from django.conf.urls.static import static
# from django.conf.urls import url

# from django.contrib import admin
from django.urls import path, re_path

from .views import (
    # product_list_view as a,
    ProductListView as b,
    # product_detail_view as a0,
    # ProductDetailView as b0,
    # ProductFeaturedDetailView as c,
    # ProductFeaturedListView as c0,
    ProductDetailSlugView as d
)


#  re_path(r'^contact/$', ContactView.as_view(), name='contact'),
urlpatterns = [
    path('', b.as_view()),
    re_path('(?P<slug>[\w-]+)/', d.as_view()),

]
