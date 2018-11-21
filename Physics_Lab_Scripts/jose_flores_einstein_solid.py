"""

Created for Thermal Physics Homework
Name: Jose Flores
Date: Sunday November 13, 2016

"""
""" Depending on the version of Python you use, you might need to replace np.log to math.log """

######################### Modules ##########################

import numpy as np
import math
from math import factorial

######################### Number of Oscillators and Energy Units ######################

# ---Number of Oscillators for Einstein Solid A

n_A = 650.0

# ---Number of Oscillators for Einstein Solid B

n_B = 350.0

# ---Energy Units for Einstein Solid A
q_A = np.arange(201.0)
#print (q_A)

# ---Energy Units for Einstein Solid B
q_B = q_A[::-1.0]
#print (q_B)

################################### Calculations of Solids ##############################################


for i in q_A:

    # ---Multiplicity of Solid A
    omega_A = factorial(q_A[i] + n_A - 1.0) / (factorial(q_A[i]) * factorial(n_A - 1.0))
#    print ("%e"%(omega_A))

    # ---Multiplicity of Solid B
    omega_B = factorial(q_B[i] + n_B - 1.0) / (factorial(q_B[i]) * factorial(n_B - 1.0))
#    print ("%e"%(omega_B))

    # ---Total Multiplicity
    omega_tot = omega_A * omega_B
#    print ("Multi:", omega_tot, "q_A:", q_A[i])

    # ---Entropy (s) per Boltzman Constant (k) of Solid A
    s_per_k_A = math.log(omega_A)
#    print ("S_A/k:" , s_per_k_A, "q_A:" ,q_A[i])

    # ---Entropy (s) per Boltzman Constant (k) of Solid B
    s_per_k_B = math.log(omega_B)
#    print ("S_B/k:", s_per_k_B, "q_B:" ,q_B[i])

 # ---Total Entropy (s) per Boltzman Constant (k)
    s_per_k_tot = math.log(omega_tot)
    print ("S_tot/k:", s_per_k_tot, "q_A:", q_A[i])
