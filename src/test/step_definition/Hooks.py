import pytest

from src.test.utilities.Driver import Driver

class Hooks:
    @pytest.hookimpl(tryfirst=True)
    def setup_method(self):
        self.driver = Driver().get_driver()

    @pytest.hookimpl(trylast=True)
    def teardown_method(self):
        Driver.get_driver(self).quit()
