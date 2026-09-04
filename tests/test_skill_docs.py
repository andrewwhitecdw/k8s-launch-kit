import pathlib

import pytest

SKILL_PATH = pathlib.Path("skills/k8s-launch-kit-generate/SKILL.md")


def test_number_of_planes_describes_none_as_multiplane_mode():
    content = SKILL_PATH.read_text()
    assert (
        "An explicit `none` also implies 1, and an explicit 1 implies `none`." not in content
    )
    assert (
        "An explicit `--multiplane-mode=none` also implies `--number-of-planes 1`, "
        "and an explicit `--number-of-planes 1` implies `--multiplane-mode=none`."
