from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from django.contrib import admin
from django.urls import path, re_path, include
from . import views

from products.views import ProductFeaturedListView as c0, ProductDetailView as b0

# (
#     product_list_view as a,
#     ProductListView as b,
#     product_detail_view as a0,
#     ProductDetailView as b0,
#     ProductFeaturedDetailView as c,
#     ProductFeaturedListView as c0,
#     ProductDetailSlugView as d
# )


#  re_path(r'^contact/$', ContactView.as_view(), name='contact'),
urlpatterns = [
    url('admin/', admin.site.urls),
    path('', views.home, name="Home"),
    path('contact/', views.hello, name="Contact"),
    re_path(r'^login/$', views.login_page, name="login"),
    path('register/', views.register_page, name="register"),
    path('register/login/', views.login_page, name="Login"),
    path('products/', include("products.urls")),

    # re_path('featured/(?P<slug>[\w-]+)/', c.as_view(), name="DetailView"),
    path('featured/', c0.as_view(), name="ListView"),
    # path('products/', b.as_view(), name='products'),
    # path('products-fbv/', a, name='products'),
    # re_path('details/(?P<pk>\d+)/', b0.as_view(), name='products'),
    # re_path('details/(?P<slug>[\w-]+)/', d.as_view(), name='products'),
    path('details/(?P<pk>\d+)', b0.as_view(), name='products'),
    # re_path('details-fbv/(?P<pk>\d+)/', a0, name='products'),
    path('list/', views.index0, name='list')
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
