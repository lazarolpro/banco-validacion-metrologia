import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validate", ROOT / "validate.py")
validate = importlib.util.module_from_spec(spec)
sys.modules["validate"] = validate
spec.loader.exec_module(validate)


def _specs():
    return json.loads((ROOT / "specs" / "dut_specs.json").read_text(encoding="utf-8"))


def test_all_points_conforme_by_default():
    results = validate.validate(_specs())
    assert len(results) == 3
    assert all(r.verdict == "CONFORME" for r in results)


def test_error_within_tolerance_and_uncertainty_positive():
    for r in validate.validate(_specs()):
        assert abs(r.error) <= r.tolerance
        assert r.uncertainty > 0
        assert r.stdev >= 0


def test_reproducible():
    a = validate.validate(_specs())
    b = validate.validate(_specs())
    assert [x.mean for x in a] == [x.mean for x in b]
