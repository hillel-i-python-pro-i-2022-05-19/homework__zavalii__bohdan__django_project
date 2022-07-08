from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView

from apps.contacts.models import Contact


class ShowAllContactsView(ListView):
    model = Contact
    template_name = 'contacts/show_all.html'
    context_object_name = 'contacts'


class ContactCreateView(CreateView):
    model = Contact
    fields = [
        'contact_name',
        'phone_value',
        'birthday_date'
    ]
    success_url = reverse_lazy('contacts:show_all')


class ContactUpdateView(UpdateView):
    model = Contact
    fields = ['contact_name', 'phone_value']
    success_url = reverse_lazy('contacts:show_all')


class DeleteContactsView(DeleteView):
    model = Contact
    success_url = reverse_lazy('contacts:show_all')
