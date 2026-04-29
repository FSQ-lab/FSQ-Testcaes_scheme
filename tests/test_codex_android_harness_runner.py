from __future__ import annotations

import importlib.util
from pathlib import Path


def load_runner():
    path = Path(__file__).resolve().parents[1] / "skills" / "codex-fsq-case-runner" / "scripts" / "codex_android_harness_runner.py"
    spec = importlib.util.spec_from_file_location("codex_android_harness_runner", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_long_press_target_is_detected():
    runner = load_runner()

    gesture = runner.gesture_for_target("I perform a long press gesture on address bar")

    assert gesture == {"type": "long_press", "target": "address bar"}


def test_rect_center_uses_element_bounds():
    runner = load_runner()

    assert runner.rect_center({"x": 10, "y": 20, "width": 100, "height": 40}) == (60, 40)
