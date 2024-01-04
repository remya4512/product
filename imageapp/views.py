from django.shortcuts import redirect,render
from imageapp.models import product
import os
# Create your views here.



def index(request):
    return render(request,'add_product.html')

def add_product(request):
    if request.method=='POST':
        pname=request.POST['pname']
        price=request.POST['price']
        qty=request.POST['qty']
        image=request.FILES.get('file')
        prd=product(product_name=pname, price=price,quantity=qty,image=image)
        prd.save()
        return redirect('show_products')
    
def show_products(request):
    prdts=product.objects.all()
    return render(request,'show_product.html',{'prdts':prdts})

def editpage(request,pk):
  prdts=product.objects.get(id=pk)
  return render(request,"edit.html",{'prdts':prdts})

def edit_product(request,pk):
    if request.method=='POST':
        prdcts=product.objects.get(id=pk)
        prdcts.product_name=request.POST.get('pname')
        prdcts.price=request.POST.get('price')
        prdcts.quantity=request.POST.get('qty')
        if len(request.FILES)!=0:
            if len(prdcts.image)>0:
                os.remove(prdcts.image.path)
            prdcts.image= request.FILES.get('file')  
        prdcts.save() 
        return redirect('show_products')
    return render(request,'edit.html')

def delete(request,pk):
   p=product.objects.get(id=pk)
   p.delete()
   return redirect('show_products')



