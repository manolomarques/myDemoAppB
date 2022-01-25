from appium.webdriver.common.appiumby import AppiumBy



class Mainpage(BasePage):
    # definir os localizadores / locators
    image_view_locator = '(//andoid.widget.ImageView[@content-desc=\"Displays selected product\"])[1]'
    _product_image_view = {'by': AppiumBy.XPATH, 'value': image_view_locator}

    #mapeariamos também os demais elementos

    # iniciarlização
    def __init__(self, driver):
        self.driver = driver

    # ações
    def selecionar_preimeiro_(self):
        self._apertar(self._product_image_view)

