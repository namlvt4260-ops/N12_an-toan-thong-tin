"""[C] Demo RSA chuẩn: python -m cli.demo_rsa_std [--bits 2048 3072 4096]"""
import argparse

from src import rsa_compare, rsa_std


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bits", type=int, nargs="+", default=list(rsa_std.SUPPORTED_KEY_SIZES))
    parser.add_argument("--compare", action="store_true", help="Chạy demo RSA thô vs OAEP/PSS")
    args = parser.parse_args()
    # TODO: với mỗi cỡ khóa gọi rsa_std.export_results, in tóm tắt; nếu --compare gọi rsa_compare.run_all
    raise NotImplementedError


if __name__ == "__main__":
    main()
