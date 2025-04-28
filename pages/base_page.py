from typing import Any


class BasePage:
    def __init__(self,driver):
        self.driver = driver
    def open_page(self,url):
        try:
            self.driver.get(url)
            return True
        except Exception as e:
            print(f"Failed to open the page  {url}. Fault: {e}")
            return False

    def get_page_load_time(self):
        navigation_timing = self.driver.execute_script(
            "return window.performance.getEntriesByType('navigation')[0]"
        )

        if navigation_timing and navigation_timing["loadEventEnd"] > 0:
            start_time = navigation_timing["startTime"]
            load_event_end = navigation_timing["loadEventEnd"]
            page_load_time = load_event_end - start_time
        else:
            # Якщо дані погані — fallback на старий метод
            timing = self.driver.execute_script("return window.performance.timing")
            navigation_start = timing["navigationStart"]
            load_event_end = timing["loadEventEnd"]
            page_load_time = load_event_end - navigation_start

        return int(page_load_time)


