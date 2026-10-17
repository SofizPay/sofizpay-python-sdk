"""
SofizPay SDK - Python library for Stellar-based payments

This SDK provides easy-to-use functions for integrating SofizPay 
payment functionality into Python applications.
"""

from .client import SofizPayClient
from .payments import PaymentManager
from .transactions import TransactionManager
from .exceptions import (
    SofizPayError,
    PaymentError,
    TransactionError,
    NetworkError,
    ValidationError
)

__version__ = "1.1.11"
__author__ = "SofizPay Team"
__email__ = "support@sofizpay.com"

# Unified class alias
SofizPaySDK = SofizPayClient

__all__ = [
    "SofizPayClient",
    "SofizPaySDK",
    "PaymentManager", 

    "TransactionManager",
    "SofizPayError",
    "PaymentError",
    "TransactionError",
    "NetworkError",
    "ValidationError",
    "make_cib_transaction",
    "make_sandbox_cib_transaction",
    "verify_signature",
    "verify_webhook_signature",
    "verify_sofizpay_signature"
]

# Convenience functions for easy access
def make_cib_transaction(transaction_data):
    """Convenience function to make CIB transaction"""
    client = SofizPayClient()
    return client.make_cib_transaction(transaction_data)

def make_sandbox_cib_transaction(transaction_data):
    """Convenience function to make Sandbox CIB transaction"""
    client = SofizPayClient(sandbox=True)
    return client.make_sandbox_cib_transaction(transaction_data)

def verify_signature(verification_data, signature=None):
    """Convenience function to verify signature"""
    return SofizPayClient.verify_signature(verification_data, signature)

def verify_webhook_signature(webhook_payload):
    """Convenience function to verify SofizPay webhook signature"""
    client = SofizPayClient()
    return client.verify_webhook_signature(webhook_payload)

def verify_sofizpay_signature(verification_data):
    """Convenience function to verify SofizPay signature (backward-compatible)"""
    client = SofizPayClient()
    return client.verify_sofizpay_signature(verification_data)
