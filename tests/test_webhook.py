"""Webhook verification against real SofizPay CIB sandbox webhooks.

The fixtures below are genuine webhooks sent by SofizPay's sandbox and signed with the
production SofizPay key embedded in the SDK. They pin down the real signed format:
message == "cib" + payment_status + amount + order_number.
"""
import pytest

from sofizpay.client import SofizPayClient

REAL_SANDBOX_WEBHOOKS = [
    {
        "event": "cib.payment.updated",
        "payment_status": "success",
        "transaction_id": "26667195-d7cb-471b-b048-a43f1e10fbe3",
        "cib_transaction_id": "4790895316",
        "order_id": "be6ed33d42aa49f3b027",
        "order_number": "4790895316",
        "order_status": 2,
        "amount": 5000,
        "currency": "012",
        "message": "cibsuccess50004790895316",
        "signature": "Ocz0_NXYjh1H35Wbs7q4InKEMyxUT0uURHHCKseSa_KlOuzJVtpcqQgyhRZcgbLiXWhfTQmQhpIe2yqf71qR6WrrxmsNxLWRfw1mX13Dc2b4epnys62wkZ-OIOc4uSJpA1BNim_y9BW3wIXzWB75eo5varOaZYp27VGiZjT3xpp0UM0bC2bzOGYPhW1aKc27-Tp3b6LuG-CZS1B7rplSTfM8p3GV32pvSNTpSGDDwGYD2YRa8zo0O0GIrV0m5YpMsJ61rDnPvRUt5L4N7Xe6exyt09LUbi_tZ4V-Ke8y3S82L8Ubee656EE2LHF3iPWYH9r8wNfmtPfElpPzK57Fww=="
    },
    {
        "event": "cib.payment.updated",
        "payment_status": "failed",
        "transaction_id": "47966cdb-5359-4b75-936c-fef6c0b768d8",
        "cib_transaction_id": "7203791580",
        "order_id": "48027a3eb6bb43e2ad9b",
        "order_number": "7203791580",
        "order_status": 6,
        "amount": 5000,
        "currency": "012",
        "message": "cibfailed50007203791580",
        "signature": "M9zEtvV91_fUM1sEfe_WifckVenu0ZrfhpFysRfA8iDQwgcJKFqcG-ry2QC2cuJemlJWan8KWxZ8Rt76P0UMeafa2kY9LcgrEzd2PUE2Pg-dpT85l4wo18dsXE-W1PegZGBCUFIo7I7xTAcSJuhLuh0q6k76XxeSvA54rJBtoMK0FJqnswblk0BV3evRhpCEMlMcY5tKlWODn4znBoC2gQv9Q9MNJD_KXRil2TNgp-QVlgYQXm265STCPPUnoPLPDE-VYGbUkyrml_QEM3Lem_rC0TDB78R8sroYLL_kwBK8d6U-uydo2LlP4KqOy4eznWYbTTpRVc5_ApPR87GydA=="
    }
]


@pytest.fixture(scope="module")
def client():
    return SofizPayClient()


@pytest.mark.parametrize("payload", REAL_SANDBOX_WEBHOOKS, ids=lambda p: p["payment_status"])
def test_real_webhook_is_accepted(client, payload):
    assert payload["message"] == "cib" + payload["payment_status"] + str(payload["amount"]) + payload["order_number"]
    assert client.verify_webhook_signature(payload)
    assert client.verify_webhook_payload(payload)


@pytest.mark.parametrize("payload", REAL_SANDBOX_WEBHOOKS, ids=lambda p: p["payment_status"])
def test_deprecated_callback_url_is_ignored(client, payload):
    assert client.verify_webhook_payload(payload, "https://yourstore.com/api/cib-webhook/")


@pytest.mark.parametrize("field,value", [
    ("amount", 500000),
    ("order_number", "1111111111"),
    ("payment_status", "success"),
])
def test_tampered_top_level_field_is_rejected(client, field, value):
    failed = next(p for p in REAL_SANDBOX_WEBHOOKS if p["payment_status"] == "failed")
    tampered = dict(failed, **{field: value})
    # The signature over `message` is still valid, so the signature-only check cannot catch this...
    assert client.verify_webhook_signature(tampered)
    # ...but the payload check does.
    assert not client.verify_webhook_payload(tampered)


@pytest.mark.parametrize("bad", [
    {"message": {"a": 1}, "signature": "AAAA"},
    {"message": "cibsuccess1001", "signature": ["AAAA"]},
    {},
])
def test_malformed_payload_returns_false(client, bad):
    assert client.verify_webhook_payload(bad) is False
