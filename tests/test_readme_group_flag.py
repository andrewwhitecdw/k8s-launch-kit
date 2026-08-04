import re
import sys
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"


def code_blocks(text):
    return re.findall(r"```(?:bash)?\n(.*?)```", text, re.DOTALL)


def test_generate_examples_use_groups_flag():
    text = README.read_text(encoding="utf-8")
    blocks = code_blocks(text)
    generate_commands = [b for b in blocks if "l8k generate" in b]

    for cmd in generate_commands:
        if re.search(r"--group\b", cmd):
            raise AssertionError(
                "README documents a non-existent --group flag in an "
                "l8k generate example.\nUse --groups instead:\n" + cmd
            )

    assert any(
        "--groups group-0" in cmd for cmd in generate_commands
    ), "README should include a single-group example using --groups group-0"


if __name__ == "__main__":
    test_generate_examples_use_groups_flag()
    print("ok")
