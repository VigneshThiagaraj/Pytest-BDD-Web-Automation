from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
from .base_page import BasePage


class SearchProducts(BasePage, PageFactory):
    TXT_SEARCH = (By.XPATH, "//input[@id='twotabsearchtextbox01']")
    BTN_SEARCH = (By.XPATH, "//input[@id='nav-search-submit-button']")
    SEARCH_LIST = (By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
    """
    Locators = {
        "txt_search": >("XPATH", "//input[@id='twotabsearchtextbox']"),
        "btn_searchIcon": ("XPATH", "//input[@id='nav-search-submit-button']"),
        "btn_searchResult": ("XPATH", "//span[@class='a-size-medium a-color-base. a-text-normal']")
    }
    """

    def enter_product_name(self, product_name):
        #self.txt_username.set text(product name)
        self.enter_value(self.TXT_SEARCH, product_name)

    def click_search_btn(self):
        #self.btn_searchIcon.click button()
        self.click_element(self.BTN_SEARCH)

    def verify_search_result_list(self):
        for searchListProductName in self.find_list_webelement(self.SEARCH_LIST):
            print(searchListProductName.text)
