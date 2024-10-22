#Imports and definitions
from smartmca import SmartMCA
from smartmca import ConfigMCA, ConfigAnalog, ConfigDigitalIO, ConfigAcquisition
import numpy as np 
from matplotlib import pyplot as plt
import time
from scipy.optimize import curve_fit 

def gauss(x, H, A, x0, sigma): 
    return H + A * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))
    
#Connection to the server 
mca = SmartMCA()
mca.connect("http://127.0.0.1", "user", "password")
mca.get_server_status()
#Get all parameters configurations
config = mca.get_mca_configuration()
print(config)
config_analog = mca.get_analog_configuration()
print(config_analog)
config_digital = mca.get_digital_io_configuration()
print(config_digital)
config_acquisition = mca.get_acquisition_configuration()
print(config_acquisition)
config_scope = mca.get_oscilloscope_configuration()
print(config_scope)
mca.reset_statistics()

#get scope data and plot the analog trace
y= mca.oscilloscope_get_data(enable_trace_processing=False)
plt.figure(0)
plt.plot(y.channels[0].analog)
plt.savefig('wave.png')

#Start energy histogram acquisition
mca.histogram_reset(type=ConfigAcquisition.SpectrumType.ENERGY)
mca.histogram_start(type=ConfigAcquisition.SpectrumType.ENERGY)
#30s acquisition
time.sleep(30)
#Stop energy histogram acquisition
mca.histogram_stop(type=ConfigAcquisition.SpectrumType.ENERGY)
#Get energy histogram and statistics
y_data, counts = mca.histogram_get(type=ConfigAcquisition.SpectrumType.ENERGY,rebin=2048)
time.sleep(1)
stats = mca.get_mca_statistics()
print(stats)
#Plot energy histogram and execute a Gaussian fit
plt.figure(1)
plt.plot(y_data)
x = np.arange(0, 2048, 1) 
parameters, covariance = curve_fit(gauss, x[1250:1700], y_data[1250:1700], p0=[0,50,1550,20]) 
y_fit = gauss(x, parameters[0], parameters[1], parameters[2], parameters[3]) 
plt.plot(x[0:2000], y_fit[0:2000], c='r', label='Best fit') 
print(parameters) 
print(covariance) 
print(counts)
plt.savefig('hist.png')
plt.show()