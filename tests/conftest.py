import os
import pytest


@pytest.fixture(scope="session")
def base_url():
    """Fixture to set the Base URL from environment variable"""
    return os.environ.get("BASE_URL")
