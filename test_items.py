import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_visibility(browser):
    try:
        browser.get(link)
        time.sleep(30)
        browser.find_element_by_css_selector("button.btn:nth-child(3)")
        return True
    except:
        return False
