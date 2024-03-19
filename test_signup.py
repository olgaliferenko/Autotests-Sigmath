from playwright.sync_api import Playwright, sync_playwright, expect

from random import choice
from string import ascii_uppercase
random_part = ''.join(choice(ascii_uppercase) for i in range(12))
email = f'klara_{random_part}@test.com'

def run_signup(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://sigmath-stage.fly.dev/")
    page.get_by_role("link", name="Log in").click()
    page.get_by_label("Email").click()
    page.get_by_role("link", name="Sign up").click()
    page.get_by_label("Name").click()
    page.get_by_label("Name").fill("Klaaaaaaalllllllrrrrrrraaaaaaa")

    page.get_by_label("Email").click()

    print(email)

    page.get_by_label("Email").fill(email)
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("123456789")
    page.get_by_role("button", name="Create an account").click()
    expect(page.get_by_text("There is an onboarding")).to_be_visible()
    page.screenshot(path= f"screenshot_{email}.png")
    expect(page.get_by_role("link", name="Your profile")).to_be_visible()
    expect(page.get_by_role("link", name="Log out")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()

#TODO:
#1 poprobovat avtopizaciu cherez -> https://playwright.dev/python/docs/next/network#http-authentication 
    

def run_signin(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("https://sigmath-stage.fly.dev/")
    page.get_by_role("link", name="Log in").click()
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill(email)
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("123456789")
    page.get_by_label("Keep me logged in").check()
    page.get_by_role("button", name="Sign in").click()


with sync_playwright() as playwright:
    run_signup(playwright)
    run_signin(playwright)

