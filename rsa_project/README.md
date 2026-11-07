# Đề tài 12: Từ Euclid mở rộng đến mô phỏng RSA

> CẢNH BÁO: RSA tham số nhỏ chỉ dùng để minh họa. Không tự triển khai RSA để bảo vệ dữ liệu thật.
> Khóa PEM trong `results/` chỉ là khóa thử nghiệm.

## Cài đặt
    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt

## Chạy demo
    python -m cli.demo_euclid 240 46
    python -m cli.demo_rsa_toy
    python -m cli.demo_rsa_std
    python -m src.benchmark

## Chạy kiểm thử
    pytest -v

## Phân công
- A: src/numtheory.py, cli/demo_euclid.py, tests/test_numtheory.py
- B: src/rsa_toy.py, rsa_errors.py, trace.py, cli/demo_rsa_toy.py, tests/test_rsa_toy.py, test_rsa_errors.py
- C: src/rsa_std.py, rsa_compare.py, benchmark.py, cli/demo_rsa_std.py, tests/test_rsa_std.py
