import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://sigmath-stage.fly.dev/sessions/sess_02vjayEow5Iz22wIKXGJ6M")
    page.get_by_label("Name").click()
    page.get_by_label("Name").fill("Olga.test")
    page.get_by_role("button", name="Submit").click()
    # Expect a title "to contain" a substring.
    expect(page.locator("#raise_a_hand-button")).to_be_visible()
    expect(page.locator("#stop-showing-member-cursors-button")).to_be_visible()

