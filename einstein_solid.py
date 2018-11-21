#Einstein Solid Script
#Plot the multiplicty of
#two Einstein solids with oscillators
#Nan Nb with Q units of energy,
#print entropy and muplicity
#at each q value and more

from decimal import Decimal
import math
import numpy as np
import matplotlib.pyplot as plt

def multiplicity(n,q):
    multiplicity = (math.factorial(q+n-1))/(math.factorial(q)*math.factorial(n-1))
    return multiplicity
    
#Set # oscillators, and energy
na = 650
nb = 350
q = 200

#Defining arrays for the increment of q
qa = np.array(range(q+1))
qb = np.array(sorted(range(q+1), reverse = True))

#Defining array for multiplicities
mult_tot = np.zeros(q+1)

############################### Calculations for the einstein solids #########################################
for i in range (q+1):
        mult_a = multiplicity(na,qa[i])
        mult_b = multiplicity(nb,qb[i])
        mult_tot[i] = mult_a*mult_b
        print 'qA ='+str(qa[i])+', qB='+str(qb[i])
        print 'Omega A = '+str('%.2E' % Decimal(mult_a))+', Omega B = '+str('%.2E' % Decimal(mult_b))
        print 'Entropy A = '+str("%0.02f" % math.log(mult_a))+'(S/k), Entropy B = '+str("%0.02f" % math.log(mult_b))+'(S/k)'
        print 'Omega Total = '+str('%.2E' % Decimal(mult_a+mult_b))+', Entropy Total = '+str("%0.02f" % (math.log(mult_a)+math.log(mult_b)))+'(S/k)'
        print '----------'

#Calculating all interesting sigma values
minimum = mult_tot[0]
maximum = max(mult_tot)
mult_tot_sum = np.sum(mult_tot)

#To get this element as an int, not annoying tuple all to find
#max multiplicity
q_max_holder = np.where(mult_tot == maximum)
qa_max = int(q_max_holder[0])
qb_max = q-qa_max

#Probablity of highest and lowest microstate
p_max = multiplicity(na,qa_max)*multiplicity(nb,qb_max)/mult_tot_sum
p_min = multiplicity(na,0)*multiplicity(nb,q)/mult_tot_sum

#Calculating highlight entropies i.e.ln(omega) (S/l) 
entropy_max = math.log(maximum)
entropy_min = math.log(minimum)
entropy_sum = math.log(mult_tot_sum)

################ Printing highlight values (muliplicites, probablitites, max/min and entropy) ################

#Printing highlight values to command line
print 'qA Max = ' +str(qa_max)+', qB Max = ' +str(qb_max)
print 'Omega Max = '+str('%.2E' % Decimal(maximum))
print 'Omega Min = '+str('%.2E' % Decimal(minimum))
print 'Omega Sum = '+str('%.2E' % Decimal(mult_tot_sum))
print 'Prob Max = '+str('%.2E' % Decimal(p_max*100))+' %'
print 'Prob Min = '+str('%.2E' % Decimal(p_min*100))+' %'
print 'Entropy Max = '+str('%0.02f' % Decimal(entropy_max))+' S/K'
print 'Entropy Min = '+str('%0.02f' % Decimal(entropy_min))+' S/K'
print 'Entropy Sum = '+str('%0.02f' % Decimal(entropy_sum))+' S/K'

######################## Plotting qA vs omega total, printing higihlight info to plot ########################

plt.plot(qa,mult_tot,'-b')
plt.title('Einstien Solid')
plt.xlabel('qA')
plt.ylabel('Multiplicty')

#To try and pretty up the display of text
#We are matching the order of magnitude of the max value so that our
#text displays nicely on any general plot
#i.e. 1.4e95 -->log = 95, 1.4e95/10^95 = 1.4,
#then take fractions of this number and mutliply back to the proper order of magnitude
#so that we are say 75% up on the y axis of this plot
#i.e. 0.75*1.4*10^95 would be top text value
log_q = int(math.log10(q))
log_max = int(math.log10(maximum))

#Form of arguments in plt.text is (x coordinate, y coordinate, string)
#Right of the plot
plt.text(0.80*(q/(math.pow(10,log_q)))*math.pow(10,log_q), 0.95*(maximum/(math.pow(10,log_max)))*math.pow(10,log_max), 'NA = ' +str(na))
plt.text(0.80*(q/(math.pow(10,log_q)))*math.pow(10,log_q), 0.85*(maximum/(math.pow(10,log_max)))*math.pow(10,log_max), 'NB = ' +str(nb))
plt.text(0.80*(q/(math.pow(10,log_q)))*math.pow(10,log_q), 0.75*(maximum/(math.pow(10,log_max)))*math.pow(10,log_max), 'q = ' +str(q))

#Left of the plot
plt.text(0.05*(q/(math.pow(10,log_q)))*math.pow(10,log_q), 0.95*(maximum/(math.pow(10,log_max)))*math.pow(10,log_max), 'qA Max = ' +str(qa_max))
plt.text(0.05*(q/(math.pow(10,log_q)))*math.pow(10,log_q), 0.85*(maximum/(math.pow(10,log_max)))*math.pow(10,log_max), 'qB Max = ' +str(qb_max))
plt.text(0.05*(q/(math.pow(10,log_q)))*math.pow(10,log_q), 0.75*(maximum/(math.pow(10,log_max)))*math.pow(10,log_max), 'Omega Max = '+str('%.2E' % Decimal(maximum)))
plt.text(0.05*(q/(math.pow(10,log_q)))*math.pow(10,log_q), 0.65*(maximum/(math.pow(10,log_max)))*math.pow(10,log_max), 'Omega Min = '+str('%.2E' % Decimal(minimum)))
plt.text(0.05*(q/(math.pow(10,log_q)))*math.pow(10,log_q), 0.55*(maximum/(math.pow(10,log_max)))*math.pow(10,log_max), 'Omega Sum = '+str('%.2E' % Decimal(mult_tot_sum)))

plt.text(0.05*(q/(math.pow(10,log_q)))*math.pow(10,log_q), 0.45*(maximum/(math.pow(10,log_max)))*math.pow(10,log_max), 'Prob Max = '+str('%.2E' % Decimal(p_max*100))+' %')
plt.text(0.05*(q/(math.pow(10,log_q)))*math.pow(10,log_q), 0.35*(maximum/(math.pow(10,log_max)))*math.pow(10,log_max), 'Prob Min = '+str('%.2E' % Decimal(p_min*100))+' %')

plt.text(0.05*(q/(math.pow(10,log_q)))*math.pow(10,log_q), 0.25*(maximum/(math.pow(10,log_max)))*math.pow(10,log_max), 'Entropy Max = '+str('%0.02f' % Decimal(entropy_max))+' S/K')
plt.text(0.05*(q/(math.pow(10,log_q)))*math.pow(10,log_q), 0.15*(maximum/(math.pow(10,log_max)))*math.pow(10,log_max), 'Entropy Min = '+str('%0.02f' % Decimal(entropy_min))+' S/K')
plt.text(0.05*(q/(math.pow(10,log_q)))*math.pow(10,log_q), 0.05*(maximum/(math.pow(10,log_max)))*math.pow(10,log_max), 'Entropy Sum = '+str('%0.02f' % Decimal(entropy_sum))+' S/K')

plt.show()
