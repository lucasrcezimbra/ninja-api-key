# GitHub Copilot Instructions for ninja-api-key

## Project Overview

This is a Django package that provides API Key authentication for [Django Ninja](https://django-ninja.dev/). It's a fork of django-ninja-apikey with enhanced security features and better Django integration.

## Key Components

### Core Models
- `APIKey` model: Stores API keys with prefix, hashed key, user association, labels, expiration, and revocation status
- Uses Django's password hashing system for secure key storage
- Keys have format: `{prefix}.{key}` (8-char prefix + 56-char key)

### Authentication
- `APIKeyAuth` class extends Django Ninja's `APIKeyHeader`
- Uses `X-API-Key` header for authentication
- Integrates with Django's user system and permissions

### Security Features
- API keys are hashed using Django's `PASSWORD_HASHERS` setting
- Keys can be expired, revoked, or associated with inactive users
- Includes custom SHA256 hasher for performance when needed

## Code Patterns

### Django Integration
- Follow Django's model patterns and conventions
- Use `get_user_model()` for user model references
- Leverage Django's admin interface for key management
- Use Django's timezone utilities for datetime handling

### Testing
- Use pytest with pytest-django for testing
- Test files are in `ninja_apikey/tests/`
- Use parametrized tests for multiple scenarios
- Mock Django settings with `@override_settings` decorator
- Test security, models, admin, and hashers separately

### Code Style
- Use Black for code formatting (line length: 88)
- Use Ruff for linting (select: E, F, I; ignore: E501)
- Use isort with black profile for import sorting
- Follow pre-commit hooks configuration for consistency

## Development Patterns

### Dependencies
- Core: Django, django-ninja
- Testing: pytest, pytest-django, pytest-cov
- Optional: django[argon2,bcrypt] for enhanced password hashing

### Key Generation
- Use `get_random_string()` for secure random generation
- Always hash keys before storage using `make_password()`
- Return structured `KeyData` namedtuple for generated keys

### Authentication Flow
1. Extract API key from `X-API-Key` header
2. Split into prefix and key components
3. Look up APIKey record by prefix
4. Verify key against hashed value using `check_password()`
5. Validate key is not revoked and not expired
6. Ensure associated user is active
7. Set `request.user` and return user object

## Documentation Guidelines

### Changelog Maintenance
- **Always** include detailed descriptions of changes in the CHANGELOG.md
- Follow [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format
- Categorize changes as follows:
  - **Features**: for new features and functionality
  - **Fixes**: for bug fixes and corrections
  - **Internal**: for development-related changes (refactoring, tooling, CI/CD, dependencies)
- **Breaking Changes**: Flag any breaking changes clearly in the description
- Add entries to the `[Unreleased]` section until a new version is released
- Use clear, descriptive language that helps users understand the impact of changes
- Include relevant issue/PR references when applicable

## Common Use Cases

### Basic API Protection
```python
from ninja import NinjaAPI
from ninja_apikey.security import APIKeyAuth

api = NinjaAPI(auth=APIKeyAuth())

@api.get("/protected")
def protected_endpoint(request):
    return f"Hello, {request.user}!"
```

### Endpoint-Specific Protection
```python
from ninja_apikey.security import APIKeyAuth

auth = APIKeyAuth()

@api.get("/specific", auth=auth)
def specific_endpoint(request):
    return {"user": request.user.username}
```

### Performance Optimization
```python
# In settings.py for faster hashing
PASSWORD_HASHERS = [
    "ninja_apikey.hashers.SHA256PasswordHasher",
    # ... other hashers
]
```

## Testing Guidelines

- Test security edge cases (invalid keys, expired keys, revoked keys)
- Test Django admin integration and form handling
- Test password hasher compatibility and migration
- Use fixtures for creating test users and API keys
- Mock external dependencies and Django settings when needed

## File Structure
- `models.py`: APIKey model definition
- `security.py`: Authentication classes and key utilities
- `admin.py`: Django admin integration
- `hashers.py`: Custom password hashers
- `tests/`: Comprehensive test suite
- `migrations/`: Database migrations

When working with this codebase, prioritize security, follow Django conventions, and ensure compatibility with the Django Ninja framework.
