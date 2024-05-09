from django.contrib.auth.hashers import (
    check_password,
    identify_hasher,
    is_password_usable,
    make_password,
)
from django.test.utils import override_settings

from ninja_apikey.hashers import SHA256PasswordHasher


@override_settings(PASSWORD_HASHERS=["ninja_apikey.hashers.SHA256PasswordHasher"])
def test_sha256():
    """
    Based on https://github.com/django/django/blob/5.0.6/tests/auth_tests/test_hashers.py#L110
    """
    encoded = make_password("lètmein", "seasalt", hasher="sha256")
    assert (
        encoded
        == "sha256$seasalt$e0327e0c88846ec7f85601380e86c72a5242e3455a1ae0f736f349858f126eb9"
    )
    assert is_password_usable(encoded) is True
    assert check_password("lètmein", encoded) is True
    assert check_password("lètmeinz", encoded) is False
    assert identify_hasher(encoded).algorithm == "sha256"


@override_settings(PASSWORD_HASHERS=["ninja_apikey.hashers.SHA256PasswordHasher"])
def test_blank_password():
    """
    Based on https://github.com/django/django/blob/5.0.6/tests/auth_tests/test_hashers.py#L110
    """
    blank_encoded = make_password("", "seasalt", "sha256")
    assert blank_encoded.startswith("sha256$")
    assert is_password_usable(blank_encoded) is True
    assert check_password("", blank_encoded) is True
    assert check_password(" ", blank_encoded) is False


@override_settings(PASSWORD_HASHERS=["ninja_apikey.hashers.SHA256PasswordHasher"])
def test_entropy_check():
    """
    Based on https://github.com/django/django/blob/5.0.6/tests/auth_tests/test_hashers.py#L110
    """
    hasher = SHA256PasswordHasher()
    encoded_weak_salt = make_password("lètmein", "iodizedsalt")
    encoded_strong_salt = make_password("lètmein", hasher.salt())
    assert hasher.must_update(encoded_weak_salt) is True
    assert hasher.must_update(encoded_strong_salt) is False
