#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.views.generic.base import View
from django.utils.http import is_safe_url
from django.utils.translation import ugettext_lazy as _

from .forms import EmailLoginForm, ForlifeLoginForm

class LoginView(View):
    
    mode = None
    template_name = "students/login.html"
    
    def dispatch(self, request, *args, **kwargs):
        mode = kwargs.get('mode', 'forlife') #if no mode is specified, forlife is the default one
        
        if mode == 'logout': # to log out the user
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
        # we decide whether the user wants to log in via email or school identifier
            self.form_class = EmailLoginForm
            self.failure_message = _("Invalid password or email address")
        else:
            self.form_class = ForlifeLoginForm
            self.failure_message = _("Invalid password or identifier/school id")
            
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        Generates the requested form, adding a next parameter used for redirection
        """
        next = request.GET.get('next', '/')
        initial = {'next': next}
        form = self.form_class(initial=initial)
        return render(request, self.template_name, {'form': form, 'mode' : self.mode, 'next': next})
            
    def post(self, request, *args, **kwargs):
        """
        Tries to authenticate the user, then redirects him/her
        """
        form = self.form_class(request.POST) 
        next = request.POST.get('next', '/')
        if form.is_valid():
            formdat = form.cleaned_data
            
                
            # authenticate() checks the parameters, and "next" is not used by the
            # authentication backend
            formdat.pop('next', None) 
            student = authenticate(**formdat)
            if student is not None: # the user has been succesfully authenticated
                if student.is_active:
                    login(request, student)
                    redirect_to = next
                    if not is_safe_url(url=redirect_to, host=request.get_host()):
                        redirect_to = '/'
                    return redirect(redirect_to) # succesfully authenticated
        return render(request, self.template_name, {'form': form, 'next': next, 'message': self.failure_message}) # authentication failed   
         
