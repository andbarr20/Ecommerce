from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Department, Municipality, ProductCategory, Product, Profile, Country,Car, CarItem

from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView,UpdateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView,DestroyAPIView

from .serializers import ProductSerializer
from .serializers import CategorySerializer
#from .serializers import OrdersCreateSerializer
from .serializers import ProductCreateSerializer
#from .serializers import OrderSerializer
from .serializers import ShoppingCarSerializer
from .serializers import ItemsCarSerializer
from .serializers import ProductFoodSerializer
from .serializers import ProductFarmacySerializer
from .serializers import ProductToySerializer
from .serializers import ProductSnackSerializer

from django.contrib.auth.mixins import LoginRequiredMixin #permisos // debe estar logeado
from django.contrib.auth.mixins import PermissionRequiredMixin #permisos // se puede personalizar

# Create your views here.
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def inicio(request):
    return render(request, 'inicio.html')

class UserListView(ListView):
    model = User  # Especifica el modelo a utilizar (User en este caso)
    template_name = 'user_list.html'  # Especifica el nombre de la plantilla para mostrar la lista de usuarios
    context_object_name = 'object_list'  # Especifica el nombre de la variable de contexto para la lista de usuarios
    paginate_by = 10  # Especifica el número de usuarios por página
    queryset = User.objects.all()  # Especifica la consulta para obtener la lista de usuarios
    ordering = ['username']  # Especifica el ordenamiento de la lista de usuarios

##@permission_classes((AllowAny, ))
class productListApi(ListAPIView): #el loginrequired, es para permisos y es mejor dejarlo de primeras, con esto al intentar ver los productos, si no esta logeado, lo va a dirigir a la ventana para que se logee 
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by('product_id')

class categoryListApi(ListAPIView):
    serializer_class = CategorySerializer
    queryset = ProductCategory.objects.all().order_by('name')
    #permission_required = 'orders.view_ProductCategory' #se coloca view_nombre del modelo, view: Permite ver el objeto o acceder a la vista, add: Permite agregar o crear nuevos objetos.change: Permite modificar o editar un objeto existente.delete: Permite eliminar un objeto existente.list: Permite ver una lista de objetos.detail: Permite ver los detalles o información específica de un objeto.create: Permite crear nuevos objetos.update: Permite actualizar o editar un objeto existente.destroy: Permite eliminar un objeto existente. 

#class salesCheckCreateApi(PermissionRequiredMixin, CreateAPIView): # permiso personalizado, si no tiene el permiso de crear orden, asi este logueado no lo va a dejar
 #   queryset = SalesCheck.objects.all()
  #  serializer_class = OrdersCreateSerializer
   # permission_required='orders.create_SalesCheck'
    
class productCreateApi(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    
#class orderListApi(LoginRequiredMixin, ListAPIView): ## para ver el listado de ordenes debe estar logeado
 #   serializer_class = OrderSerializer
  #  queryset = SalesCheck.objects.all().order_by('salesCheck_id')

class carListApi(LoginRequiredMixin,ListAPIView):
    serializer_class = ShoppingCarSerializer
    queryset = Car.objects.all()

class carItemListApi(LoginRequiredMixin,ListAPIView):
    serializer_class = ItemsCarSerializer
    queryset = CarItem.objects.all()

class productFoodListApi(ListAPIView): #el loginrequired, es para permisos y es mejor dejarlo de primeras, con esto al intentar ver los productos, si no esta logeado, lo va a dirigir a la ventana para que se logee 
    serializer_class = ProductFoodSerializer
    queryset = Product.objects.filter(productCategory_id = 4)

class productFarmacyListApi(ListAPIView):
    serializer_class = ProductFarmacySerializer
    queryset = Product.objects.filter(productCategory_id = 7)

class productToyListApi(ListAPIView):
    serializer_class = ProductToySerializer
    queryset = Product.objects.filter(productCategory_id = 6)

class productSnackListApi(ListAPIView):
    serializer_class = ProductSnackSerializer
    queryset = Product.objects.filter(productCategory_id = 5)