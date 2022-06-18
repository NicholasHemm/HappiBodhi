from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView
from .forms import SignUpForm, EditProfileForm, PasswordChangesForm, ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from firstblog.models import Profile

class UserRegistrationView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class ProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):

        user = Profile.objects.all()
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user

        return context

class PeopleView(ListView):
    model = Profile
    template_name = 'registration/people.html'

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangesForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'linkedin_url']
    success_url = reverse_lazy('home')

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile.html'
    #fields = ['bio', 'profile_pic', 'linkedin_url']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class LogoutView(CreateView):
    success_url = reverse_lazy('home')