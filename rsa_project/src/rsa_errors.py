"""[B] Các lỗi có kiểm soát của mô phỏng RSA. Mỗi lỗi có mã (code) để ghi vào bảng ca lỗi."""


class RSAError(Exception):
    code = "RSA_ERROR"


class PEqualsQError(RSAError):
    """p = q: n = p^2 nên phi(n) = p(p-1) khác (p-1)^2, và n dễ phân tích bằng căn bậc hai."""
    code = "P_EQUALS_Q"


class NotPrimeError(RSAError):
    """p hoặc q không nguyên tố: công thức phi(n) = (p-1)(q-1) sai."""
    code = "NOT_PRIME"


class ENotCoprimeError(RSAError):
    """gcd(e, phi) != 1: không tồn tại d."""
    code = "E_NOT_COPRIME"


class MessageOutOfRangeError(RSAError):
    """Thông điệp m ngoài [0, n): không phân biệt được m và m mod n."""
    code = "MSG_OUT_OF_RANGE"


class InvalidKeyError(RSAError):
    """Khóa không qua bước kiểm tra tính đúng (e*d != 1 mod phi, ...)."""
    code = "INVALID_KEY"
