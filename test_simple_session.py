from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://sigmath.org/sessions/sess_02xFexFIl3VkAIH2GjWYFm")
    page.get_by_label("Name").click()
    page.get_by_label("Name").fill("Olga.test")
    page.get_by_role("button", name="Submit").click()

    expect(page.locator("#raise_a_hand-button")).to_be_visible()
    expect(page.locator("#stop-showing-member-cursors-button")).to_be_visible()
    options_button = page.get_by_role("button", name="Open options")
    expect(options_button).to_be_visible()

    page.get_by_role("button", name="Open options").click()

    page.get_by_role("button", name="Save & exit").click()
    page.get_by_role("button", name="Yes, save and exit").click()

    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
