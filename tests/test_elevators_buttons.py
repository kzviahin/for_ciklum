import pytest
from elevators import Button


def pytest_generate_tests(metafunc):
    """Pytest hook to generate button fixture with one or two values, depends on command line parameter"""
    if 'button' in metafunc.fixturenames:
        if metafunc.config.option.smoke:
            buttons = [Button("On")]
        else:
            buttons = [Button("On"), Button("Off")]
        metafunc.parametrize("button", buttons, ids=['on', 'off'])


def test_turn_on_button(button):
    """Just small check of press button method"""
    button.press_button()
    assert button.state == 'On'
