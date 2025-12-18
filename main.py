class OrderSystem:
    def process(self, data, u_type, c_code):
        # 初始化總金額
        t = 0
        
        # 1. 計算總價與折扣邏輯
        if data:
            for i in data:
                if i['type'] == 'electronic':
                    if i['qty'] > 5:
                        t += i['price'] * i['qty'] * 0.9  # 電子產品大於5個打9折
                    else:
                        t += i['price'] * i['qty']
                elif i['type'] == 'clothing':
                    if c_code == 'SUMMER20':
                        t += i['price'] * i['qty'] * 0.8  # 夏日優惠
                    else:
                        t += i['price'] * i['qty']
                elif i['type'] == 'food':
                    t += i['price'] * i['qty']
                else:
                    print("Unknown type")
                    return
        else:
            print("No data")
            return

        # 2. 根據用戶類型計算運費
        shipping = 0
        if u_type == 1: # 1 代表 VIP
            if t > 1000:
                shipping = 0
            else:
                shipping = 100
        elif u_type == 2: # 2 代表 一般會員
            shipping = 150
        else:
            print("Invalid user")
            return

        # 3. 計算稅金 (5%)
        tax = t * 0.05
        
        # 4. 計算最終金額
        final = t + shipping + tax

        # 5. 輸出收據 (模擬資料庫儲存與 Email 發送)
        print("---------- RECEIPT ----------")
        print(f"Items Cost: {t}")
        print(f"Shipping: {shipping}")
        print(f"Tax: {tax}")
        print(f"Total: {final}")
        print("Saving to database...")
        print("Sending email to user...")
        print("-----------------------------")

        return final

# 測試用資料
items = [
    {'name': 'Laptop', 'type': 'electronic', 'price': 1000, 'qty': 1},
    {'name': 'T-Shirt', 'type': 'clothing', 'price': 200, 'qty': 3},
    {'name': 'Apple', 'type': 'food', 'price': 10, 'qty': 10}
]

# 呼叫
system = OrderSystem()
system.process(items, 1, 'SUMMER20')