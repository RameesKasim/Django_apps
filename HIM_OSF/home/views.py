from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, ListView
from .models import Request
from .forms import HelpRequestForm
from django.http import HttpResponseRedirect, HttpResponse


class IndexView(TemplateView):
    template_name = "home/index.html"


class AboutView(TemplateView):
    template_name = "home/contact.html"


class RequestView(TemplateView):
    template_name = "home/help_req.html"


def request_help(request):

    if request.POST:
        form1 = HelpRequestForm(request.POST)
        if form1.is_valid():
            q = Request()
            q.name = form1.cleaned_data['name']
            q.house = form1.cleaned_data['house']
            q.place = form1.cleaned_data['place']
            q.phone = form1.cleaned_data['contact']
            q.type = form1.cleaned_data['type']
            q.help_needed = form1.cleaned_data['help_needed']
            q.letter = form1.cleaned_data['letter']
            q.save()
        else:
            form1 = HelpRequestForm()
    return render(request, "home/viewreq.html", {"form": form1})


class ViewRequest(ListView):
    template_name = 'home/viewreq.html'
    model = Request
    context_object_name = "query"

