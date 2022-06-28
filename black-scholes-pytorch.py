import torch 
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import numpy as np

sessions =  10000

spot_price = torch.tensor(3279.42)
strike_price = torch.tensor(3250)
call_option_price = torch.tensor(245.8)
input_option_price = torch.tensor(290.3)
option_price = torch.tensor([[call_option_price],[input_option_price]])

t = torch.tensor(1)
z = torch.randn(1, sessions)


def equ_error(params):

    drift, vol = params

    
    spot_price_t = torch.tensor(spot_price*torch.exp((drift-(vol*vol/2)*t+vol*torch.sqrt(t)*z)))
    call_option_est = torch.mean(torch.max((spot_price_t-strike_price), torch.tensor(0)))
    input_option_est = torch.mean(torch.max((strike_price-spot_price_t), torch.tensor(0)))
    option_est = torch.tensor([[call_option_est],[input_option_est]])
    error = torch.sqrt(torch.sum(torch.square(option_est-option_price)))
    return error

res = minimize(equ_error, np.array(torch.randn(2)), method='Nelder-Mead')


print(equ_error(res.x))
