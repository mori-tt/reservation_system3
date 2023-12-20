from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import CustomUser
from accounts.forms import ProfileForm, SignupUserForm, CusSignupUserForm
from django.shortcuts import render, redirect
from allauth.account import views
from app.models import Staff, Booking
from django.utils import timezone


# スタッフサインアップビュー
class SignupView(views.SignupView):
    template_name = 'accounts/signup.html'
    form_class = SignupUserForm
    def form_valid(self, form):
        if self.request.user.user_type == '1':  # スタッフ
            return redirect('store.html')
        else:  
            return redirect('/')

# class SignupView(views.SignupView):
#     template_name = 'accounts/signup.html'
#     form_class = SignupUserForm

#     def form_valid(self, form):
#         self.user = form.save(self.request)
#         return redirect(self.get_success_url('store.html'))

# カスタマーサインアップビュー
# class UserSignupView(views.SignupView):
#     template_name = 'accounts/user_signup.html'
#     form_class = SignupUserForm
class CusSignupView(views.SignupView):
    template_name = 'accounts/cus_signup.html'
    form_class = CusSignupUserForm

    def form_valid(self, form):
        self.user = form.save(self.request)
        return redirect(self.get_success_url())

# スタッフログインビュー
class LoginView(views.LoginView):
    template_name = 'accounts/login.html'
# class LoginView(views.LoginView):
#     template_name = 'accounts/login.html'

#     def form_valid(self, form):
#         super().form_valid(form)
#         if self.request.user.user_type == '1':  # スタッフ
#             return redirect('store.html')
#         else:  
#             return redirect('/')

# カスタマーログインビュー
# class UserLoginView(views.LoginView):
#     template_name = 'accounts/user_login.html'
class CusLoginView(views.LoginView):
    template_name = 'accounts/cus_login.html'

    def form_valid(self, form):
        super().form_valid(form)
        if self.request.user.user_type == '0':  # カスタマー
            return redirect('/')
        else:
            return redirect('/')

# ログアウトビュー
class LogoutView(views.LogoutView):
    template_name = 'accounts/logout.html'
    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect('/')

class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)
        staff_data = Staff.objects.filter(user=user_data).first()
        booking_data = Booking.objects.filter(staff=staff_data, start__gte=timezone.now())
        return render(request, 'accounts/profile.html', {
            'user_data': user_data,
            'staff_data': staff_data,
            'booking_data': booking_data,
        })

class ProfileEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)
        form = ProfileForm(
            request.POST or None,
            initial={
                'first_name': user_data.first_name,
                'last_name': user_data.last_name,
                'description': user_data.description,
                'image': user_data.image
            }
        )
        return render(request, 'accounts/profile_edit.html', {
            'form': form,
            'user_data': user_data
        })

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            user_data = CustomUser.objects.get(id=request.user.id)
            user_data.first_name = form.cleaned_data['first_name']
            user_data.last_name = form.cleaned_data['last_name']
            user_data.description = form.cleaned_data['description']
            if request.FILES.get('image'):
                user_data.image = request.FILES.get('image')
            user_data.save()
            return redirect('profile')

        return render(request, 'accounts/profile.html', {
            'form': form
        })