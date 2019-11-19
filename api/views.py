from django.shortcuts import render
from django.http import JsonResponse
from .forms import ImageForm
from django.views.decorators.csrf import csrf_exempt
import base64

# Create your views here.
@csrf_exempt
def predict(request):
    if (form := ImageForm(request.POST, request.FILES)).is_valid():
        img = form.cleaned_data['img']
        return JsonResponse({
            'status': 'success',
            'data': base64.b64encode(img.open().read()).decode('utf8')
        })
    else:
        return JsonResponse({'status': 'failure', 'msg': 'form is not valid', 'data':form.errors}, status=500)
