import pyupbit

access = "본인 값으로 변경"          # 본인 값으로 변경
secret = "본인 값으로 변경"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))
print(upbit.get_balance("KRW"))