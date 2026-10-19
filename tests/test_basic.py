import sofizpay

def test_import():
    assert sofizpay is not None
    assert hasattr(sofizpay, "SofizPayClient")
    assert hasattr(sofizpay, "SofizPaySDK")

def test_version():
    assert hasattr(sofizpay, "__version__")
    assert sofizpay.__version__ == "1.1.0"
