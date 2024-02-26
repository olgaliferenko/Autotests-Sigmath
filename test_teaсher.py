import re
from playwright.sync_api import Page, expect

def test_login_and_save_settings(page: Page):
    page.goto("https://sigmath-stage.fly.dev/users/log_in")
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("olga.test@liferenko.com")
    page.get_by_label("Email").press("Tab")
    page.get_by_label("Password").fill("Silvias15")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("link", name="Sessions").click()
    page.get_by_text("Onboarding Session").click()
    page.get_by_role("button", name="Join live session").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Open options").click()
    page.get_by_role("button", name="Session Settings").click()
    page.get_by_role("button", name="Save Session").click()
    page.locator("#session-settings-modal-container").get_by_label("close").click()
    expect(page.get_by_text("Success! Settings updated")).to_be_visible()

