"""[B] Kiểm thử các lỗi có kiểm soát."""
import pytest

from src import rsa_toy
from src.rsa_errors import (ENotCoprimeError, MessageOutOfRangeError, NotPrimeError,
                            PEqualsQError)


def test_p_equals_q():
    with pytest.raises(PEqualsQError):
        rsa_toy.generate_keypair(61, 61, e=17)


def test_e_not_coprime():
    with pytest.raises(ENotCoprimeError):
        rsa_toy.generate_keypair(61, 53, e=12)


@pytest.mark.parametrize("m", [-1, 3233, 5000])
def test_message_out_of_range(m):
    key = rsa_toy.generate_keypair(61, 53, e=17)
    with pytest.raises(MessageOutOfRangeError):
        rsa_toy.encrypt(m, key.public)


@pytest.mark.parametrize("p,q", [(15, 53), (61, 51), (1, 53)])
def test_not_prime(p, q):
    with pytest.raises(NotPrimeError):
        rsa_toy.generate_keypair(p, q, e=17)


def test_wrong_phi_when_p_not_prime_breaks_roundtrip():
    # TODO: minh họa nếu cố tình bỏ qua kiểm tra thì giải mã sai với một số m
    pass
