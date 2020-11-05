#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import skfuzzy as fuzz
import skfuzzy.membership as mf
import matplotlib.pyplot as plt


# In[45]:


x_bodytemp = np.arange(20, 50 , 1)
x_respiratory = np.arange(0, 50 , 1)
x_pulse = np.arange(0, 150 , 1)
y_areacolour = np.arange(0, 4, 1)


# In[46]:


bodytemp_verylow = mf.trapmf(x_bodytemp, [-100, 0, 30, 34.5])
bodytemp_low = mf.trapmf(x_bodytemp, [0, 34.5, 35 ,36 ])
bodytemp_normal = mf.trimf(x_bodytemp, [36, 36.5, 37])
bodytemp_high = mf.trapmf(x_bodytemp, [36, 38, 41, 42])
bodytemp_veryhigh = mf.trapmf(x_bodytemp, [41, 42,45, 100])


# In[47]:


respiratory_low = mf.trimf(x_respiratory, [-100, 0, 12])
respiratory_normal = mf.trapmf(x_respiratory, [8, 12, 20, 24])
respiratory_high = mf.trimf(x_respiratory, [20, 50, 100])


# In[48]:


pulse_low = mf.trimf(x_pulse, [-100, 0, 60])
pulse_normal = mf.trapmf(x_pulse, [30, 60, 100, 120])
pulse_high = mf.trimf(x_pulse, [100, 150, 200])


# In[49]:


areacolour_green = mf.trimf(y_areacolour, [-1.2, 0, 1.2])
areacolour_yellow = mf.trimf(y_areacolour, [0.4, 1.5, 2.3])
areacolour_red= mf.trimf(y_areacolour, [1.8, 3, 5]) 


# In[54]:


fig, (ax0, ax1, ax2) = plt.subplots(nrows = 3, figsize =(6, 10))
ax0.plot(x_bodytemp, bodytemp_verylow, 'd', linewidth = 2, label = 'VERY LOW')
ax0.plot(x_bodytemp, bodytemp_low, 'r', linewidth = 2, label = 'LOW')
ax0.plot(x_bodytemp, bodytemp_normal, 'g', linewidth = 2, label = 'NORMAL')
ax0.plot(x_bodytemp, bodytemp_high, 'b', linewidth = 2, label = 'HIGH')
ax0.plot(x_bodytemp, bodytemp_veryhigh, 'c', linewidth = 2, label = ' VERY HIGH')
ax0.set_title('BODY TEMPERATURE')
ax0.legend()

ax0.plot(x_respiratory, respiratory_low, 'r', linewidth = 2, label = 'LOW')
ax0.plot(x_respiratory, respiratory_normal, 'g', linewidth = 2, label = 'NORMAL')
ax0.plot(x_respiratory, respiratory_high, 'b', linewidth = 2, label = 'HIGH')

ax0.set_title('RESPİRATORY')
ax0.legend()

fig, (ax0, ax1, ax2) = plt.subplots(nrows = 3, figsize =(6, 10))

ax0.plot(x_pulse, pulse_low, 'r', linewidth = 2, label = 'LOW')
ax0.plot(x_pulse, pulse_normal, 'g', linewidth = 2, label = 'NORMAL')
ax0.plot(x_pulse, pulse_high, 'b', linewidth = 2, label = 'HIGH')

ax0.set_title('pulse')
ax0.legend()
plt.tight_layout()

input_bodytemp = 40
input_pulse= 75


# In[ ]:





# In[55]:


bodytemp_fit_verylow = fuzz.interp_membership(x_bodytemp, bodytemp_verylow, x_bodytemp)
bodytemp_fit_low = fuzz.interp_membership(x_bodytemp, bodytemp_low,x_bodytemp)
bodytemp_fit_normal = fuzz.interp_membership(x_bodytemp, bodytemp_normal, x_bodytemp)
bodytemp_fit_high = fuzz.interp_membership(x_bodytemp, bodytemp_high, x_bodytemp)
bodytemp_fit_veryhigh = fuzz.interp_membership(x_bodytemp, bodytemp_veryhigh, x_bodytemp)


# In[56]:


respiratory_fit_low = fuzz.interp_membership(x_respiratory, respiratory_low, x_respiratory)
respiratory_fit_normal = fuzz.interp_membership(x_respiratory, respiratory_normal, x_respiratory)
respiratory_fit_high = fuzz.interp_membership(x_respiratory, respiratory_high, x_respiratory)


# In[57]:


pulse_fit_low = fuzz.interp_membership(x_pulse, pulse_low, x_pulse)
pulse_fit_normal = fuzz.interp_membership(x_pulse, pulse_normal, x_pulse)
pulse_fit_high = fuzz.interp_membership(x_pulse,pulse_high, x_pulse)


# In[58]:


rule1 = np.fmin(np.fmin(bodytemp_fit_verylow, respiratory_fit_low, pulse_fit_low), areacolour_red)
rule2 = np.fmin(np.fmin(bodytemp_fit_verylow, respiratory_fit_low, pulse_fit_normal), areacolour_red)
rule3 = np.fmin(np.fmax(bodytemp_fit_verylow, respiratory_fit_low, pulse_fit_high), areacolour_red)
rule4 = np.fmin(np.fmax(bodytemp_fit_verylow, respiratory_fit_normal, pulse_fit_lowhigh), areacolour_red)
rule5 = np.fmin(np.fmax(bodytemp_fit_verylow, respiratory_fit_normal, pulse_fit_normal), areacolour_yellow)
rule6 = np.fmin(np.fmax(bodytemp_fit_verylow, respiratory_fit_normal, pulse_fit_high), areacolour_red)
rule7 = np.fmin(np.fmax(bodytemp_fit_verylow, respiratory_fit_high, pulse_fit_low), areacolour_red)
rule8 = np.fmin(np.fmax(bodytemp_fit_verylow, respiratory_fit_high, pulse_fit_normal), areacolour_red)
rule9 = np.fmin(np.fmax(bodytemp_fit_verylow, respiratory_fit_high, pulse_fit_high), areacolour_red)

rule10 = np.fmin(np.fmin(bodytemp_fit_low, respiratory_fit_low, pulse_fit_low), areacolour_red)
rule11 = np.fmin(np.fmin(bodytemp_fit_low, respiratory_fit_low, pulse_fit_normal), areacolour_red)
rule12 = np.fmin(np.fmax(bodytemp_fit_low, respiratory_fit_low, pulse_fit_high), areacolour_red)
rule13 = np.fmin(np.fmax(bodytemp_fit_low, respiratory_fit_normal, pulse_fit_lowhigh), areacolour_red)
rule14 = np.fmin(np.fmax(bodytemp_fit_low, respiratory_fit_normal, pulse_fit_normal), areacolour_green)
rule15 = np.fmin(np.fmax(bodytemp_fit_low, respiratory_fit_normal, pulse_fit_high), areacolour_red)
rule16 = np.fmin(np.fmax(bodytemp_fit_low, respiratory_fit_high, pulse_fit_low), areacolour_red)
rule17 = np.fmin(np.fmax(bodytemp_fit_low, respiratory_fit_high, pulse_fit_normal), areacolour_red)
rule18 = np.fmin(np.fmax(bodytemp_fit_low, respiratory_fit_high, pulse_fit_high), areacolour_red)

rule19 = np.fmin(np.fmin(bodytemp_fit_normal, respiratory_fit_low, pulse_fit_low), areacolour_red)
rule20 = np.fmin(np.fmin(bodytemp_fit_normal, respiratory_fit_low, pulse_fit_normal), areacolour_yellow)
rule21 = np.fmin(np.fmax(bodytemp_fit_normal, respiratory_fit_low, pulse_fit_high), areacolour_green)
rule22 = np.fmin(np.fmax(bodytemp_fit_normal, respiratory_fit_normal, pulse_fit_lowhigh), areacolour_yellow)
rule23 = np.fmin(np.fmax(bodytemp_fit_normal, respiratory_fit_normal, pulse_fit_normal), areacolour_green)
rule24 = np.fmin(np.fmax(bodytemp_fit_normal, respiratory_fit_normal, pulse_fit_high), areacolour_red)
rule25 = np.fmin(np.fmax(bodytemp_fit_normal, respiratory_fit_high, pulse_fit_low), areacolour_red)
rule26 = np.fmin(np.fmax(bodytemp_fit_normal, respiratory_fit_high, pulse_fit_normal), areacolour_yellow)
rule27 = np.fmin(np.fmax(bodytemp_fit_normal, respiratory_fit_high, pulse_fit_high), areacolour_red)

rule28 = np.fmin(np.fmin(bodytemp_fit_high, respiratory_fit_low, pulse_fit_low), areacolour_red)
rule29 = np.fmin(np.fmin(bodytemp_fit_high, respiratory_fit_low, pulse_fit_normal), areacolour_red)
rule30 = np.fmin(np.fmax(bodytemp_fit_high, respiratory_fit_low, pulse_fit_high), areacolour_red)
rule31 = np.fmin(np.fmax(bodytemp_fit_high, respiratory_fit_normal, pulse_fit_lowhigh), areacolour_red)
rule32 = np.fmin(np.fmax(bodytemp_fit_high, respiratory_fit_normal, pulse_fit_normal), areacolour_green)
rule33 = np.fmin(np.fmax(bodytemp_fit_high, respiratory_fit_normal, pulse_fit_high), areacolour_yellow)
rule34 = np.fmin(np.fmax(bodytemp_fit_high, respiratory_fit_high, pulse_fit_low), areacolour_red)
rule35 = np.fmin(np.fmax(bodytemp_fit_high, respiratory_fit_high, pulse_fit_normal), areacolour_red)
rule36 = np.fmin(np.fmax(bodytemp_fit_high, respiratory_fit_high, pulse_fit_high), areacolour_red)

rule37 = np.fmin(np.fmin(bodytemp_fit_veryhigh, respiratory_fit_low, pulse_fit_low), areacolour_red)
rule38 = np.fmin(np.fmin(bodytemp_fit_veryhigh, respiratory_fit_low, pulse_fit_normal), areacolour_red)
rule39 = np.fmin(np.fmax(bodytemp_fit_veryhigh, respiratory_fit_low, pulse_fit_high), areacolour_red)
rule40 = np.fmin(np.fmax(bodytemp_fit_veryhigh, respiratory_fit_normal, pulse_fit_lowhigh), areacolour_red)
rule41 = np.fmin(np.fmax(bodytemp_fit_veryhigh, respiratory_fit_normal, pulse_fit_normal), areacolour_yellow)
rule42 = np.fmin(np.fmax(bodytemp_fit_veryhigh, respiratory_fit_normal, pulse_fit_high), areacolour_red)
rule43 = np.fmin(np.fmax(bodytemp_fit_veryhigh, respiratory_fit_high, pulse_fit_low), areacolour_red)
rule44 = np.fmin(np.fmax(bodytemp_fit_veryhigh, respiratory_fit_high, pulse_fit_normal), areacolour_red)
rule45 = np.fmin(np.fmax(bodytemp_fit_veryhigh, respiratory_fit_high, pulse_fit_high), areacolour_red)


# In[59]:


out_red = np.fmax(rule1, rule2, rule3, rule4, rule6, rule7, rule8, rule9, rule10,, rule11, ruke12, rule13, rule15, rule16, rule17, rule18, rule18, rule19, rule21, rule24, rule25, rule27, rule28, rule29, rule30, rule31, rule34, rule35, rule36, rule37, rule38, rule39, rule40, rule42, rule43, rule44, rule45) 
out_green = np.fmax(rule32, rule23, rule14)
out_yellow = np.fmax(rule33, rule41, rule26, rule22, rule20, rule5)




# In[35]:


out_areacolour = np.fmax(out_green, out_red, out_yellow)

defuzzified = fuzz.defuzz(y_areacolour, out_areacolour, 'centroid')

result = fuzz.interp_membership(y_areacolour, out_areacolour, defuzzified)


# In[36]:


print("Area Colour: ", defuzzified)


# In[ ]:




