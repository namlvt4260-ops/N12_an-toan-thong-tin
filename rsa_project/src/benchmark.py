"""[C] Benchmark: sinh khóa, mã hóa, giải mã, ký, xác minh. Chạy: python -m src.benchmark"""
from __future__ import annotations

import time  # dùng time.perf_counter

from src import rsa_std

KEY_SIZES = (1024, 2048, 3072, 4096)
ITERATIONS = {"keygen": 10, "encrypt": 200, "decrypt": 200, "sign": 200, "verify": 200}
WARMUP = 5  # số lần chạy khởi động, không tính vào kết quả
MESSAGE = b"benchmark message"


def time_it(func, repeat: int, warmup: int = WARMUP) -> list[float]:
    """Chạy func nhiều lần, trả về danh sách thời gian (giây) mỗi lần."""
    raise NotImplementedError


def summarize(samples: list[float]) -> dict:
    """mean, stdev, min, max, median (đơn vị ms)."""
    raise NotImplementedError


def bench_keygen(bits: int) -> dict:
    raise NotImplementedError


def bench_encrypt_decrypt(bits: int) -> dict:
    raise NotImplementedError


def bench_sign_verify(bits: int) -> dict:
    raise NotImplementedError


def environment_info() -> dict:
    """CPU, hệ điều hành, phiên bản Python, phiên bản cryptography/OpenSSL."""
    raise NotImplementedError


def write_log(results: list[dict], env: dict, path: str = "results/benchmark.log") -> None:
    raise NotImplementedError


def write_csv(results: list[dict], path: str = "results/benchmark.csv") -> None:
    raise NotImplementedError


def plot(results: list[dict], path: str = "results/benchmark_plot.png") -> None:
    """matplotlib: cột/đường theo cỡ khóa; dùng trục log nếu chênh lệch lớn."""
    raise NotImplementedError


def main() -> None:
    raise NotImplementedError


if __name__ == "__main__":
    main()
