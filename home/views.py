from django.shortcuts import render
from paywix.payu import PAYU
import hashlib
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse

# Create your views here.

payu = PAYU()

def payme(request):
    if request.method == 'POST':
        data = { 'amount': '1000', 
                'firstname': 'madhav', 
                'email': 'mnandan06@gmail.com',
                'phone': '9170459494', 'productinfo': 'test'
                 
                
        }
        payu_data = payu.initiate_transaction(data)


        print("posted parameters are:")
        print(payu_data)

        return render(request, 'payme.html', {"posted": payu_data})
        #return render(request, 'payme.html', {})





# Success URL
@csrf_protect
@csrf_exempt
def payment_success(request):

    payu_success_data = payu.check_hash(dict(request.POST))

    return JsonResponse(payu_success_data)


# Failure URL
@csrf_protect
@csrf_exempt
def payment_failure(request):

    payu_failure_data = payu.check_hash(dict(request.POST))

    return JsonResponse(payu_failure_data)
