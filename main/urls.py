from django.urls import path
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

from main.views import BasketView, CategoryView, ConfirmAccount, ContactView, OrderView, PartnerUpdate, LoginAccount, ProductInfoView, RegisterUser, LoginAccount, ShopView


app_name = 'main'
urlpatterns = [
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('user/login', LoginAccount.as_view(), name='user-login'),
    path('user/register', RegisterUser.as_view(), name='user-register'),
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('shops', ShopView.as_view(), name='shops'),
    path('categories', CategoryView.as_view(), name='categories'),
    path('products', ProductInfoView.as_view(), name='shop'),
    path('basket', BasketView.as_view(), name='basket'),
    path('order_confirm', OrderView.as_view(), name='order_confirm'),
    path('contact', ContactView.as_view(), name='contact')


]