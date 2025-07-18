# Ninja API Key


[![PyPI](https://img.shields.io/pypi/v/ninja-api-key.svg)](https://pypi.python.org/pypi/ninja-api-key)

[![codecov](https://codecov.io/gh/lucasrcezimbra/ninja-api-key/graph/badge.svg)](https://codecov.io/gh/lucasrcezimbra/ninja-api-key)


API Key authentication for [Django Ninja](https://django-ninja.dev/).

This is a fork from [django-ninja-apikey](https://github.com/mawassk/django-ninja-apikey).

Key Features:
- Easy integration into your projects
- Well integrated with the Admin interface
- Secure API keys due to hashing
- Works with the standard user model


## Installation

```bash
pip install ninja-api-key
```


## How to use
1. Add `ninja_apikey` to your installed apps in your Django project:
```Python
# settings.py

INSTALLED_APPS = [
    # ...
    "ninja_apikey",
]
```

2. Apply migrations
```shell
python manage.py migrate
```

3. Secure

    a. the whole API
    ```Python
    # api.py

    from ninja import NinjaAPI
    from ninja_apikey.security import APIKeyAuth

    #  ...

    api = NinjaAPI(auth=APIKeyAuth())

    # ...

    @api.get("/secure_endpoint")
    def secure_endpoint(request):
        return f"Hello, {request.user}!"
    ```

    b. an specific endpoint
    ```Python
    # api.py

    from ninja import NinjaAPI
    from ninja_apikey.security import APIKeyAuth

    #  ...

    auth = APIKeyAuth()
    api = NinjaAPI()

    # ...

    @api.get("/secure_endpoint", auth=auth)
    def secure_endpoint(request):
        return f"Hello, {request.user}!"
    ```


4. ninja-api-key uses `settings.PASSWORD_HASHERS` to hash the API keys.
   Django's default `PBKDF2PasswordHasher` may be slow depending on the number
   of iterations. You can change the `settings.PASSWORD_HASHERS` to
   use a faster (but less secure) one. ninja-api-key provides a `SHA256PasswordHasher`.

   ```python
    # settings.py

    PASSWORD_HASHERS = [
        "ninja_apikey.hashers.SHA256PasswordHasher",
        # others
    ]
    ```

    ⚠️ Keep in mind that this will affect Django authentication as a whole,
       not just ninja-api-key.


## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes and releases.

## Contributing

Contributions are welcome; feel free to open an Issue or Pull Request.

```
git clone https://github.com/lucasrcezimbra/ninja-api-key
cd ninja-api-key
python -m venv .venv
source .venv/bin/activate
pip install .[test]
pre-commit install
make test
```
