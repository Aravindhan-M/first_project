from django.contrib.auth import login, authenticate, logout
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.utils.http import is_safe_url

from .decorators import check_re_captcha
from .forms import SignUpForm, LoginForm
from .multiform import MultiFormsView
from .authyUtils import start_verification


class RegisterLoginView(MultiFormsView):
    template_name = 'user/register_login.html'
    form_classes = {'signup': SignUpForm,
                    'login': LoginForm,
                    }

    success_urls = {
        'signup': reverse_lazy('login'),
        'login': '/'
    }

    @check_re_captcha
    def signup_form_valid(self, form):

        form_name = form.cleaned_data.get('action')

        if self.request.method == 'POST':
            if form.is_valid():

                if self.request.re_captcha_is_valid:
                    form.save()
                else:
                    signup = SignUpForm(self.request.POST)
                    signup.add_error(None, "Invalid captcha please try again")
                    self.form_classes = {
                        'signup': signup,
                        'login': LoginForm
                    }
                    return super(RegisterLoginView, self).forms_invalid(self.form_classes)

        return HttpResponseRedirect(self.get_success_url(form_name))

    @check_re_captcha
    def login_form_valid(self, form):
        request = self.request
        if not request.re_captcha_is_valid:
            login_form = LoginForm(self.request.POST)
            login_form.add_error(None, "Invalid captcha please try again")
            self.form_classes = {
                'signup': SignUpForm,
                'login': login_form
            }
            return super(RegisterLoginView, self).forms_invalid(self.form_classes)
        next_ = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or None
        mobile_number = form.cleaned_data['mobile_number']
        password = form.cleaned_data['password']
        user = authenticate(request, username=mobile_number, password=password)
        if user is not None:
            login(request, user)
        if is_safe_url(redirect_path, request.get_host()):
            return redirect_path
        else:
            form_name = form.cleaned_data.get('action')
            return HttpResponseRedirect(self.get_success_url(form_name))

        return super(RegisterLoginView, self).form_invalid(form)


class Logout(TemplateView):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('login')


# class SignUp(CreateView):
#     form_class = SignUpForm
#     template_name = 'user/register_login.html'
#     success_url = reverse_lazy('registration')
#
#     def get_context_data(self, **kwargs):
#         print(kwargs,"contextsignup")
#         pass
#
#
# class Login(FormView):
#     template_name = 'user/register_login.html'
#     form_class = LoginForm
#     success_url = '/'
#
#     def form_valid(self, form):
#         request = self.request
#         next_ = request.GET.get('next')
#         next_post = request.POST.get('next')
#         redirect_path = next_ or next_post or None
#         mobile_number = form.cleaned_data['mobile_number']
#         password = form.cleaned_data['password1']
#         user = authenticate(request, username=mobile_number, password=password)
#         if user is not None:
#             login(request, user)
#         if is_safe_url(redirect_path, request.get_host()):
#             return redirect_path
#         else:
#             redirect("/")
#         return super(Login, self).form_invalid(form)
#
#
# def registration(request):
#     # con = get_context_obj(request)
#     # print(response, "response og login register")
#     # response.context_data['obj'] = con['obj']
#     # response.context_data['country'] = con['country']
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return render(request, 'user/register_login.html',{'form': form,"success":"phone number registered successfully"})
#     else:
#         form = SignUpForm()
#     return render(request, 'user/register_login.html',{'form': form})


def handle_opt(request):
    try:
         start_verification()
    except:
        pass
    return HttpResponse({"data":"dummy"},status=200)


def index(request):
    if not request.session.session_key:
        request.session.create()

    print(request.session.session_key)
    return render(request, 'home.html')


# def registration(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(email=user.email, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})

def ad(request):
    return render(request, 'ad.html')


def phone_verification(request):
    pass
    # if request.method == 'POST':
    #     form = VerificationForm(request.POST)
    #     if form.is_valid():
    #         request.session['phone_number'] = form.cleaned_data['phone_number']
    #         request.session['country_code'] = form.cleaned_data['country_code']
    #         authy_api.phones.verification_start(
    #             form.cleaned_data['phone_number'],
    #             form.cleaned_data['country_code'],
    #             via=form.cleaned_data['via']
    #         )
    #         return redirect('token_validation')
    # else:
    #     form = VerificationForm()
    # return render(request, 'phone_verification.html', {'form': form})


def token_validation(request):
    print(request.GET.get('country_code', None))
    print(request.GET.get('mobile_number', None))
    pass
    # if request.method == 'POST':
    #     form = TokenForm(request.POST)
    #     if form.is_valid():
    #         verification = authy_api.phones.verification_check(
    #             request.session['phone_number'],
    #             request.session['country_code'],
    #             form.cleaned_data['token']
    #         )
    #         if verification.ok():
    #             request.session['is_verified'] = True
    #             return redirect('verified')
    #         else:
    #             for error_msg in verification.errors().values():
    #                 form.add_error(None, error_msg)
    # else:
    #     form = TokenForm()
    # return render(request, 'token_validation.html', {'form': form})


def verified(request):
    if not request.session.get('is_verified'):
        return redirect('phone_verification')
    return render(request, 'verified.html')

