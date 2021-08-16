from django.views.generic import TemplateView
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
class PasswordChangeView(TemplateView):
    template_name = 'password_change_form.html'
