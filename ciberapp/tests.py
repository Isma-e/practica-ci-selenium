from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service # <--- AFAGEIX AIXÒ
from webdriver_manager.chrome import ChromeDriverManager # <--- AFAGEIX AIXÒ
from selenium.webdriver.common.by import By

class WebCheck(LiveServerTestCase):
    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        # AQUESTA LÍNIA ÉS LA CLAU:
        self.selenium = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), 
            options=options
        )

    def tearDown(self):
        self.selenium.quit()

    def test_home_page_title(self):
        self.selenium.get(self.live_server_url)
        body_text = self.selenium.find_element(By.TAG_NAME, "body").text
        self.assertIn("Portal segur", body_text)
