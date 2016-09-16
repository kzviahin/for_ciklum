import pytest


def pytest_addoption(parser):
    parser.addoption("--smoke", action="store_true", help="just parameter to check small test or not")