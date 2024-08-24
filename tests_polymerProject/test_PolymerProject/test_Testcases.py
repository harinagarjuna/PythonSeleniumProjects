import time
import pytest
from tests_parabank.utilities.actionutilities import ActionUtilities
from tests_parabank.utilities.utils import BasicUtils
from tests_polymerProject.constants.basiconstants import BaseConstants
from tests_polymerProject.pageObjects.cartPage import CartPage
from tests_polymerProject.pageObjects.checkoutPage import CheckOutPage
from tests_polymerProject.pageObjects.completepage import CompletePage
from tests_polymerProject.pageObjects.landingPage import LandingPage
from tests_polymerProject.pageObjects.menswear import MenswearPage
from tests_polymerProject.pageObjects.productPage import ProductPage



@pytest.mark.usefixtures('ch_driver')
def test_landingpage_Menswear(ch_driver):
   dr = ch_driver
   BSObject = BaseConstants()
   dr.get(BSObject.base_url)
   time.sleep(5)
   landing_page = LandingPage(dr)
   landing_page.click_on_menswear_link()

@pytest.mark.usefixtures('ch_driver')
def test_click_on_product(ch_driver):
    dr = ch_driver
    BSObject = BaseConstants()
    dr.get(BSObject.base_url)
    time.sleep(5)
    landing_page = LandingPage(dr)
    landing_page.click_on_menswear_link()
    menswear = MenswearPage(dr)
    menswear.click_youtube_shirt()
    assert dr.current_url == "https://shop.polymer-project.org/detail/mens_outerwear/YouTube+Ultimate+Hooded+Sweatshirt", "Wrong Page"


# def test_addproducttocartandcheckout():
#     driver = BSObject.get_driver(browser="chrome")
#     dr = driver.__next__()
#     dr.get(BSObject.base_url)
#     time.sleep(5)
#     landing_page = LandingPage(dr)
#     landing_page.click_on_menswear_link()
#     menswear = MenswearPage(dr)
#     menswear.click_youtube_shirt()
#     time.sleep(3)
#     product_page = ProductPage(dr)
#     assert "YouTube" in product_page.get_product_title().text
#     assert product_page.get_product_price().text == '$32.35'
#     product_page.select_product_size("L")
#     product_page.select_quantity("2")
#     product_page.add_cart_button().click()
#     util = BasicUtils(dr)
#     util.get_cart().click()
#     time.sleep(3)
#     cartpage = CartPage(dr)
#     cartpage.click_checkout()
#     time.sleep(5)
#     assert BSObject.check_out_url == dr.current_url

@pytest.mark.usefixtures('ch_driver')
def test_select_product(ch_driver):
    dr = ch_driver
    action_utils = ActionUtilities()
    action_utils.click_on_a_product(dr)
    product_page = ProductPage(dr)
    assert "YouTube" in product_page.get_product_title().text
    assert product_page.get_product_price().text == '$32.35'

@pytest.mark.usefixtures('ch_driver')
def test_select_a_product_checkout(ch_driver):
    dr = ch_driver
    BSObject = BaseConstants()
    actionutil = ActionUtilities()
    actionutil.select_a_product(dr,"XL","3")
    util = BasicUtils(dr)
    util.click_cart()
    cartpage = CartPage(dr)
    cartpage.click_checkout()
    time.sleep(5)
    assert BSObject.check_out_url == dr.current_url


@pytest.mark.usefixtures('ch_driver')
def test_checkout(ch_driver):
    dr = ch_driver
    BSObject = BaseConstants()
    actionutil = ActionUtilities()
    checkout = CheckOutPage(dr)
    complete = CompletePage(dr)
    actionutil.select_a_product(dr,"XL","3")
    util = BasicUtils(dr)
    util.click_cart()
    cartpage = CartPage(dr)
    cartpage.click_checkout()
    time.sleep(5)
    assert BSObject.check_out_url == dr.current_url, "Not expected URL"
    assert checkout.get_CheckoutPageTitle().text == "Checkout", "Not Matching"
    checkout.enter_account_details(email="haritest@123.com",phone="1234567890")
    checkout.enter_shipping_details(address="123 street, down town",city="Toronto",state="Ontorio",zip="C1A505",shipping_country="CA")
    checkout.click_use_different_billing_checkbox()
    time.sleep(2)
    checkout.enter_billing_details(address="345 street, down town",city="Illinois",state="Texas",zip="516434",billing_country="US")
    checkout.enter_payment_details(name="HariCCTest",cnumber="123456789012345",expdate="08",expyear="2024",cvv="1234")
    checkout.get_place_order_button().click()
    time.sleep(4)
    assert "Thank" in complete.get_thanks_title().text
    assert "complete" in complete.get_confirmation().text
    #complete.get_finish_button().click()
    time.sleep(2)




















