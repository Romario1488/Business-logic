from django.shortcuts import render
from mailings.mailchimp_services import add_email_with_tag


def webhook(request):
    """Обработчик Вебхука от платежной системы"""
    add_email_with_tag(email=request.POST.get('email'),
                       audience_name='DONATES',
                       tag = 'DONATE'
                        )