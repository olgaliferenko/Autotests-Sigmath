import time
from playwright.sync_api import Playwright, sync_playwright, expect

#TODO : 
#  -posledti user ne uhodit from session
# - vikidivaet from session teh, kto bil tam (na usere 10 iz 11)
# - posle 10 userA ne pokasivaet ih na stranice session
# - na usere 2 i 4 otkluchilsa screenshare
# - proverit na rasnoi shirine ekrana
# - proverit https://sigmath.org/users/log_in
# - proverit https://sigmath.org/users/register

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    #user 1
    list_of_numbers = range(1, 4, 1)

    for index in list_of_numbers:
        username = f'user {index}'
        page = context.new_page()
        page.goto("https://sigmath-stage.fly.dev/sessions/sess_02vjayEow5Iz22wIKXGJ6M")
        page.get_by_label("Name").click()
        page.get_by_label("Name").fill(username)
        page.get_by_role("button", name="Submit").click()

    # ---------------------
    time.sleep(5)
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
