import pytest
from pages.base_page import BasePage
from utils.config import URLS_TO_TEST, PAGE_LOAD_TIME_THRESHOLD
from utils.reporter import Reporter

reporter = Reporter(report_path="reports/performance_report.csv")

@pytest.mark.parametrize("url", URLS_TO_TEST)
def test_page_load_perfomance(driver,url):

    page = BasePage(driver)
    page_opened = page.open_page(url)
    assert  page_opened, f"Failed to open the page:{url}"

    load_time = page.get_page_load_time()

    if load_time <= PAGE_LOAD_TIME_THRESHOLD:
        status = "Passed"
    else:
        status = "Failed"

    reporter.add_result(page_url=url, status=status, load_time=load_time)
    reporter.save_report()


    assert status == "Passed", (
        f"The page load time {url} ({load_time} ms) exceeds the threshold value of {PAGE_LOAD_TIME_THRESHOLD} ms."
    )
@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    reporter.save_report()



