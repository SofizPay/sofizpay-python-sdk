# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).





## [1.2.1] - 2026-11-21

### Fixed
- `verify_webhook_payload` now checks the exact signed format `"cib" + payment_status + amount + order_number`
  (confirmed with real sandbox and production webhooks). `callback_url` is deprecated and ignored: the callback
  URL is not part of the signed message, so passing it in 1.2.0 rejected genuine webhooks.

### Docs
- README: real `message` example and no `callback_url` recommendation.

## [1.2.0] - 2026-11-21

### Added
- `SofizPayClient.verify_webhook_payload(payload, callback_url=None)` and module-level
  `sofizpay.verify_webhook_payload`: verify the CIB webhook signature **and** that `payment_status`,
  `amount` and `order_number` match the signed `message`. Use it before trusting those fields.

### Fixed
- `verify_signature` / `verify_webhook_signature` return `False` instead of raising when `message`
  or `signature` is not a string.

## [1.0.2] - 2025-08-01
sd

## [1.0.2] - 2025-08-01
sd

## [1.0.2] - 2025-08-01
hello

## [1.0.2] - 2025-08-01
hello

## [1.0.1] - 2025-07-16

### Added
- Initial release of SofizPay SDK for Python
- Payment operations using Stellar network
- DZT asset support with default issuer configuration
- Real-time transaction streaming and monitoring
- Balance checking for DZT and other assets
- Transaction history retrieval
- Transaction lookup by hash
- Comprehensive error handling and validation
- Async/await support for all operations
- Rate limiting for API calls
- Context manager support
- Extensive documentation and examples
- Full test suite with pytest

### Features
- **Payment Management**: Send DZT payments with memo support
- **Transaction Monitoring**: Real-time transaction streaming
- **Balance Checking**: Get DZT balances and all account assets
- **Transaction History**: Retrieve transaction records with filtering
- **Error Handling**: Comprehensive exception hierarchy
- **Validation**: Input validation for all operations
- **Rate Limiting**: Built-in rate limiting for API stability
- **Examples**: Complete examples for all major operations

### Technical Details
- Compatible with Python 3.8+
- Uses stellar-sdk 8.0+ for Stellar operations
- Async/await support throughout
- Comprehensive test coverage
- Type hints for better IDE support
- PEP 8 compliant code style

### Documentation
- Complete API documentation
- Usage examples in Arabic and English
- Installation and setup instructions
- Error handling guidelines
- Development setup guide
