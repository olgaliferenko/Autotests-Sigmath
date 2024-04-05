import time
from playwright.sync_api import Playwright, sync_playwright, expect

#TODO : 


# - posle 10 userA ne pokasivaet ih na stranice session
# - na usere 2 i 4 otkluchilsa screenshare
# - proverit na rasnoi shirine ekrana

# - for every guest set new country
# - add screenshot for every size

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    screens={
        "mobile": {
            "M": {"width": 360, "height": 740}, 
            "L": {"width": 2176, "height": 1812}
        },
        "desctop": {
            "M": {"width": 1366, "height": 768}, 
            "L": {"width": 1920, "height": 1080}
        }
    }
    screen_list = [
        screens["mobile"]["L"], 
        screens["desctop"]["M"],
        screens["desctop"]["L"],
        screens["mobile"]["M"], 
    ]
    #screen_list refactor

    context = browser.new_context()

    #user 1
    list_of_numbers = range(0, 3, 1)

    for index in list_of_numbers:
        username = f'user {index}'
        page = context.new_page()
        page.set_viewport_size(screen_list[index])
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
