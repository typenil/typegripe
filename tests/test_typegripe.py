import pathlib
from typing import List

import pytest

from typegripe import check

FIXTURE_PATH = "./tests/file_fixtures"


@pytest.mark.parametrize("filename", ["valid_function.py", "empty.py"])
def test_valid_files(filename: str):
    assert [] == check.check_file(pathlib.Path(f"{FIXTURE_PATH}/{filename}"))


@pytest.mark.parametrize(
    "filename,expected_warnings",
    [
        (
            "function_missing_args.py",
            [
                check.TypeWarning(
                    code=check.WarnCode.UNTYPED_ARG,
                    description="",
                    line_num=1,
                    name="this",
                ),
                check.TypeWarning(
                    code=check.WarnCode.UNTYPED_ARG,
                    description="",
                    line_num=1,
                    name="thing",
                ),
            ],
        ),
    ],
)
def test_invalid_files(
    filename: str, expected_warnings: List[check.TypeWarning]
):
    assert expected_warnings == check.check_file(
        pathlib.Path(f"{FIXTURE_PATH}/{filename}")
    )
