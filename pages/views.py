from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm

class StaffRequiredMixin(object):
    """ ESTE MIXIN REQUERIRA QUE EL USUARIO SEA MIEMBRO DEL STAFF """

    @method_decorator(staff_member_required)
    #SOBRE ESCRITURA DEL METODO DISPATCH
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

#DEFINICION DE CLASES BASADAS EN VISTAS (CBV)
#========================================================================================
#========================================================================================
#CLASE QUE LISTA TODOS LOS OBJETOS DE UN MODELO EN FORMA DE LISTA
class PageListView(ListView):
    model = Page

#========================================================================================
#========================================================================================
#CLASE QUE MUESTRA LA INFORMACION DETALLADA DE UN OBJETO DENTRO DE UNA LISTA
class PageDetailView(DetailView):
    model = Page

#========================================================================================
#========================================================================================
#CLASE QUE PRESENTA UNA PAGINA DONDE SE PUEDAN AGREGAR OBJETOS A LA LISTA DEL MODELO
@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

#========================================================================================
#========================================================================================
#CLASE QUE PRESENTA UNA PAGINA DONDE SE PUEDAN MODIFICAR OBJETOS A LA LISTA DEL MODELO
@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self) -> str:
        return reverse_lazy('pages:update', args=[self.object.id]) + "?ok"

#========================================================================================
#========================================================================================
#CLASE QUE PRESENTA UNA PAGINA DONDE SE PUEDE ELIMINAR UN OBJETO DENTRO DE LA LISTA DEL MODELO
@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')

