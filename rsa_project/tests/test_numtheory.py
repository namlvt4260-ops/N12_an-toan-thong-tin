"""[A] Kiểm thử số học nền tảng."""
import pytest

from src import numtheory as nt

COPRIME_PAIRS = [(3, 11), (17, 3120), (65537, 3120 * 7)]
COMMON_FACTOR_PAIRS = [(12, 18), (240, 46), (100, 75)]
ZERO_PAIRS = [(0, 5), (5, 0), (0, 0)]
LARGE_PAIRS = [(2**127 - 1, 2**89 - 1)]
NO_INVERSE = [(6, 9), (4, 8), (10, 100)]


@pytest.mark.parametrize("a,b", COPRIME_PAIRS + COMMON_FACTOR_PAIRS + ZERO_PAIRS + LARGE_PAIRS)
def test_egcd_bezout(a, b):
    g, x, y = nt.egcd(a, b)
    assert g == nt.gcd(a, b)
    assert a * x + b * y == g


@pytest.mark.parametrize("a,n", COPRIME_PAIRS)
def test_modinv_correct(a, n):
    assert (a * nt.modinv(a, n)) % n == 1


# @pytest.mark.parametrize("a,n", NO_INVERSE)
# def test_modinv_no_inverse(a, n):
#     with pytest.raises(nt.NoModularInverseError):
#         nt.modinv(a, n)


# def test_phi_euler_known_values():
#     assert nt.phi_euler(3233) == 3120  # 61 * 53
#     assert nt.phi_euler(1) == 1
#     # TODO: thêm n là lũy thừa số nguyên tố, n nguyên tố


# def test_carmichael_known_values():
#     assert nt.carmichael(3233) == 780  # lcm(60, 52)
#     # TODO: so sánh lambda(n) | phi(n) với nhiều n


# def test_egcd_trace_last_row_matches_egcd():
#     # TODO: so khớp dòng cuối của egcd_trace với egcd
#     pass
