def click_btn(driver, indentifier):
    next_btn = driver.find_element_by_css_selector(indentifier)
    next_btn.click()

def insert_into_field(driver, indentifier, data):
    field = driver.find_element_by_css_selector(indentifier)
    field.send_keys(data)