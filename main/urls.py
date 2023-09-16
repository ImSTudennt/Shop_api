from django.urls import path
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm

from main.views import PartnerUpdate, LoginAccount
# RegisterAccount, LoginAccount, CategoryView, ShopView, ProductInfoView, \
#     BasketView, \
#     AccountDetails, ContactView, OrderView, PartnerState, PartnerOrders, ConfirmAccount

app_name = 'main'
urlpatterns = [
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('user/login', LoginAccount.as_view(), name='user-login'),

]