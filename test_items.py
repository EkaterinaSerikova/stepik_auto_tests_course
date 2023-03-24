import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_visibility(browser):
    try:
        browser.get(link)
        time.sleep(30)
        button = browser.find_element_by_css_selector("button.btn:nth-child(3)")
        assert button.is_displayed()
        return True
    except:
        return False
