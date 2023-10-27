from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver, Signal
from main.models import ConfirmEmailToken, User

new_user_registered = Signal()
new_order = Signal()
change_order_state = Signal()

STATE_CHOICES = {
    "confirmed": "Ваш заказ - Подтвержден",
    "assembled": "Ваш заказ - Собран",
    "sent": "Ваш заказ - Отправлен",
    "delivered": "Ваш заказ - Доставлен",
    "canceled": "Ваш заказ - Отменен",
}


@receiver(new_user_registered)
def new_user_registered_signal(user_id, **kwargs):
    """
    отправляем письмо с подтрердждением почты
    """
    # send an e-mail to the user
    token, _ = ConfirmEmailToken.objects.get_or_create(user_id=user_id)

    msg = EmailMultiAlternatives(
        # title:
        f"Password Reset Token for {token.user.email}",
        # message:
        f"Ваш токен - {token.key}",
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [token.user.email],
    )
    msg.send()


@receiver(new_order)
def new_order_signal(user_id, order_id, **kwargs):
    """
    отправяем письмо при изменении статуса заказа
    """
    # send an e-mail to the user
    user = User.objects.get(id=user_id)

    msg = EmailMultiAlternatives(
        # title:
        f"Обновление статуса заказа",
        # message:
        f'Заказ сформирован\nНомер вашего заказа: {order_id}\nНаш оператор свяжется с вами в ближайшее время для уточнения делатей заказа\nСтатуc заказов вы можете посмотреть в разделе "Заказы"',
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [user.email],
    )
    msg.send()


@receiver(change_order_state)
def change_order_state_signal(user_id, state, **kwargs):
    """
    отправяем письмо при изменении статуса заказа
    """
    # send an e-mail to the user
    user = User.objects.get(id=user_id)

    msg = EmailMultiAlternatives(
        # title:
        f"Статус вашего заказа обновлен.",
        # message:
        f"{STATE_CHOICES[state]}",
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [user.email],
    )
    msg.send()
