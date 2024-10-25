import pytest
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from ninja_apikey.admin import APIKeyAdmin
from ninja_apikey.models import APIKey


@pytest.mark.django_db
def test_admin_save():
    admin_site = AdminSite()
    apikey_admin = APIKeyAdmin(APIKey, admin_site=admin_site)
    assert admin_site
    assert apikey_admin
    user = User()
    user.name = get_random_string(10)
    user.password = get_random_string(10)
    user.save()
    assert user
    key = APIKey()
    key.user = user
    key = apikey_admin.save_model(request=None, obj=key, form=None, change=None)
    assert key
    assert key.prefix
    assert key.hashed_key
    assert key.user == user
