from django.test import TestCase
from django.urls import reverse
import pytest
from contents.models import HostedContent
from contents.models import UploadedContent
from contents.models import CheckedContent
import datetime


@pytest.fixture
def new_hosted_content(db):
    hosted_content = HostedContent.objects.create(
        title='Item South Pavilion_PreOpClinic-CO-02approved_elec',
        folder_path='/ ABSMC Campuses / Summit Campus / South Pavilion / As-Builts / PDF',
        release_date=datetime.datetime(2022, 9, 1), 
        revision=1,
        content_type='Drawings',
        content_subtype='As-Built',
        content_format='PDF'
    )
    return hosted_content


def test_search_hosted_contents(new_hosted_content):
    assert HostedContent.objects.filter(
        title='Item South Pavilion_PreOpClinic-CO-02approved_elec').exists()
