from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage

class ProductPage(BasePage):

    # Locators
    _nome_produto = {'by': AppiumBy.ID, 'value': 'com.saucelabs.mydemoapp.android:id/productTV'}
    _preco_produto = {'by': AppiumBy.ID, 'value': 'com.saucelabs.mydemoapp.android:id/priceTV'}
    _origem_x = 927
    _origem_Y = 2073
    _destino_x = 967
    _destino_y = 1313
    _red_color = '(//android.widget.ImageView[@content-desc=\"Displays color of product\"])[4]'
    _color_image_view = {'by': AppiumBy.XPATH, 'value': _red_color }
    _aumentar_quantidade = {'by': AppiumBy.ACCESSIBILITY_ID 'value': 'Increases number of products'}
    _adicionar_carrinho = {'by': AppiumBy.ACCESSIBILITY_ID 'value': 'Tap to add product to cart'}


    # Inicialização
    def __init__(self, driver):
        self.driver =  driver

    # Ação
    # Ler o nome e o preço do produto
    def ler_nome(self):
        return self._ler(self._nome_produto)

    def ler_preco(self):
        return  self._ler(self._preco_produto)

    # Arrasta para cima
    def arrastar_para_cima(self):
        self._rolar(
            self._origem_x,
            self._origem_Y,
            self._destino_x,
            self._destino_y
        )

    # Realizar o fluxo de escolhas da compra
    def como_(self):
        # Selecionar a cor da mochila como vermelha
        self._apertar(self._color_image_view)

        # Clicar até selecionar a quantidade desejada
        for itens in range(quantidade -1):
            self._apertar(self._aumentar_quantidade)

        # Adicionar produto no carrinho
        self._apertar(self._adicionar_carrinho)