from datetime import timedelta

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
