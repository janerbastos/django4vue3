from django.shortcuts import (render, redirect)
from django.contrib import (auth, messages)
from django.contrib.auth.decorators import login_required

# models
from .models import User

# forms
from .forms import (
    LoginForm,
    RegisterForm,
    ForgotPasswordForm,
    ChangerPassword,
    ProfileForm,
    RecoverPassword,
)

# Create your views here.

def login (request):
    forn = None
    next = request.GET.get('next', '/admin')
    template = 'usuarios/form-login.html'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = auth.authenticate(email=email, password=password )
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect(next)
                else:
                    messages.warning(request, 
                    'Usuário esta inativo. Acesse seu email para \
                    ativar sua conta ou procute o administrador do sistema.')
            else:
                messages.warning(request, 
                    'Por favor, insira um email e senha corretos para \
                    uma conta de equipe. Note que ambos campos são \
                    sensíveis a maiúsculas e minúsculas.')
    else:
        form = LoginForm()
    return render(request, template, context={'title': 'Entrar', 'form': form})


@login_required(login_url='login')
def logout (request):
    template = 'usuarios/logout.html'
    auth.logout(request)
    messages.success(request, 'Sessão encerrada com sucesso.')
    return render(request, template, context={'title': 'Sessão encerrada'})


def forgot_password(request):
    template = 'usuarios/form-forgot-password.html'
    form = ForgotPasswordForm()
    return render(
        request, template,
        context={'title': 'Esquici minha senha', 'form': form}
    )


def recover_password(request):
    template = 'usuarios/form-recover-password.html'
    form = form = RecoverPassword()
    return render(
        request, template,
        context={'title': 'Esquici minha senha', 'form': form}
    )


def register (request):
    template = 'usuarios/form-register.html'
    form = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'phone_number': form.cleaned_data['phone_number'],
                'email': form.cleaned_data['email'],
                'username': form.cleaned_data['username'],
            }
            user = User.objects.create(**data)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Envia e-mail para ativação de conta.

            messages.success(request,
                'Usuário registrado com sucesso. \
                Verifique seu email para concluir seu registro.'
            )
            return redirect('login')
        else:
            messages.warning( request,
                'Não foi possível fazer seu registro. \
                Corrija os erros e tente novamente')

    else:
        form = RegisterForm()
    return render(request, template, context={'title': 'Novo registro', 'form': form})


@login_required(login_url='login')
def changer_password(request):
    template = 'usuarios/form-changer-password.html'
    user = request.user
    form = None
    if request.method == 'POST':
        form = ChangerPassword(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if user.check_password(password):
                repeat_password = form.cleaned_data['repeat_password']
                user.set_password(repeat_password)
                user.save()
                messages.success(request, 'Senha alterada com sucesso.')
                return redirect('login')
            else:
                messages.warning(request, 'A senha atual esta errada, corrija e tente novamente.')
                return redirect('changer-password')
        else:
            messages.warning(request, 
                'Não foi possível alterar sua senha. \
                Corrija os erros e tente novamente')
    else:
        form = ChangerPassword()
    return render(request, template, context={'title': 'Troca de senha', 'form': form})


@login_required(login_url='login')
def profile(request):
    user = request.user
    profile = user.profile
    form = None
    template = 'usuarios/form-profile.html'
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():

            profile.address_line_1 = form.cleaned_data['cover_photo']
            profile.address_line_1 = form.cleaned_data['address_line_1']
            profile.address_line_2 = form.cleaned_data['address_line_1']
            profile.country = form.cleaned_data['country']
            profile.state = form.cleaned_data['state']
            profile.city = form.cleaned_data['city']
            profile.pin_code = form.cleaned_data['pin_code']
            profile.latitude = form.cleaned_data['latitude']
            profile.longitude = form.cleaned_data['longitude']

            profile.save()

            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
            
    return render(request, template, context={'title': 'Profile do usuário', 'form': form})