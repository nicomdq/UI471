from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    # Assess - Given
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to website https://symonstorozhenko.wixsite.com/website-1
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)
    page.wait_for_load_state("networkidle")

    # Act - When/And
    # Add first product
    page.get_by_role("link", name="Shoes Shoes").click()
    page.locator(
        "div:nth-child(2) > .CoreRadioButton848120068__icon > .CorePopover1561687578__root > .CorePopover1561687578__popoverElement > .ColorPickerItem3151989514__radioOuter > .ColorPickerItem3151989514__radioInner").click()
    page.get_by_role("button", name="Add to Cart").click()

    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    # Add second product
    page.get_by_role("link", name="Button-Up T-Shirt Button-Up T-Shirt Best Seller").click()
    page.locator(
        "div:nth-child(2) > .CoreRadioButton848120068__icon > .CorePopover1561687578__root > .CorePopover1561687578__popoverElement > .ColorPickerItem3151989514__radioOuter > .ColorPickerItem3151989514__radioInner").click()
    page.get_by_role("button", name="Add to Cart").click()

    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    # Assert - Then
    # Verify that the products have been successfuly added to Cart
    page.goto("https://symonstorozhenko.wixsite.com/website-1/cart-page")
    expect(page.get_by_text("Shoes")).to_be_visible()
    expect(page.get_by_text("Button-Up T-Shirt")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
