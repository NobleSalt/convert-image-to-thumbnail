from django.http.response import HttpResponse, HttpResponseRedirect
from toThumb.form import ImageForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

# Create your views here.


class UploadImage(View):
    template_name = 'file.html'

    def get(self, request):
        form = ImageForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ImageForm(self.request.POST, self.request.FILES)
        print('Checking...')
        if form.is_valid():
            print('Valid')
            form.save()
            return HttpResponseRedirect(reverse('home'))
        print('Invalid !')
        return HttpResponseRedirect(reverse('thumb:nail'))
