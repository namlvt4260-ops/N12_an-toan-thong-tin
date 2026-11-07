"""[B] Kiểm thử điều kiện cần của RSA tham số nhỏ."""
import pytest

from src import rsa_toy


def test_textbook_example():
    key = rsa_toy.generate_keypair(61, 53, e=17)
    assert key.n == 3233 and key.phi == 3120 and key.d == 2753
    c = rsa_toy.encrypt(65, key.public)
    assert c == 2790
    assert rsa_toy.decrypt(c, key.private) == 65


@pytest.mark.slow
@pytest.mark.parametrize("p,q,e", [(5, 11, 3), (11, 13, 7), (61, 53, 17)])
def test_all_messages_roundtrip(p, q, e):
    key = rsa_toy.generate_keypair(p, q, e=e)
    for m in range(key.n):
        assert rsa_toy.decrypt(rsa_toy.encrypt(m, key.public), key.private) == m


def test_carmichael_and_phi_give_same_plaintext():
    # TODO: sinh khóa với use_carmichael True/False, so sánh kết quả giải mã
    pass


def test_verify_key_report():
    # TODO: kiểm tra các trường của verify_key (exhaustive True/False)
    pass
