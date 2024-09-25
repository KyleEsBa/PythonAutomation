import time
#from src.test.utilities.Driver import Driver
from src.test.step_definition.Hooks import Hooks
class TestSample(Hooks):
    def testSample(self):
        self.driver.get('http://www.google.com/')
        time.sleep(2)
        search_box = self.driver.find_element('name','q')
        search_box.send_keys('ChromeDriver')
        search_box.submit()
        time.sleep(2)