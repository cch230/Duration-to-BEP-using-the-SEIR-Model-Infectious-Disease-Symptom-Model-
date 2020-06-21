import scipy.integrate as spi
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import math

# Initial conditions
# 인구수 51780579
S0 = 12900  # 타겟 시장 규모 (업체 개수
E0 = 7000  # 초기 광고노출 집단 개체수,초기 유저집단의 30퍼
I0 = 100  # 정식오픈시 초기 유저집단 개체 수(베타테스트를 통한 초기 유저 모집 수)
R0 = 0 # 지속적 사용자 집단 개체 수, 초기 유저집단의 28.5퍼

N= S0+E0+I0+R0 # 타겟 시장 규모
# Time vector
t = np.linspace(0, 60,60)#0~4년

N = S0 + I0 + R0  # 모집단  3,000,000

S0_ = S0/N
E0 = E0/N
I0 = I0/N
RO = R0/N


a = 0.3  # 접촉율 : 광고 접촉율
b = 0.15  # 전환율 : 광고를 보고 유저로 전환할 비율(여기가 중요)
c = 0.05  # 이환율 : 지속적 사용자 종료 비율
d= 0.7 # 한번사용후 이탈율
ramda= 0.5 #  사용자의 총 이탈율 0.715
beta= 0.075 # 지속적 사용 가능성 0.012825
sigma = b

Input = (S0_, E0, I0)

def SEIR(INT, t):
    '''The main set of equation'''
    Y = np.zeros((3))
    X = INT  # S0 = X[0], E = X[1], I0 = X[2]
    Y[0] = 0-beta*X[0]*X[2]
    Y[1] = beta * X[0] * X[2] - sigma * X[1] - c * X[1]
    Y[2] = sigma * X[1] - ramda * X[2]    # (이환 제외)

    return Y  # for spicy.odeint


t_start = 0.0
t_end = 3  # 5년
t_inc = 0.083  # 출시일부터 5년 경과시까지, 1달단위 변화율
t_range = np.arange(t_start, t_end + t_inc, t_inc)
SEIR = spi.odeint(SEIR, Input, t_range)

plt.axhline(y=600, color='k', label='Break-even point')
plt.plot(SEIR[:,2]*7000, '-r', label='User')
plt.grid()
plt.legend(loc=0)
plt.xlabel('Time(Months)')
plt.ylabel('Companies')
plt.show()