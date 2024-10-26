import pytest
from django.contrib.auth.hashers import (
    PBKDF2PasswordHasher,
    check_password,
    make_password,
)
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from ninja_apikey.models import APIKey
from ninja_apikey.security import check_apikey, generate_key


def test_key_generation():
    data = generate_key()
    assert data
    assert data.prefix
    assert data.key
    assert data.hashed_key
    assert check_password(data.key, data.hashed_key)


@pytest.mark.django_db
def test_check_apikey():
    assert not check_apikey(None)
    user = User()
    user.name = get_random_string(10)
    user.password = get_random_string(10)
    user.save()
    assert user
    key = APIKey()
    key.user = user
    key_data = generate_key()
    key.prefix = key_data.prefix
    key.hashed_key = key_data.hashed_key
    key.save()
    assert key
    assert user.username in str(key)
    assert not check_apikey(key_data.key)
    assert not check_apikey(key.prefix)
    assert not check_apikey(f"{key_data.prefix}.{get_random_string(10)}")
    assert check_apikey(f"{key_data.prefix}.{key_data.key}")
    user.is_active = False
    user.save()
    assert not check_apikey(f"{key_data.prefix}.{key_data.key}")
    user.delete()
    assert not check_apikey(f"{key_data.prefix}.{key_data.key}")


@pytest.mark.django_db
def test_check_apikey_updates_if_hash_changed():
    class CustomHasher(PBKDF2PasswordHasher):
        iterations = 1

    key_data = generate_key()
    hashed_key = make_password(key_data.key, hasher=CustomHasher())

    api_key = APIKey.objects.create(
        user=User.objects.create_user(username="test", password="test"),
        prefix=key_data.prefix,
        hashed_key=hashed_key,
    )

    check_apikey(f"{key_data.prefix}.{key_data.key}")

    api_key.refresh_from_db()
    assert api_key.hashed_key != hashed_key
    assert api_key.hashed_key.startswith(
        f"pbkdf2_sha256${PBKDF2PasswordHasher.iterations}$"
    )
