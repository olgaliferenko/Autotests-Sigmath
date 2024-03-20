import time
from playwright.sync_api import Playwright, sync_playwright, expect

#TODO :
# - for every guest set new country
# - check that RU sees notification


def run(playwright: Playwright) -> None:
    # find free proxy in Google and add it here
    proxy_serbia = "217.26.67.57:3180"
    proxy_ukraina = "31.43.158.108:8888"
    proxy_ru = "82.146.45.136:3128"

    browser = playwright.firefox.launch(proxy={"server": proxy_ru})

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
   

with sync_playwright() as playwright:
    run(playwright)