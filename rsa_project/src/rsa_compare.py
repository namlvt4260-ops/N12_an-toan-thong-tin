"""[C] Demo đối chiếu RSA thô và lược đồ có đệm."""
from __future__ import annotations


def raw_rsa_encrypt_bytes(message: bytes, n: int, e: int) -> int:
    """RSA thô: c = int(message)^e mod n. Chỉ dùng để minh họa tính tất định."""
    raise NotImplementedError


def demo_raw_is_deterministic(bits: int = 2048) -> dict:
    """Mã hóa cùng thông điệp 2 lần bằng RSA thô -> c1 == c2."""
    raise NotImplementedError


def demo_oaep_is_randomized(bits: int = 2048) -> dict:
    """Mã hóa cùng thông điệp 2 lần bằng OAEP -> c1 != c2, nhưng cùng giải mã ra bản rõ."""
    raise NotImplementedError


def demo_raw_malleability(bits: int = 2048) -> dict:
    """Tính khả nhân: E(m1)*E(m2) mod n = E(m1*m2 mod n) với RSA thô."""
    raise NotImplementedError


def demo_pss_tamper(bits: int = 2048) -> dict:
    """Sửa 1 bit của chữ ký (hoặc của thông điệp) -> pss_verify trả False."""
    raise NotImplementedError


def run_all(out_path: str = "results/compare_demo.txt") -> None:
    raise NotImplementedError
