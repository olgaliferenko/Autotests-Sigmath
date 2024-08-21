from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://freshmart.com.ua/")
    page.get_by_role("link", name="Овочі Овочі").click()
    expect(page.get_by_role("link", name="Овочі Овочі")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
