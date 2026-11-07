"""[C] RSA-OAEP (mã hóa) và RSA-PSS (chữ ký) bằng thư viện chuẩn `cryptography`."""
from __future__ import annotations

from pathlib import Path

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

SUPPORTED_KEY_SIZES = (2048, 3072, 4096)
COMPARISON_ONLY_KEY_SIZES = (1024,)  # chỉ để so sánh, không dùng thực tế
PUBLIC_EXPONENT = 65537


def generate_key(bits: int = 2048) -> rsa.RSAPrivateKey:
    """Sinh khóa RSA, e = 65537."""
    raise NotImplementedError


def oaep_padding(hash_alg: hashes.HashAlgorithm | None = None) -> padding.OAEP:
    """OAEP với MGF1(cùng hàm băm), label=None. Mặc định SHA-256."""
    raise NotImplementedError


def pss_padding(hash_alg: hashes.HashAlgorithm | None = None, salt_length: int | None = None) -> padding.PSS:
    """PSS với MGF1; salt_length mặc định bằng độ dài hàm băm."""
    raise NotImplementedError


def max_oaep_plaintext_len(bits: int, hash_len: int = 32) -> int:
    """Độ dài tối đa bản rõ OAEP = k - 2*hLen - 2 (byte)."""
    raise NotImplementedError


def oaep_encrypt(public_key: rsa.RSAPublicKey, plaintext: bytes) -> bytes:
    raise NotImplementedError


def oaep_decrypt(private_key: rsa.RSAPrivateKey, ciphertext: bytes) -> bytes:
    raise NotImplementedError


def pss_sign(private_key: rsa.RSAPrivateKey, message: bytes) -> bytes:
    raise NotImplementedError


def pss_verify(public_key: rsa.RSAPublicKey, message: bytes, signature: bytes) -> bool:
    """Trả True/False, không ném lỗi ra ngoài (bắt InvalidSignature)."""
    raise NotImplementedError


def save_private_pem(key: rsa.RSAPrivateKey, path: str | Path) -> None:
    """Chỉ lưu khóa THỬ NGHIỆM. Không mã hóa mật khẩu vì đây là khóa bỏ đi."""
    raise NotImplementedError


def save_public_pem(key: rsa.RSAPublicKey, path: str | Path) -> None:
    raise NotImplementedError


def export_results(bits: int, out_dir: str | Path = "results") -> dict:
    """Chạy trọn quy trình cho một cỡ khóa và ghi tệp:
    results/oaep/<bits>/ (key.pem, plaintext, ciphertext.bin, decrypted, ok)
    results/pss/<bits>/  (key.pem, message, signature.bin, verify_result)
    Trả về dict tóm tắt."""
    raise NotImplementedError
