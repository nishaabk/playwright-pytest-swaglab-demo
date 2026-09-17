from Locators.locators import CartLocators
class CartPage:
    def __init__(self, page):
        self.page = page
    def add_product(self, product_name):
        self.page.locator(CartLocators.INVENTORY_ITEM).filter(has_text=product_name).get_by_role("button", name=CartLocators.ADD_TO_CART).click()
    def remove_product(self, product_name):
        self.page.locator(CartLocators.CART_ITEM).filter(has_text=product_name).get_by_role("button", name=CartLocators.REMOVE_BUTTON).click()

    def add_multiple_products(self, products):
        for product in products:
            self.add_product(product)

    def remove_multiple_products(self, products):
        for product in products:
            self.remove_product(product)

    def sort_products(self, sort_option):
        self.page.locator(CartLocators.SORT_DROPDOWN).select_option(label=sort_option)

    def open_cart(self):
        self.page.locator(CartLocators.CART_LINK).click()

    def is_product_present(self, product_name):
        return (self.page.locator(CartLocators.CART_ITEM).filter(has_text=product_name).count() > 0 )