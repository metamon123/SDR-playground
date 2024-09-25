import numpy as np
from scipy.signal import resample_poly, firwin, bilinear, lfilter
import matplotlib.pyplot as plt
from scipy.io import wavfile

src_fname = 'samples/2024-09-10_sn10000000_cf92500000.0_sr250000.0_rg50.iq'
x = np.fromfile(src_fname, dtype=np.complex64)

sample_rate = 250e3