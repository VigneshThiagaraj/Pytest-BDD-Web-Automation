from pytest_bdd import scenarios, given, when, then, parsers
from pages.search_products import SearchProducts
scenarios('../features/searchProducts.feature')


@when(parsers.parse('I enter the product name to be searched as "{searchtext}"'))
def search_product(driver, searchtext):
    SearchProducts(driver).enter_product_name(searchtext)
    SearchProducts(driver).click_search_btn()


@then(parsers.parse('I verify the search result'))
def verify_search_product(driver):
    SearchProducts(driver).verify_search_result_list()
