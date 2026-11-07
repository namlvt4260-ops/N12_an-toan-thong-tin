"""[A] Demo: python -m cli.demo_euclid <a> <b>  -> in bảng (a, b, q, r, x, y) và nghịch đảo nếu có."""
import argparse
import csv

from src import numtheory as nt


def save_csv(rows: list[dict], path: str) -> None:
    raise NotImplementedError


def main() -> None:
    parser = argparse.ArgumentParser(description="Euclid mở rộng từng bước")
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    parser.add_argument("--csv", default=None, help="Ghi bảng ra CSV, ví dụ results/euclid_trace.csv")
    args = parser.parse_args()
    # TODO: gọi nt.egcd_trace, in bảng, in kết luận gcd và modinv (hoặc thông báo lỗi)
    raise NotImplementedError


if __name__ == "__main__":
    main()
