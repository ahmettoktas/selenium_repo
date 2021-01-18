from selenium.webdriver.common.by import By


class Facebook:
    website_link = 'https://www.facebook.com/'
    sign_up = (By.ID, 'u_0_2')


class Google:
    website_link = 'https://www.google.com/'
    search_bar = (By.NAME, 'q')
    search_button = (By.CLASS_NAME, 'gNO89b')
    text = 'Hellokitty'


class Amazon:
    website_link = 'https://www.amazon.com/'
    search_bar = (By.ID, 'twotabsearchtextbox')
    search_button = (By.ID, 'nav-search-submit-button')
    text = 'Hellokitty '
