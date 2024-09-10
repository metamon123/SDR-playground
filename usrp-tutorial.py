import uhd
usrp = uhd.usrp.MultiUSRP()
sample_nums = int(1e7) # 샘플을 몇 개 얻을 것인지
center_freq = 92500e3 # 어느 주파수에 tuning 할 것인지 (92.5 MHz)
sample_rate = 250e3 # 샘플을 얼마나 자주 얻을 것인지
recv_channels = [0] # USRP 의 어느 채널을 사용할 것인지
					# recv 의 경우 (0 -> RF A 의 RX2), (1 -> RF B 의 RX2)
recv_gain = 50 # 수신 감도 (dB), B210 은 최대 76 dB

from loguru import logger
logger.info("Start sampling via USRP B210", sample_nums, center_freq, sample_rate, recv_channels, recv_gain)
samples = usrp.recv_num_samps(sample_nums, center_freq, sample_rate, recv_channels, recv_gain)
logger.info("Done")
print(samples)

from datetime import date

fname = f"{date.today()}_sn{sample_nums}_cf{center_freq}_sr{sample_rate}_rg{recv_gain}.iq"
samples.tofile(fname)
logger.info(f"Stored IQ samples as {fname}")