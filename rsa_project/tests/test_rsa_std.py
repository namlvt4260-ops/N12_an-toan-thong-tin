"""[C] Kiểm thử RSA-OAEP và RSA-PSS."""
import pytest

from src import rsa_std


@pytest.fixture(scope="module", params=[2048, 3072])
def key(request):
    return rsa_std.generate_key(request.param)


def test_oaep_roundtrip(key):
    pt = b"hello rsa"
    ct = rsa_std.oaep_encrypt(key.public_key(), pt)
    assert rsa_std.oaep_decrypt(key, ct) == pt


def test_oaep_is_randomized(key):
    pt = b"same message"
    assert rsa_std.oaep_encrypt(key.public_key(), pt) != rsa_std.oaep_encrypt(key.public_key(), pt)


def test_oaep_plaintext_too_long(key):
    # TODO: bản rõ dài hơn max_oaep_plaintext_len phải gây ValueError
    pass


def test_pss_sign_verify(key):
    msg = b"message"
    sig = rsa_std.pss_sign(key, msg)
    assert rsa_std.pss_verify(key.public_key(), msg, sig) is True


def test_pss_flipped_bit_fails(key):
    msg = b"message"
    sig = bytearray(rsa_std.pss_sign(key, msg))
    sig[0] ^= 0x01
    assert rsa_std.pss_verify(key.public_key(), msg, bytes(sig)) is False


def test_pss_modified_message_fails(key):
    # TODO: ký msg rồi xác minh với msg đã đổi
    pass


@pytest.mark.slow
def test_key_size_4096():
    # TODO: chạy OAEP/PSS với 4096
    pass
