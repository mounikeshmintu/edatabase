from django.shortcuts import render,get_object_or_404
from shop.forms import ContactForm,LoginForm,RegisterForm
from django.contrib.auth import authenticate,login
from django.views.generic import ListView,DetailView
from shop.models import Product,ProductManager
# from PIL import image
# Create your views here.
def form(request):
    contact_form =ContactForm(request.POST or None)
    context={

        "form":contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)


    return render(request,"shop/index2.html",context)
def loginform(request):
    form = LoginForm()
    if form.is_valid():
        print("hey form is correct")
        susername = form.cleaned_data.get("username")
        spassword = form.cleaned_data.get("password")
        user= authenticate(request,username='susername',password='spassword')
        if user is not None:
            login(request,user)
    context={
        'login':form
    }
    return render(request,"shop/login.html",context)
def registerform(request):
    form = RegisterForm()
    if form.is_valid():
        print("hey form is correct")
        susername = form.cleaned_data.get("username")
        susername = form.cleaned_data.get("email")
        spassword = form.cleaned_data.get("password")
        spassword2 = form.cleaned_data.get("password2")
        # user= authenticate(request,username='susername',password='spassword')
        # if user is not None:
        #     login(request,user)
    context={
        'register':form
    }
    return render(request,"shop/register.html",context)
class ProductListView(ListView):
    model=Product
class ProductDetailView(DetailView):
    model=Product
    def Product_detail_view(request,pk):
        try:
            product_id = Product.objects.get(pk=pk)
        except Book.Doesnotexist:
            raise Http404("your product doesnt exist")
            context={
                product:'product_id'
            }
        return render(request,'shop/product_detail.html',context)
class ProductfView(DetailView):
    model = Product
    template_name='shop/featured.html'
    def get_context_data(self,**kwargs):
        context=super(ProductfView,self).get_context_data(**kwargs)
        context['f_list']=Product.objects.featured()
        return context

# class ProductFeaturedView(DetailView):
#     model=Product
#     def Product_detail_view(request,pk):
#         try:
#             queryset = Product.objects.all().featured()
#
#             # product_id = Product.objects.featured(pk=pk)
#         except Book.Doesnotexist:
#             raise Http404("your product doesnt exist")
#             context={
#                 featured:'queryset'
#             }
#         return render(request,'shop/product_detail.html',context)

#class ProductFeaturedDetailView( DetailView):

    # queryset = Product.objects.all()
    # template_path='shop/product_list.html'
    #model=Product
    # def product_detail_view(request,ListView):
    #     instance=get_object_or_404(Product,pk=pk)
    #     context={
    #         'detailobj':instance
    #
    #     }
    #     return render(request,"shop/product_list.html",context)

    # def get_context_data(self,pk=None,*args,**kwargs):
    #     context= super(ProductDetailView ,self).get_context_data(*args,**kwargs)
    #     context['product_list']= books.objects.get(pk=pk)
    #     return context
