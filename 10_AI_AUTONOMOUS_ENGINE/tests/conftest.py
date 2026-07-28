import pytest


def pytest_collect_file(parent, file_path):

    if file_path.name.startswith("autonomous_engine_"):

        return pytest.Module.from_parent(
            parent,
            path=file_path
        )

    return None