from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.contrib.auth.base_user import BaseUserManager
from django import forms

from House.forms import HouseForm
from Employment.forms import EmployeeForm
from Scheduling.forms import SchedulePeriodForm

from Scheduling.models import SchedulePeriod, ShiftType
from House.models import House
from Employment.models import Employee

from django.views.generic import TemplateView
from django.views.generic.edit import FormView, CreateView
import json

#-------------------------------------------------------------------------------
# Page Views
#-------------------------------------------------------------------------------


class RegisterHouse(FormView):
    template_name = 'setUP/HouseForm.html'
    form_class = HouseForm
    success_url = reverse_lazy('SetUP:SchedulePeriod')

    def form_valid(self, form):
        data = form.cleaned_data
        House.objects.create(
            manager=data['manager'],
            name = data['name'],
            primary_color = data['primary_color'],
            secondary_color = data['secondary_color']
        )
        return super(RegisterHouse, self).form_valid(form)

class SchedulePeriodForm(FormView):
    template_name = 'setUP/scheduleperiod_form.html'
    form_class = SchedulePeriodForm
    success_url = reverse_lazy('SetUP:ShiftTypes')

    def form_valid(self, form):
        data = form.cleaned_data
        if data['end_date'] > data['start_date']:
            SchedulePeriod.objects.create(
            start_date = data['start_date'],
            end_date = data['end_date']
            )
        return super(SchedulePeriodForm, self).form_valid(form)

class ShiftTypes(CreateView):
    model = ShiftType
    fields = '__all__'

class CurrentEmployees(FormView):
    template_name = 'setUP/CurrentEmployeesForm.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('SetUP:SetUpComplete')

    def form_valid(self, form):
        data = form.cleaned_data
        password = BaseUserManager.make_random_password(self)
        user = User.objects.create_user(
            username=data['first_name'],
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            password = password
        )
        employee = Employee.objects.create(
            user=user,
            phone_number=data['phone_number'],
            email = user.email,
            pay_rate = data['pay_rate']
        )
        return super(CurrentEmployees, self).form_valid(form)

class SetUpComplete(TemplateView):
    template_name = 'setUP/SetUpComplete.html'

class BeginSetUp(TemplateView):
    template_name = 'setUP/BeginSetUp.html'
