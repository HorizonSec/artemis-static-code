"""Tests for the code analyzer module."""

from artemis_static_code.code_analyzer import CodeAnalyzer


def test_code_analyzer_initialization():
    """Test that CodeAnalyzer can be initialized."""
    analyzer = CodeAnalyzer()
    assert analyzer is not None


def test_code_analyzer_analyze():
    """Test the analyze method."""
    analyzer = CodeAnalyzer()
    result = analyzer.analyze("/test/path")
    
    assert result is not None
    assert result["status"] == "success"
    assert result["path"] == "/test/path"
