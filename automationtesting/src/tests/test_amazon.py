import pytest
from playwright.sync_api import sync_playwright
from amazon_page import AmazonPage

@pytest.fixture(scope="module")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="module")
def page(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    page.close()
    browser.close()

def test_search_and_add_to_basket(page):
    amazon_page = AmazonPage(page)
    amazon_page.go_to_homepage()
    amazon_page.search_product("product name")
    amazon_page.select_first_result()
    amazon_page.add_to_basket()
    amazon_page.go_to_basket()
    amazon_page.update_quantity("2")
    assert amazon_page.get_quantity_in_basket() == "2"