"""Tests for the CLI module."""

import sys
from io import StringIO
from artemis_static_code.cli import main


def test_main_runs_successfully():
    """Test that the main function runs without errors."""
    result = main()
    assert result == 0


def test_main_prints_output(capsys):
    """Test that the main function prints expected output."""
    main()
    captured = capsys.readouterr()
    assert "ARTEMIS Static Code Analysis - CLI" in captured.out
    assert "Version: 0.1.0" in captured.out
