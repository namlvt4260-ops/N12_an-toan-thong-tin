"""[A] Số học nền tảng: Euclid, Euclid mở rộng, nghịch đảo modulo, phi Euler, Carmichael."""
from __future__ import annotations


class NoModularInverseError(ValueError):
    """Ném ra khi gcd(a, n) != 1 nên không tồn tại nghịch đảo modulo."""

    def __init__(self, a: int, n: int, g: int):
        super().__init__(f"Không có nghịch đảo của {a} mod {n}: gcd({a}, {n}) = {g} != 1")
        self.a, self.n, self.g = a, n, g


def gcd(a: int, b: int) -> int:
    """Thuật toán Euclid. Trả về ước chung lớn nhất không âm.
    Cần xử lý: số 0, số âm."""
    while b != 0:
        a, b = b, a % b
    return abs(a)
    # raise NotImplementedError


def egcd(a: int, b: int) -> tuple[int, int, int]:
    """Euclid mở rộng. Trả về (g, x, y) sao cho a*x + b*y = g = gcd(a, b)."""
    old_r, r = a, b      # số dư: dòng trước, dòng hiện tại
    old_x, x = 1, 0      # hệ số của a
    old_y, y = 0, 1      # hệ số của b
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_x, x = x, old_x - q * x
        old_y, y = y, old_y - q * y
    if old_r < 0:        # chuẩn hóa để g không âm (khi đầu vào có số âm)
        return -old_r, -old_x, -old_y
    return old_r, old_x, old_y
    # raise NotImplementedError


def egcd_trace(a: int, b: int) -> list[dict]:
    """Euclid mở rộng có ghi vết. Mỗi dòng: {'a','b','q','r','x','y'}.
    Dùng cho bảng bước (results/euclid_trace.csv)."""

    raise NotImplementedError


def modinv(a: int, n: int) -> int:
    """Nghịch đảo của a modulo n, kết quả trong [0, n).
    Ném NoModularInverseError nếu gcd(a, n) != 1. Ném ValueError nếu n <= 1."""
    if gcd(a, n) != 1:
        g, x, y = egcd(a, n)
        raise ValueError(f"Modulo phải lớn hơn 1, nhận được n = {n}")
    else:
        g, x, y = egcd(a,n)
        return x % n
    # raise NotImplementedError


def is_prime(n: int) -> bool:
    """Kiểm tra nguyên tố cho n nhỏ (chia thử đến sqrt(n))."""
    raise NotImplementedError


def factorize(n: int) -> dict[int, int]:
    """Phân tích thừa số nguyên tố cho n nhỏ. Trả về {p: số mũ}."""
    raise NotImplementedError


def phi_euler(n: int) -> int:
    """Hàm phi Euler phi(n) (dựa trên factorize)."""
    raise NotImplementedError


def carmichael(n: int) -> int:
    """Hàm Carmichael lambda(n) (ước nhỏ nhất m > 0 sao cho a^m = 1 mod n, mọi a nguyên tố cùng nhau với n).
    Gợi ý: dùng lcm trên các lũy thừa nguyên tố, chú ý 2^k với k >= 3."""
    raise NotImplementedError


def lcm(a: int, b: int) -> int:
    """Bội chung nhỏ nhất, dùng gcd."""
    raise NotImplementedError


def format_trace_table(rows: list[dict]) -> str:
    """Định dạng kết quả egcd_trace thành bảng văn bản căn cột."""
    raise NotImplementedError
