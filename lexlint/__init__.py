"""A placeholder for the LexLint command line, which is not released yet.

It holds the name `lexlint` on PyPI and makes no network call. `lexlint --version` prints the
version. Anything else says the command line is not released and exits 3, the code the real
command uses for "could not lint", so a CI step that runs it fails rather than passing.
"""
from __future__ import annotations

import sys

__version__ = "0.0.2"

NOTICE = ("lexlint {version} is a placeholder: the LexLint command line is not released yet, "
          "so nothing was linted. See https://lexlint.io for how to run LexLint today.")


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else list(argv)
    if args == ["--version"]:
        print(f"lexlint {__version__}")
        return 0
    print(NOTICE.format(version=__version__), file=sys.stderr)
    return 3
