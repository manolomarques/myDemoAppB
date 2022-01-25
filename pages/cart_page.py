from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class CartPage(BasePage):
    # localizadores
    _icone_carrinho = {'by': AppiumBy.ID, 'value': 'com.saucelabs.mydemoapp.android:id/cartTV'}
    #_titulo_tela = {'by': AppiumBy.ID, 'value': 'com.saucelabs.mydemoapp.android:id/productTV'}
    _titulo_produto = {'by': AppiumBy.ID, 'value': 'com.saucelabs.mydemoapp.android:id/titleTV'}
    _preco_produto = {'by': AppiumBy.ID, 'value': 'com.saucelabs.mydemoapp.android:id/priceTV'}
    _preco_total = {'by': AppiumBy.ID, 'value': 'com.saucelabs.mydemoapp.android:id/totalPriceTV'}

    # Inicialização
    def __init__(self, driver):
        self.driver =  driver

    # Ação
    # Ir para carrinho
    def ir_para_o_carrinho_de_compras(self):
        self._apertar(self._icone_carrinho)


    # Ler dados do produto no carrinho
    def ler_dados_do_carrinho(self):
        dados = {
            '_titulo_produto': self._ler(self._titulo_produto),
            '_preco_produto': self._ler(self._preco_produto),
            '_preco_total': self._ler(self._preco_total)
        }
        return [dados['_titulo_produto'], dados['_preco_produto'], dados['_preco_total']]

