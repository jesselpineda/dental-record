# encoding:utf-8
from datetime import datetime

from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect, render_to_response
from django.views.generic import ListView, UpdateView, CreateView

from wkhtmltopdf.views import PDFTemplateView
from core.utils import generic_search

from inventario.models import UnidadMedida, Producto, Entradas
from inventario.forms import ProductoForm, UnidadMedidaForm, EntradasForm, \
    DevolucionesForm, EgresosForm


def busqueda(request):
    query = 'q'
    MODEL_MAP = {
        Producto: ['producto', 'porciones'],
    }

    objects = []

    for model, fields in MODEL_MAP.iteritems():
        objects += generic_search(request, model, fields, query)

    return render_to_response('entradas.html', {'objects': objects,
                              'search_string': request.GET.get(query, '')})


class Productos(ListView):
    model = Producto
    context_object_name = 'productos'
    template_name = 'productos.html'


class ProductoCreate(CreateView):
    form_class = ProductoForm
    template_name = 'producto.html'
    success_url = reverse_lazy('inventario:productos')


class ProductoUpdate(UpdateView):
    form_class = ProductoForm
    model = Producto
    template_name = 'producto.html'
    success_url = reverse_lazy('inventario:productos')


class Unidades(ListView):
    model = UnidadMedida
    context_object_name = 'unidades'
    template_name = 'unidades.html'
    success_message = "%(name)s was created successfully"


def unidadView(request):
    if request.method == 'POST':
        modelform = UnidadMedidaForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect('inventario:unidades')
    else:
        modelform = UnidadMedidaForm()
    return render(request, "unidad.html", {"form": modelform})


class UnidadCreate(CreateView):
    form_class = UnidadMedidaForm
    model = UnidadMedida
    template_name = 'unidad.html'
    success_url = reverse_lazy('inventario:unidades')


def ingresarCantidad(request, entrada_id):
    # id de la entrada de producto

    if request.method == "POST":
        modelform = EntradasForm(request.POST)
        if modelform.is_valid():
            producto = modelform.cleaned_data.get('producto')
            cantidad = int(modelform.cleaned_data.get('porciones'))
            entrada = Entradas.objects.get(producto=producto)
            entrada.agregar(cantidad)
            entrada.save()
            producto = entrada.producto
            producto.agregar(cantidad)
            producto.save()
            return redirect('/inventario/productos/')
    else:
        modelform = EntradasForm()
    return render(request, "ingresar.html", {"form": modelform, })


class EntradasProducto(CreateView):
    form_class = EntradasForm
    template_name = 'ingresar.html'
    success_url = reverse_lazy('inventario:productos')

    def get_context_data(self, **kwargs):
        context = super(EntradasProducto, self).get_context_data(**kwargs)
        producto = Producto.objects.filter(pk=self.kwargs.get('pk'))
        context.update({'producto': producto})
        return context

    def get_initial(self):
        initial = super(EntradasProducto, self).get_initial()
        initial = initial.copy()
        initial['producto'] = self.kwargs.get('pk')
        return initial

    # def post(self, request, *args, **kwargs):
    #     super(EntradasProducto, self).post(request, *args, **kwargs)
    #     # TODO: Ask what those two saves were for!


class EditProductView(UpdateView):
    # TODO: Ask Ray what this is all about.
    model = Producto
    success_url = '/entradas/'
    template_name = 'producto.html'
    form_class = ProductoForm

    def get_context_data(self, **kwargs):
        context = super(EditProductView, self).get_context_data(**kwargs)
        context['action'] = reverse('producto-edit',
                                    kwargs={'pk': self.object.id})
        return context


def devoluciones(request):
    if request.method == 'POST':
        modelform = DevolucionesForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect('/inventario/devolucion/')
    else:
        modelform = DevolucionesForm()
    print modelform.helper
    messages.add_message(request, messages.SUCCESS, 'Profile details updated.',
                         fail_silently=True)
    return render(request, "devoluciones.html", {"form": modelform})


def egresos(request):
    if request.method == 'POST':
        modelform = EgresosForm(request.POST)
        if modelform.is_valid:
            modelform.save()
            return redirect('inventario/productos/')
    else:
        modelform = EgresosForm(request.POST)
    return render(request, "egresos.html", {"form": modelform})


class ProductosPDF(PDFTemplateView):
    filename = 'productos.pdf'
    template_name = 'productos_pdf.html'
    cmd_options = {
        'margin-top': 13,
    }

    def get_context_data(self, **kargs):
        context = super(ProductosPDF).get_context_data(**kargs)
        context['productos'] = Producto.objects.order_by('producto__producto')
        context['fecha'] = datetime.now().strftime("%d/%m/%Y")
        context['hora'] = datetime.now().strftime("%I:%M %p")
        return context
