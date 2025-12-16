"""Tests for the taxonomy classification module."""

from minisweagent.taxonomy.classify_agent import generate_taxonomy_report


def test_generate_taxonomy_report():
    """Test that the taxonomy report is generated correctly."""
    report = generate_taxonomy_report()
    
    # Check that report is a non-empty string
    assert isinstance(report, str)
    assert len(report) > 0
    
    # Check that report contains expected sections
    assert "# SWE Agent Taxonomy Classification Report" in report
    assert "## Agent: mini-swe-agent" in report
    
    # Check all categories are present
    categories = [
        "AGENT ARCHITECTURE",
        "AGENT COGNITION - Workflow Patterns",
        "AGENT COGNITION - Planning Strategies", 
        "AGENT COGNITION - Reasoning Techniques",
        "AGENT MEMORY",
        "AGENT TOOL"
    ]
    for category in categories:
        assert category in report
    
    # Check expected labels are present
    expected_labels = [
        "SINGLE-AGENT",
        "ITERATIVE",
        "DIRECT-EXECUTION",
        "REPLANNING",
        "REACT",
        "CHAIN-OF-THOUGHT",
        "EPHEMERAL",
        "FILE-MANAGEMENT",
        "SHELL-SCRIPTING"
    ]
    for label in expected_labels:
        assert label in report
    
    # Check that justifications are present
    assert "**Justification:**" in report
    assert report.count("**Justification:**") == 6


def test_report_structure():
    """Test that the report has the correct structure."""
    report = generate_taxonomy_report()
    
    # Check markdown formatting
    assert report.startswith("# SWE Agent Taxonomy Classification Report")
    assert "**Labels:**" in report
    assert report.count("**Labels:**") == 6
    
    # Verify all six categories have labels and justifications
    assert report.count("###") == 6
