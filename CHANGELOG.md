# Changelog

## 1.1.0 - 2021-01-22
### Changed
- Switched to Textual VDF version 2.0
  - Now, all VDF types can be used as top-level elements
  - Note: VDF 1.0 files can still be highlighted
- The brackets in array types are now highlighted as part of the type

## 1.0.0 - 2020-12-28
### Added
- Extension icon
- MIT License

### Changed
- Language ID is now "vdf" instead of "vulcdataformat"
- Types and boolean values are now case-insensitive

## 0.2.0 - 2020-11-27
### Added
- The top-level element must be of object or list type
- Everything written after the top-level element is closed is a comment

### Fixed
- Fixed bug triggering autoclosing pairs inside strings

## 0.1.0 - 2020-11-24
- Initial release
