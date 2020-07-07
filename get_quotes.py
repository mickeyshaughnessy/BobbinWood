from pyrh import Robinhood
from config import rh_username, rh_password

rh = Robinhood()
rh.login(username=rh_username, password=rh_password)

rh.print_quote('AAPL')

input()

rh.print_quotes(stocks=["BB", "FB", "MSFT"])

input()

quote_info = rh.quote_data('AAPL')
print(quote_info)
type(quote_info)
#print(rh.authenticated)
#print(rh.login_set)
#print(rh.token_expired)
print(rh.__dict__)
