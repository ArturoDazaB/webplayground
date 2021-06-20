from os import name
from django.views.generic.edit  import UpdateView
from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Profile

# VISTA DE REGISTRO
class SignUpView(CreateView):
    # CONFIGURACION DE FORMULARIO 
    form_class = UserCreationFormWithEmail
    # ASIGNACION DEL TEMPLATE NAME
    template_name = 'registration/signup.html'
    # CONFIRUACION DE REDIRECCION LUEGO DEL REGISTRO
    def get_success_url(self) -> str:
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # MODIFICAR EN TIEMPO REAL DE LOS CAMPOS DEL FORMULARIO 'CreateView'
        form.fields['username'].widget = forms.TextInput(attrs={"class":"form-control mb-2", "placeholder":"Nombre de usuario"})
        form.fields['email'].widget = forms.EmailInput(attrs={"class":"form-control mb-2", "placeholder":"Correo electronico"})
        form.fields['password1'].widget = forms.PasswordInput(attrs={"class":"form-control mb-2", "placeholder":"Contraseña"})
        form.fields['password2'].widget = forms.PasswordInput(attrs={"class":"form-control mb-2", "placeholder":"Confirmacion de la contraseña"})
        form.fields['username'].label = ''
        form.fields['email'].label = ''
        form.fields['password1'].label = ''
        form.fields['password1'].label = ''

        return form

@method_decorator(login_required, name = 'dispatch')
class ProfileUpdate(UpdateView):
    form = ProfileForm
    fields = ['avatar', 'bio', 'link']
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        # RECUPERAR EL OBJETO QUE SE VA A EDITAR
        profile, created = Profile.objects.get_or_create(user = self.request.user)
        return profile 

@method_decorator(login_required, name = 'dispatch')
class EmailUpdate(UpdateView):
    form = EmailForm
    fields = ['email']
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        return self.request.user

    def get_form(self, form_class = None):
        form = super(EmailUpdate, self).get_form()
        # MODIFICAR EN TIEMPO REAL DE LOS CAMPOS DEL FORMULARIO 'CreateView'
        form.fields['email'].widget = forms.EmailInput(attrs={"class":"form-control mb-2", "placeholder":"Email"})

        return form