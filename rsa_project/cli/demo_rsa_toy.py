"""[B] Demo RSA nhỏ: python -m cli.demo_rsa_toy [--p 61 --q 53 --e 17 --m 65]"""
import argparse

from src import rsa_toy
from src.rsa_errors import RSAError
from src.trace import Tracer

ERROR_CASES = [
    {"name": "p = q", "p": 61, "q": 61, "e": 17, "m": 65},
    {"name": "e không nguyên tố cùng nhau với phi", "p": 61, "q": 53, "e": 12, "m": 65},
    {"name": "m >= n", "p": 61, "q": 53, "e": 17, "m": 4000},
    {"name": "p không nguyên tố", "p": 15, "q": 53, "e": 17, "m": 65},
]


def run_normal(p: int, q: int, e: int, m: int, csv_path: str | None) -> None:
    raise NotImplementedError


def run_error_cases(out_path: str) -> None:
    """Chạy từng ca trong ERROR_CASES, bắt RSAError, ghi mã lỗi + thông báo vào out_path."""
    raise NotImplementedError


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", type=int, default=61)
    parser.add_argument("--q", type=int, default=53)
    parser.add_argument("--e", type=int, default=17)
    parser.add_argument("--m", type=int, default=65)
    parser.add_argument("--errors", action="store_true", help="Chạy các ca lỗi có kiểm soát")
    args = parser.parse_args()
    raise NotImplementedError


if __name__ == "__main__":
    main()
