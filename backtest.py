import pyupbit
import numpy as np

df = pyupbit.get_ohlcv("KRW-BTC", count=7)
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

fee = 0.05
# ror(수익율), np.where(조건문, 참일때 값, 거짓일때 값)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target']-fee,
                     2)
# 누적곱 계산 (cumprod) => hpr (누적 수익률)
df['hpr'] = df['ror'].cumprod()
# 하락폭(Draw Down) 계산 ==> 누적 최대 값과 현재 hpr 차이 / 누적 최대값 x 100
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")