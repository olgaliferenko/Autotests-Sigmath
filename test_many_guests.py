import time
from playwright.sync_api import Playwright, sync_playwright, expect

#TODO : 


# - posle 10 userA ne pokasivaet ih na stranice session
# - na usere 2 i 4 otkluchilsa screenshare
# - proverit na rasnoi shirine ekrana

# - for every guest set new country

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    #user 1
    list_of_numbers = range(1, 13, 1)

    for index in list_of_numbers:
        username = f'user {index}'
        page = context.new_page()
        page.on("request", lambda request: print(">>", request.method, request.url))
        page.on("response", lambda response: print("<<", response.status, response.url))
        page.goto("https://sigmath-stage.fly.dev/sessions/sess_02vjayEow5Iz22wIKXGJ6M")
        page.get_by_label("Name").click()
        page.get_by_label("Name").fill(username)
        page.get_by_role("button", name="Submit").click()

    # ---------------------
    time.sleep(5)
    context.close()
    browser.close()
    # Browser proxy option is required for Chromium on Windows.
# browser = chromium.launch(proxy={"server": "per-context"})
# context = browser.new_context(proxy={"server": "http://myproxy.com:3128"})


with sync_playwright() as playwright:
    run(playwright)
