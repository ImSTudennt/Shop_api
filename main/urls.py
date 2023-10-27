from django.urls import path
from main.views import (
    AccountInfoView,
    BasketView,
    CategoryView,
    ConfirmEmailAccount,
    ContactView,
    OrderView,
    PartnerState,
    PartnerUpdate,
    LoginAccount,
    ProductInfoView,
    RegisterUser,
    LoginAccount,
    ShopView,
)


app_name = "main"
urlpatterns = [
    path("partner/update", PartnerUpdate.as_view(), name="partner-update"),
    path("user/login", LoginAccount.as_view(), name="user-login"),
    path("user/register", RegisterUser.as_view(), name="user-register"),
    path(
        "user/register/confirm",
        ConfirmEmailAccount.as_view(),
        name="user-register-confirm",
    ),
    path("shops", ShopView.as_view(), name="shops"),
    path("categories", CategoryView.as_view(), name="categories"),
    path("products", ProductInfoView.as_view(), name="shop"),
    path("basket", BasketView.as_view(), name="basket"),
    path("order_confirm", OrderView.as_view(), name="order_confirm"),
    path("contact", ContactView.as_view(), name="contact"),
    path("account/info", AccountInfoView.as_view(), name="account_info"),
    path("partner/state", PartnerState.as_view(), name="account_info"),
]
