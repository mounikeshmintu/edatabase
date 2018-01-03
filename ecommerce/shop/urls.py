from django.urls import path,re_path
from shop import views
from django.conf import settings
from django.conf.urls.static import static
    # static files (images, css, javascript, etc.)
    # urlpatterns += patterns('',
    #     (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    #     'document_root': settings.MEDIA_ROOT}))
urlpatterns=[

path('home',views.form,name='form'),
path('login',views.loginform,name='loginform'),
path('register',views.registerform ,name='registerform'),
path('list',views.ProductListView.as_view() ,name='registerform'),
#
# path('productsfbv',views.product_list_view ,name='products'),
# path('products',views.ProductListView.as_view() ,name='products'),
# path('featured',views.ProductfView.as_view(),name='featured'),

# re_path(r'^featured/(?P<slug>[\w-]+)$',views.ProductfView.as_view(),name='featured'),
 re_path(r'^detail/(?P<pk>\d+)$',views.ProductDetailView.as_view() ,name='detailfbv'),
#path('details/<int:pk>/',views.ProductDetailView.as_view() ,name='detail'),
# re_path(r'^detail/(?P<slug>\w+)$',views.ProductDetailView.as_view(),name='detail'),
]
# if settings:
#     urlpatterns +=  static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
