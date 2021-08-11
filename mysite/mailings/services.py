from typing import Union

from mailings.mailchimp_services import add_email_with_tag
from mailings.models import CommonMailingList, CaseMailingList
from cases.models import Cases

def add_email_to_common_list(email: str):
    """Добавляет email в общий лист рассылки"""
    add_email_with_tag(audience_name='COMMON', email = email, tag = 'COMMON TAG')

    CommonMailingList.objects.get_or_create(email=email)


def add_email_to_case_list(email: str,  case_id: Union[int, str]):
    """Добавляет email в лист рассылки по делу"""
    case = Cases.objects.get(pk=case_id)
    add_email_with_tag(audience_name='CASES', email = email, tag = f'Cases {case.name}')
    CaseMailingList.objects.get_or_create(email=email)
