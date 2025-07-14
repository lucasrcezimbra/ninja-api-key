# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.2] - 2024-07-14

### Added
- Django Ninja API Key authentication package
- Secure API key hashing using Django's password hashers
- Integration with Django Admin interface
- Support for API key expiration and revocation
- Custom SHA256PasswordHasher for improved performance
- Comprehensive test suite with pytest
- API key management with prefix-based lookup
- User association with API keys
- Support for Django 3.0+ and Python 3.6+

### Security
- API keys are securely hashed before storage
- Keys cannot be retrieved in plain text after creation
- Support for key revocation and expiration

## [1.0.1] - Previous Release

### Fixed
- Minor bug fixes and improvements

## [1.0.0] - Initial Release

### Added
- Initial release forked from django-ninja-apikey
- Basic API key authentication for Django Ninja
- Core models and authentication classes

[Unreleased]: https://github.com/lucasrcezimbra/ninja-api-key/compare/v1.0.2...HEAD
[1.0.2]: https://github.com/lucasrcezimbra/ninja-api-key/compare/v1.0.1...v1.0.2
[1.0.1]: https://github.com/lucasrcezimbra/ninja-api-key/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/lucasrcezimbra/ninja-api-key/releases/tag/v1.0.0
