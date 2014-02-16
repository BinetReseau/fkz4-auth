#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.views.generic.base import View
from .forms import EmailLoginForm, ForlifeLoginForm
from django.utils.http import is_safe_url

class LoginView(View):
    
    mode = None
    template_name = "students/login.html"
    
    def dispatch(self, request, *args, **kwargs):
        mode = kwargs.get('mode', 'forlife')
        
        if mode == 'logout':
             logout(request)
             return redirect('/')
        
        if request.user.is_authenticated(): 
        # if the user is already authenticated, he/she is redirected
            next = request.GET.get('next', '/')
            redirect_to = next
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                        redirect_to = '/'
            return redirect(redirect_to)

        self.mode = mode
        if mode == 'email':
            self.form_class = EmailLoginForm
        else:
            self.form_class = ForlifeLoginForm
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        next = request.GET.get('next', '/')
        initial = {'next': next}
        form = self.form_class(initial=initial)
        return render(request, self.template_name, {'form': form, 'mode' : self.mode})
            
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            formdat = form.cleaned_data
            next = formdat['next']
                
            formdat.pop('next', None)
            student = authenticate(**formdat)
            if student is not None: # the user has been succesfully authenticated
                if student.is_active:
                    login(request, student)
                    redirect_to = next
                    if not is_safe_url(url=redirect_to, host=request.get_host()):
                        redirect_to = '/'
                    return redirect(redirect_to) # succesfully authenticated
        return render(request, self.template_name, {'form': form}) # authentication failed   
         
