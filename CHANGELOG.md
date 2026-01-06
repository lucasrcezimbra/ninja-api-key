# Changelog

## [Unreleased]

## [2.0.0] - 2025-01-06
### Changed
- Remove Python 3.9 support, keep 3.10-3.14

### Internal
- pre-commit autoupdates

## [1.0.3] - 2025-10-14
### Fixed
- String representation of APIKey model to use `get_username()`

### Docs
- Add CHANGELOG.md
- Update README.md

### Internal
* Add copilot-instructions and copilot-setup-steps for GitHub Copilot
* pre-commit autoupdates

## [1.0.2] - 2024-07-14

### Fixed
- Increase APIKey.hashed_key max_length

### Internal
- Reorganize tests
- pre-commit autoupdate

## [1.0.0] - 2024-05-09

### Added
- Updates password when checking
- Add SHA256 password hashers

### Fixed
- Unpin Python version - now requires >=3.6.2

### Internal
- Add pre-commit
- Fix CI/CD and update actions
- Reorganize dependencies

[Unreleased]: https://github.com/lucasrcezimbra/ninja-api-key/compare/2.0.0...HEAD
[2.0.0]: https://github.com/lucasrcezimbra/ninja-api-key/compare/1.0.3...2.0.0
[1.0.3]: https://github.com/lucasrcezimbra/ninja-api-key/compare/1.0.2...1.0.3
[1.0.2]: https://github.com/lucasrcezimbra/ninja-api-key/compare/1.0.0...1.0.2
[1.0.0]: https://github.com/lucasrcezimbra/ninja-api-key/releases/tag/1.0.0
