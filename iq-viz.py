import numpy as np
from scipy.signal import resample_poly, firwin, bilinear, lfilter
import matplotlib.pyplot as plt
from scipy.io import wavfile

src_fname = 'samples/2024-09-10_sn10000000_cf92500000.0_sr250000.0_rg50.iq'
x = np.fromfile(src_fname, dtype=np.complex64)

center_freq = 92500e3 # 92.5 MHz
sample_rate = 250e3

N = 1024 # fft_size
x = x[0:N]
# apply window? (hamming, hanning, blackman-harris, ...)
# https://velog.io/@workhard/hanning-window%EB%9E%80 여기서는 hanning 이 가장 무난하다고 한다. 우선은 SDR Console 에서 쓰고 있던 Blackman 을 쓰자.
x = x * np.blackman(len(x))

PSD = np.abs(np.fft.fft(x)) ** 2 / (N * sample_rate)
PSD = 10.0 * np.log10(PSD)
print(PSD)

# fftshift: 0 에 매칭되는 값이 가운데가 되도록 전체 리스트를 shift 한다.
# 마지막에 fftshift 를 하든 log 전에 fftshift 를 하든 최종 결과는 똑같다.
PSD = np.fft.fftshift(PSD)
print(PSD)

f = np.arange(sample_rate/-2.0, sample_rate/2.0, sample_rate/N) # start, stop, step
f += center_freq
f = f / 1e6 # Hz -> MHz

plt.plot(f, PSD)
plt.xlabel("Frequency [MHz]")
plt.ylabel("Magnitude [dB]")
plt.grid(True)
plt.show()