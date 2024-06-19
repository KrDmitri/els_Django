import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .utils.price_eval import get_price
from .models import  ELS_PRODUCT


# Create your views here.




@csrf_exempt
def get_evaluated_price(request):
    if request.method == 'POST':
        print("eval product function called")
        data = json.loads(request.body)

        product_code = data['productCode']

        try:
            product = ELS_PRODUCT.objects.get(name=product_code)
            ans = product.value
        except:
            ans = get_price(data)
            ELS_PRODUCT.objects.create(name=product_code, value=ans)

        response_data = {'answer': ans}

        response = JsonResponse(response_data)
        response["Access-Control-Allow-Origin"] = "*"  # 모든 출처 허용
        response["Access-Control-Allow-Methods"] = "POST"  # 허용할 메서드 설정

        return response


def health_check(request):
    health_status = {
        'status': 'healthy'
    }
    return JsonResponse(health_status, status=200)