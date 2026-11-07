"""[B] Bảng truy vết: công thức -> thay số -> giá trị trung gian."""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TraceStep:
    step: int
    name: str          # ví dụ "n"
    formula: str       # ví dụ "n = p * q"
    substituted: str   # ví dụ "n = 61 * 53"
    value: object      # ví dụ 3233


@dataclass
class Tracer:
    steps: list[TraceStep] = field(default_factory=list)
    verbose: bool = False  # True: in ra màn hình ngay khi thêm bước

    def add(self, name: str, formula: str, substituted: str, value: object) -> None:
        raise NotImplementedError

    def to_rows(self) -> list[dict]:
        raise NotImplementedError

    def to_csv(self, path: str) -> None:
        raise NotImplementedError

    def to_markdown(self) -> str:
        """Bảng markdown để dán vào báo cáo Word."""
        raise NotImplementedError

    def print(self) -> None:
        raise NotImplementedError
