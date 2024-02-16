from playwright.sync_api import sync_playwright

def navigate_and_show_something(page, url):
    page.goto(url)
    # Here you can perform some actions or demonstrate something cool on the page
    # For demonstration purposes, let's just take a screenshot
    page.screenshot(path=f'{url.replace("https://", "").replace("/", "_")}.png')

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    try:
        # Try navigating to YouTube
        navigate_and_show_something(page, 'https://huggingface.co/archaic-group')
    except Exception as e:
        print(f"An error occurred while navigating to YouTube: {e}")
        # If YouTube isn't accessible, let's try another page
        try:
            navigate_and_show_something(page, 'https://example.com')
        except Exception as e:
            print(f"An error occurred while navigating to Example.com: {e}")
            # If both YouTube and Example.com are inaccessible, you can handle it further here

    # Close the page
    page.close()
    
    # Close the browser
    browser.close()
