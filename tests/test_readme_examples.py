#!/usr/bin/env python3
"""Regression tests for README.md CLI examples."""

import re
import sys
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"


def test_specific_node_group_example_uses_groups_flag():
    content = README.read_text()
    block_pattern = re.compile(
        r"### Generate Deployment Files for a Specific Node Group.*?"
        r"```bash\n(.*?)```",
        re.DOTALL,
    )
    match = block_pattern.search(content)
    assert match, "Specific node group example block not found in README.md"
    example = match.group(1)
    assert "--groups group-0" in example, "Example should use the --groups flag"
    assert re.search(r"--group\b", example) is None, (
        "Example must not use the singular --group flag; the CLI flag is --groups"
    )


