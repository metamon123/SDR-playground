import numpy as np
from scipy.signal import resample_poly, firwin, bilinear, lfilter
import matplotlib.pyplot as plt
from scipy.io import wavfile

src_fname = 'samples/2024-09-10_sn10000000_cf92500000.0_sr250000.0_rg50.iq'
x = np.fromfile(src_fname, dtype=np.complex64)

sample_rate = 250e3 # 보통 FM station 은 250 kHz bandwidth 을 쓰고, 그래서 sampling rate 도 bandwidth 에 맞게 250 kHz 를 쓴다고 한다.
center_freq = 92500e3

# Ref: https://pysdr.org/content/rds.html#wrap-up-and-final-code

# Demodulation
x = np.diff(np.unwrap(np.angle(x)))

# De-emphasis filter, H(s) = 1/(RC*s + 1), implemented as IIR via bilinear transform
bz, az = bilinear(1, [75e-6, 1], fs=sample_rate)
x = lfilter(bz, az, x)

# decimate by 6 to get mono audio
x = x[::6]
sample_rate_audio = sample_rate/6

# normalize volume so its between -1 and +1
x /= np.max(np.abs(x))

# some machines want int16s
x *= 32767
x = x.astype(np.int16)

# Save to wav file, you can open this in Audacity for example
wavfile.write(f"{src_fname[:-3]}.demod.wav", int(sample_rate_audio), x)