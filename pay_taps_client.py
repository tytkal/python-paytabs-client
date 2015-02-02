from create_page_model import CreatePageModel

__author__ = 'tytkal'
from rest_client import RestClient
class PayTapsClient:
    username = ''
    password = ''
    res_client = None
    api_key = ''
    auth_url = 'authentication'
    create_pay_page = 'create_pay_page'
    valide_api_key = 'api_key_valid'
    verify_payment = 'verify_payment'
    expire_key = 'logout'
    def __init__(self):
        self.res_client = RestClient('https://www.paytabs.com/api/')
    def auth(self):
        params = {'merchant_id':self.username,'merchant_password':self.password}
        self.res_client.resourse = 'authentication'
        responce = self.res_client.post(params=params)
        api_key = responce.json()['api_key']
        if api_key == None:
            print 'password is wrong'
        else:
            self.api_key = api_key
            #print self.api_key
        return  self.api_key
    def validate_api_key(self):
        print ''

    def vrify_payment(self):
        print ''

    def expire_api_key(self):
        print ''

    def create_pay_page(self):
        cr_pa_mo = CreatePageModel()
        cr_pa_mo.api_key = self.auth()
        cr_pa_mo.title = 'testing'
        cr_pa_mo.address_shipping = 'nakil'
        print ''