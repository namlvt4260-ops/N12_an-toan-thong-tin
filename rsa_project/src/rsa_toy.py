"""[B] RSA tham số nhỏ để minh họa. KHÔNG dùng để bảo vệ dữ liệu thật."""
from __future__ import annotations

from dataclasses import dataclass

from src import numtheory as nt
from src.rsa_errors import (ENotCoprimeError, InvalidKeyError, MessageOutOfRangeError,
                            NotPrimeError, PEqualsQError)
from src.trace import Tracer


@dataclass(frozen=True)
class ToyKeyPair:
    p: int
    q: int
    n: int
    phi: int
    lam: int
    e: int
    d: int

    @property
    def public(self) -> tuple[int, int]:
        return (self.n, self.e)

    @property
    def private(self) -> tuple[int, int]:
        return (self.n, self.d)


def validate_primes(p: int, q: int) -> None:
    """Ném PEqualsQError, NotPrimeError."""
    raise NotImplementedError


def validate_exponent(e: int, modulus: int) -> None:
    """Ném ENotCoprimeError nếu gcd(e, modulus) != 1; kiểm tra 1 < e < modulus."""
    raise NotImplementedError


def validate_message(m: int, n: int) -> None:
    """Ném MessageOutOfRangeError nếu m < 0 hoặc m >= n."""
    raise NotImplementedError


def generate_keypair(p: int, q: int, e: int = 17, use_carmichael: bool = False,
                     tracer: Tracer | None = None) -> ToyKeyPair:
    """Sinh khóa từng bước, ghi vào tracer:
    n = p*q; phi = (p-1)(q-1); lambda = lcm(p-1, q-1); kiểm tra e; d = modinv(e, phi hoặc lambda)."""
    raise NotImplementedError


def encrypt(m: int, public: tuple[int, int], tracer: Tracer | None = None) -> int:
    """c = m^e mod n (dùng pow 3 tham số)."""
    raise NotImplementedError


def decrypt(c: int, private: tuple[int, int], tracer: Tracer | None = None) -> int:
    """m = c^d mod n."""
    raise NotImplementedError


def verify_key(key: ToyKeyPair, exhaustive: bool = False) -> dict:
    """Kiểm tra tính đúng của khóa. Trả về dict:
    {'gcd_e_phi_is_1': bool, 'e_d_congruent_1': bool, 'roundtrip_all_m': bool | None}
    Nếu exhaustive=True: kiểm tra m^(ed) = m (mod n) với mọi m trong [0, n)."""
    raise NotImplementedError
