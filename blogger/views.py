from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
<<<<<<< HEAD
from blogger.models import Avatar
=======
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 0a009633fadd6ed47669973d23c4c5e639b2d31e
from django.contrib.auth.decorators import login_required
from blogger.forms import UserForm
from django.shortcuts import redirect

<<<<<<< HEAD
# """ class SignUpView(SuccessMessageMixin, CreateView):
#     template_name = 'create_user.html'
#     success_url = reverse_lazy('home')
#     form_class = UserCreationForm
#     success_message = '¡Perfil creado satisfactoriamente!' """
=======
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()


    return render(request, 'create_user.html', {'form': form})

=======

=======

>>>>>>> refs/remotes/origin/main
class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'create_user.html'
    success_url = reverse_lazy('home')
    form_class = UserCreationForm
    success_message = '¡Perfil creado satisfactoriamente!'
>>>>>>> 0a009633fadd6ed47669973d23c4c5e639b2d31e

class BloggerProfile(DetailView):
    model = User
    template_name = "profile.html"

class BloggerUpdate(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "update_profile.html"
    fields = ["username", "email", "first_name", "last_name"]
    success_message = '¡Perfil actualizado satisfactoriamente!'
    
    def get_success_url(self):
      return reverse_lazy("profile", kwargs={"pk": self.request.user.id})
<<<<<<< HEAD

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()


    return render(request, 'create_user.html', {'form': form})

=======
<<<<<<< HEAD
>>>>>>> refs/remotes/origin/main
=======
>>>>>>> refs/remotes/origin/main
>>>>>>> 0a009633fadd6ed47669973d23c4c5e639b2d31e
