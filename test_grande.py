from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
    permissions=["microphone","camera"],
    )

    page = context.new_page()
    page.goto("https://sigmath-stage.fly.dev/users/log_in")
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("olga.test@liferenko.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("Silvias15")
    page.get_by_role("button", name="Sign in").click()
    page1 = context.new_page()
    page1.goto("https://sigmath-stage.fly.dev/sessions/sess_02vjayEow5Iz22wIKXGJ6M")
    page1.get_by_role("button", name="Join live session").click()
    page1.wait_for_timeout(1000)
    page1.locator("#local-member-component path").first.click()
    expect(page1.locator("#local-member-component").get_by_role("img").first).to_be_visible()
    page1.locator("#local-member-component").get_by_role("img").nth(1).click()
    expect(page1.locator("#local-member-component path").nth(1)).to_be_visible()
    page1.locator("#local-member-component path").nth(1).click()
    expect(page1.locator("#local-member-component").get_by_role("img").nth(1)).to_be_visible()
    expect(page1.locator("#local-member-component").get_by_role("img").nth(2)).to_be_visible()
    page1.locator("#local-member-component").get_by_role("img").nth(2).click()
    expect(page1.locator("#local-member-component").get_by_role("img").nth(2)).to_be_visible()
    page1.locator("#local-member-component").get_by_role("img").nth(2).click()
    expect(page1.locator("#local-member-component").get_by_role("img").nth(2)).to_be_visible()
    #konec testa ekrana video mikrofona i ekrana

    expect(page1.get_by_role("button", name="Open options")).to_be_visible()
    page1.get_by_role("button", name="Open options").click()
    expect(page1.get_by_role("button", name="Save & exit")).to_be_visible()
    #proveril vidimist knopki (button)  "options"
    
    #nachinaetsa test button "hand"
    expect(page1.locator("#raise_a_hand-button")).to_be_visible()
    page1.locator("#raise_a_hand-button").click()
    expect(page1.locator("#put_hand_down-button")).to_be_visible()
    page1.locator("#put_hand_down-button").click()
    expect(page1.locator("#raise_a_hand-button")).to_be_visible()
    #end test "#raise_a_hand-button"
    
    page1.get_by_role("button", name="Open options").click()
    page1.get_by_role("button", name="Save & exit").click()
    expect(page1.get_by_text("Save session and exit? Yes,")).to_be_visible()
    page1.get_by_role("heading", name="Please share your feedback").click()
    expect(page1.locator("#feedback_msg")).to_be_visible()
    expect(page1.get_by_role("button", name="Send")).to_be_visible()
    expect(page1.get_by_role("button", name="Skip")).to_be_visible()
    page1.locator("#feedback_msg").click()
    page1.locator("#feedback_msg").fill("тест обратная связь")
    page1.get_by_role("button", name="Send").click()
    expect(page1.get_by_role("navigation")).to_contain_text("Home")

    
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
