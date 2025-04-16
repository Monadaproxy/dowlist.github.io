from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView


from .forms import LoginUserForm, RegisterUserForm



class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': 'Регистрация'}
    success_url = '/users/login/'

    def get_user_context(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items() + list(c_def.items())))





#def login_user(request):
    #if request.method == 'POST':
        #form = LoginUserForm(request.POST)
        #if form.is_valid():
           # cd = form.cleaned_data
            #user = authenticate(request, username = cd['username'], password = cd['password'])
            #if user and user.is_active:
                #login(request, user)
                #return HttpResponseRedirect(reverse('home'))
    #form = LoginUserForm()
    #return render(request, 'users/login.html', {'form': form})

#def logout_user(request):
    #logout(request)
    #return HttpResponseRedirect(reverse('users:login'))
