import pytest
from pathlib import Path


def pytest_collect_file(parent, file_path):

    if file_path.suffix == ".py":

        if "_full_test" in file_path.name:

            return pytest.Module.from_parent(
                parent,
                path=file_path
            )
