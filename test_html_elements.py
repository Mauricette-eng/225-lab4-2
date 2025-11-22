from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestPlaylist(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Firefox(options=options)

    def test_songs_present(self):
        driver = self.driver

        # Use your Dev ClusterIP; adjust if needed
        driver.get("http://10.48.229.152/playlist")

        # Wait for the table to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )

        page = driver.page_source

        # Check for the 10 test songs from data-gen.py
        for i in range(10):
            title = f"Test Song {i}"
            artist = f"Test Artist {i}"
            assert title in page, f"Song title '{title}' not found on page"
            assert artist in page, f"Artist '{artist}' not found on page"

        print("✔ Selenium test passed: all 10 test songs and artists are present.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
