from pathlib import Path

from nlohmann_json import get_include


def test_header():
    include_path: Path = get_include()
    assert (include_path / "nlohmann/json.hpp").exists()
