import subprocess
from unittest.mock import MagicMock

from load_azd_env import load_azd_env


def test_load_azd_env_azd_not_installed(monkeypatch, caplog):
    """When azd is not installed or fails, load_azd_env should log a warning and return."""
    failed_result = MagicMock()
    failed_result.returncode = 1
    failed_result.stdout = ""
    monkeypatch.setattr(subprocess, "run", lambda *args, **kwargs: failed_result)

    with caplog.at_level("WARNING"):
        load_azd_env()

    assert "azd env list failed" in caplog.text
