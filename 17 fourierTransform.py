import numpy as np
import matplotlib.pyplot as plotter
# How many time points are needed 
sampling_frequency   = 100;
# At what intervals time points are sampled
sampling_interval       = 1 / sampling_frequency;
# Begin time period of the signals
begin_time           = 0;
# End time period of the signals
end_time             = 10; 
# Frequency of the signals
signal1_frequency     = 4;
signal2_frequency     = 7;
# Time points
time        = np.arange(begin_time, end_time, sampling_interval);
# Create two sine waves
amplitude1 = np.sin(2*np.pi*signal1_frequency*time)
amplitude2 = np.sin(2*np.pi*signal2_frequency*time)
# Create subplot
figure, axis = plotter.subplots(4, 1)
plotter.subplots_adjust(hspace=1)
# Time domain representation for sine wave 1
axis[0].set_title('Sine wave with a frequency of 4 Hz')
axis[0].plot(time, amplitude1)
axis[0].set_xlabel('Time')
axis[0].set_ylabel('Amplitude')
# Time domain representation for sine wave 2
axis[1].set_title('Sine wave with a frequency of 7 Hz')
axis[1].plot(time, amplitude2)
axis[1].set_xlabel('Time')
axis[1].set_ylabel('Amplitude')
# Add the sine waves
amplitude = amplitude1 + amplitude2
# Time domain representation of the resultant sine wave
axis[2].set_title('Sine wave with multiple frequencies')
axis[2].plot(time, amplitude)
axis[2].set_xlabel('Time')
axis[2].set_ylabel('Amplitude')
# Frequency domain representation
fourier_transform = np.fft.fft(amplitude)/len(amplitude)           # Normalize amplitude
fourier_transform = fourier_transform[range(int(len(amplitude)/2))] # Exclude sampling frequency
tpCount     = len(amplitude)
values      = np.arange(int(tpCount/2))
time_period  = tpCount/sampling_frequency
frequencies = values/time_period
# Frequency domain representation
axis[3].set_title('Fourier transform depicting the frequency components')
axis[3].plot(frequencies, abs(fourier_transform))
axis[3].set_xlabel('Frequency')
axis[3].set_ylabel('Amplitude')
plotter.show()
