from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    #user 1
    list_of_numbers = range(1,200,1)

    for index in list_of_numbers:
        username = f'user {index}'
        page = context.new_page()
        page.goto("https://sigmath-stage.fly.dev/sessions/sess_02vjayEow5Iz22wIKXGJ6M")
        page.get_by_label("Name").click()
        page.get_by_label("Name").fill(username)
        page.get_by_role("button", name="Submit").click()

    # ---------------------
    
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
