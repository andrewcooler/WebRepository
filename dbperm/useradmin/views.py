from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django_tables2 import SingleTableView

from .tables import UserTable

# Create your views here.


class IndexView(SingleTableView):    
    model = User
    table_class = UserTable
    template_name = 'useradmin/index.html'
    # context_object_name = 'latest_users_list'

    # def get_queryset(self):
    #     return User.objects.all()
        # return Question.objects.filter(
        #     pub_date__lte=timezone.now()
        # ).order_by('-pub_date')[:5]

class CustomLoginView(FormView):
        form_class = LoginForm
        template_name = 'useradmin/login.html'

        
