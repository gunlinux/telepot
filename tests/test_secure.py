from ..utils import is_valid, generate_sign


def test_basic():
    secret = '1234'
    sign = generate_sign(secret, 'loki', message='test_message')
    assert sign
    assert is_valid(secret, sign, 'loki', message='test_message')
    assert not is_valid(secret, sign, 'loki1', message='test_message')
    assert not is_valid(secret, sign, 'loki', message='test_message1')
    assert not is_valid(f'{secret}1', sign, 'loki', message='test_message')
