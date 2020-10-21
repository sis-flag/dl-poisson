# !python3
# coding: utf-8
# author: sis-flag

import os
import pickle
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

with open(os.path.join("..", "exp", "sin_N", "data.pkl"), "rb") as f:
    R1 = pickle.load(f)
with open(os.path.join("..", "exp", "sin_M", "data.pkl"), "rb") as f:
    R2 = pickle.load(f)
with open(os.path.join("..", "exp", "sin_M1", "data.pkl"), "rb") as f:
    R3 = pickle.load(f)
    
plt.figure()
plt.semilogy(R1["error"], label="Normal")
plt.semilogy(R2["error"], label="Mscale")
plt.semilogy(R3["error"], label="Noscale")
plt.legend(fontsize=14)
plt.show()
    
for k in [0, 500, 1000, 5000]:
    plt.figure()
    plt.plot(R2["x_samp"], R2["u_samp_"+str(k)], 'r--')
    plt.plot(R2["x_samp"], R2["u_samp_true"], 'b-')
    plt.show()
