from datetime import timedelta

import pytest
from django.contrib.auth.hashers import (
    make_password,
)
from django.contrib.auth.models import User
from django.test.utils import override_settings
from django.utils import timezone

from ninja_apikey.models import APIKey


def test_is_valid():
    key = APIKey()
    assert key
    assert key.is_valid
    key.revoked = True
    assert not key.is_valid
    key.revoked = False
    assert key.is_valid
    key.expires_at = timezone.now() - timedelta(minutes=1)
    assert not key.is_valid
    key.expires_at = timezone.now() + timedelta(minutes=1)
    assert key.is_valid
    key.expires_at = None
    assert key.is_valid


@pytest.mark.parametrize(
    ["hasher"],
    [
        ["pbkdf2_sha256"],
        ["pbkdf2_sha1"],
        ["argon2"],
        ["bcrypt_sha256"],
        ["bcrypt"],
        ["scrypt"],
        ["md5"],
        ["sha256"],
    ],
)
@override_settings(
    PASSWORD_HASHERS=[
        "django.contrib.auth.hashers.PBKDF2PasswordHasher",
        "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
        "django.contrib.auth.hashers.Argon2PasswordHasher",
        "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
        "django.contrib.auth.hashers.BCryptPasswordHasher",
        "django.contrib.auth.hashers.ScryptPasswordHasher",
        "django.contrib.auth.hashers.MD5PasswordHasher",
        "ninja_apikey.hashers.SHA256PasswordHasher",
    ]
)
@pytest.mark.django_db
def test_hashed_key_max_length(hasher):
    """
    max_length=128 is based on Django AbstractBaseUser
    https://github.com/django/django/blob/5.1.2/django/contrib/auth/base_user.py#L41
    """
    user = User.objects.create_user(username="test", password="test")
    encoded = make_password("whatever", hasher=hasher)

    api_key = APIKey.objects.create(user=user, prefix="prefix", hashed_key=encoded)

    assert api_key
    assert len(encoded) <= 128
