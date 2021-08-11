from django.db import models

from django.db import models

class CommonMailingList(models.Model):
    """Рассылка на общ материалы сайта"""
    email = models.EmailField('Email подписчика')


    class Meta:
        db_table = 'common_mailing_list'

class CaseMailingList(models.Model):
    """Рассылка на общ материалы сайта"""
    email = models.EmailField('Email подписчика')
    case = models.ForeignKey(to='cases.Cases', verbose_name='Дело', on_delete=models.CASCADE)


    class Meta:
        db_table = 'case_mailing_list'
