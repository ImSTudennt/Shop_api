from django.forms import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from main.models import Shop, Category, Product, ProductInfo, Parametr, ProductParametr, Order, OrderItem, Contact
from yaml import load as load_yaml, Loader
from requests import get
from django.core.validators import URLValidator
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class LoginAccount(APIView):
    """
    Класс для авторизации пользователей
    """
    # Авторизация методом POST
    def post(self, request, *args, **kwargs):

        if {'email', 'password'}.issubset(request.data):
            user = authenticate(request, username=request.data['email'], password=request.data['password'])

            if user is not None:
                if user.is_active:
                    token, _ = Token.objects.get_or_create(user=user)

                    return JsonResponse({'Status': True, 'Token': token.key})

            return JsonResponse({'Status': False, 'Errors': 'Не удалось авторизовать'})

        return JsonResponse({'Status': False, 'Errors': 'Not enough all arguments'})



class PartnerUpdate(APIView):
    """
    Класс для обновления прайса от поставщика
    """
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return JsonResponse({'Status': False, 'Error': 'Log in required'}, status=403)

        if request.user.type != 'shop':
            return JsonResponse({'Status': False, 'Error': 'Только для магазинов'}, status=403)

        # url = request.data.get('url')
        with open('data/shop1.yaml', encoding='utf-8') as f:

            temp = load_yaml(f, Loader=Loader)
        # stream = get(url).content
        data = load_yaml(temp, Loader=Loader)
        shop, _ = Shop.objects.get_or_create(name=data['shop'], user_id=request.user.id)
        for category in data['categories']:
            category_object, _ = Category.objects.get_or_create(id=category['id'], name=category['name'])
            category_object.shops.add(shop.id)
            category_object.save()
        ProductInfo.objects.filter(shop_id=shop.id).delete()
        for item in data['goods']:
            product, _ = Product.objects.get_or_create(name=item['name'], category_id=item['category'])
            product_info = ProductInfo.objects.create(product_id=product.id,
                                                      external_id=item['id'],
                                                      model_name=item['model'],
                                                      price=item['price'],
                                                      price_rrc=item['price_rrc'],
                                                      quantity=item['quantity'],
                                                      shop_id=shop.id)
            for name, value in item['parameters'].items():
                parametr_object, _ = Parametr.objects.get_or_create(name=name)
                ProductParametr.objects.create(product_info_id=product_info.id,
                                                parametr_id=parametr_object.id,
                                                value=value)
        return JsonResponse({'Status': True})
    

