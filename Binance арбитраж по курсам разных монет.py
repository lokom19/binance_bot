import threading
import time
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import time

api_key = 'GH0scoSIVmHoxBzMTVNwCeH2CfZqH3GU6o8mKrnECAcL8g13jQp34dSogOJMNNoS'
secret_key = 'Gv2grQ1F5KdkQFvu77HVx0a8r9DwPGU1ede6X9qrfteMzeF9Lmw2Bv0hwmTrNE75'
client = Client(api_key, secret_key)
position = 0
goods = []
first_price = 0


def check_working():
    global work
    global a
    end_price = 0
    time1 = time.time()
    for i in range(100):
        prices = client.get_order_book(symbol='MATICUSDT')
        a = float(prices['bids'][position][0])
        first_price = a
        #print(a)
        prices = client.get_order_book(symbol='MATICBTC')
        b = float(prices['bids'][position][0])
        #print(b)
        prices = client.get_order_book(symbol='BTCUSDT')
        c = float(prices['bids'][position][0])*b
        #print(c)
        #end = 1 / b * c
        end_price = end_price + c - first_price

        # print(end)
        # if (a < end):
        #     goods.append('Выиграл')
        # else:
        #     goods.append('Проигрыш')
    #print(goods)
    time_w = time.time() - time1
    #gg = goods.count('Выиграл')
    # print(gg)
    # print(f'Вероятность выигрыша {gg / len(goods)}')
    print(f'Заработок {end_price}')
    print(time_w)


check_working()

