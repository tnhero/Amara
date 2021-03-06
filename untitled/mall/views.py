from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from .models import User


# Create your views here.
class UserFormView(View):
    form_class = UserForm
    template_name = 'mall/signup.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            telephone = form.cleaned_data['telephone']
            address1 = form.cleaned_data['address1']
            user.set_password(password)
            user.save()

            user = authenticate(email=email, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    context = {'user':user}
                    return render(request, 'mall/index.html', context)

        return render(request, self.template_name, {'form':form})


def index(request):
    template_name = 'mall/index.html'
    return render(request, template_name )


def tr(request):
    template_name = 'mall/personal.html'
    return render(request, template_name)
