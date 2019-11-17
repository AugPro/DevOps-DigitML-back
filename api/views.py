from django.shortcuts import render
from django.http import JsonResponse
from .forms import ImageForm

# Create your views here.

def predict(request):
    if (form := ImageForm(request.POST, request.FILES)).is_valid():
        img = form.cleaned_data['img']
        prediction = "8"
        if not prediction.isdigit():
            return JsonResponse({'status': 'failure', 'msg': 'prediction did not work'})
        else:
            return JsonResponse({'status': 'success', 'data': prediction})
    else:
        return JsonResponse({'status': 'failure', 'msg': 'form is not valid'})
