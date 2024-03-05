from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    #user 1
    page = context.new_page()
    page.goto("https://sigmath-stage.fly.dev/sessions/sess_02vjayEow5Iz22wIKXGJ6M")
    page.get_by_label("Name").click()
    page.get_by_label("Name").fill("user 1")
    page.get_by_role("button", name="Submit").click()

    #user 2
    page2 = context.new_page()
    page2.goto("https://sigmath-stage.fly.dev/sessions/sess_02vjayEow5Iz22wIKXGJ6M")
    page2.get_by_label("Name").click()
    page2.get_by_label("Name").fill("user 2")
    page2.get_by_role("button", name="Submit").click() 

    #user 3
    page3 = context.new_page()
    page3.goto("https://sigmath-stage.fly.dev/sessions/sess_02vjayEow5Iz22wIKXGJ6M")
    page3.get_by_label("Name").click()
    page3.get_by_label("Name").fill("user 3")
    page3.get_by_role("button", name="Submit").click()

    #user 4
    page4 = context.new_page()
    page4.goto("https://sigmath-stage.fly.dev/sessions/sess_02vjayEow5Iz22wIKXGJ6M")
    page4.get_by_label("Name").click()
    page4.get_by_label("Name").fill("user 4")
    page4.get_by_role("button", name="Submit").click()

    #user 5
    page5 = context.new_page()
    page5.goto("https://sigmath-stage.fly.dev/sessions/sess_02vjayEow5Iz22wIKXGJ6M")
    page5.get_by_label("Name").click()
    page5.get_by_label("Name").fill("user 5")
    page5.get_by_role("button", name="Submit").click()

    #user 6
    page6 = context.new_page()
    page6.goto("https://sigmath-stage.fly.dev/sessions/sess_02vjayEow5Iz22wIKXGJ6M")
    page6.get_by_label("Name").click()
    page6.get_by_label("Name").fill("user 6")
    page6.get_by_role("button", name="Submit").click()

    #user 7
    page7 = context.new_page()
    page7.goto("https://sigmath-stage.fly.dev/sessions/sess_02vjayEow5Iz22wIKXGJ6M")
    page7.get_by_label("Name").click()
    page7.get_by_label("Name").fill("user 7")
    page7.get_by_role("button", name="Submit").click()

    #user 8
    page8 = context.new_page()
    page8.goto("https://sigmath-stage.fly.dev/sessions/sess_02vjayEow5Iz22wIKXGJ6M")
    page8.get_by_label("Name").click()
    page8.get_by_label("Name").fill("user 8")
    page8.get_by_role("button", name="Submit").click()

    #user 9
    page9 = context.new_page()
    page9.goto("https://sigmath-stage.fly.dev/sessions/sess_02vjayEow5Iz22wIKXGJ6M")
    page9.get_by_label("Name").click()
    page9.get_by_label("Name").fill("user 9")
    page9.get_by_role("button", name="Submit").click()

    #user 10
    page10 = context.new_page()
    page10.goto("https://sigmath-stage.fly.dev/sessions/sess_02vjayEow5Iz22wIKXGJ6M")
    page10.get_by_label("Name").click()
    page10.get_by_label("Name").fill("user 10")
    page10.get_by_role("button", name="Submit").click()
    # ---------------------
    
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
