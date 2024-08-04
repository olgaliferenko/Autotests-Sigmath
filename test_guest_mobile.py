import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://sigmath-stage.fly.dev/sessions/sess_02wJ6DT6jQb4jStuSH3EdL")
    page.get_by_label("Name").click()
    page.get_by_label("Name").fill("Olga.test")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Rotate your device for best")).to_be_visible()
