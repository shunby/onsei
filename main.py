from onsei.player.simple_player import SimplePlayer
from onsei.player.player import Player
from onsei.wave import Wave
from onsei.wave_util import db_to_ratio, db_to_multiples, interpolate, genwave_from_multiples, interpolate2
import pyaudio
import numpy as np
import matplotlib.pyplot as plt

freq = 270

wav_u = genwave_from_multiples(freq, interpolate(
        db_to_multiples(
        [18]+[None]*4+[1.4]+[None]*4+[-4.6]+[None]*6+[-6.3])
        ).tolist())
wav_e = genwave_from_multiples(freq, interpolate(
        db_to_multiples(
                [20] + [None] * 6 + [10.6] + [None] * 3 + [12.5] + [None] * 7 + [6]
        )
).tolist())
wav_o = genwave_from_multiples(freq, interpolate(
        db_to_multiples(
                [23.4] + [20.3] + [None] * 4 + [-13.6] + [None] * 3 + [-2]
        )
).tolist())
wav_a = genwave_from_multiples(freq, interpolate(
        db_to_multiples(
                [None]*2 + [40.6] + [None]*6 +  [30.0] + [None] * 1 +  [29.6] + [None]*2 + [24.6] + [None] * 2 + [6.9]
        )
).tolist())
wav_i = genwave_from_multiples(freq, interpolate(
        db_to_multiples(
                [None] * 0 + [31.8] + [None] * 8 + [21.8] + [None]*1 + [27.9] + [None]*2 + [24.6] + [None] * 1 + [14.6]
        )
).tolist())
wav_i_new = genwave_from_multiples(270, interpolate(
        db_to_multiples(
                [1.5 * i for i in [16.7, 17.3, 18.7, 19.4]] + [None]*18 + [0.7 * i for i in [27.5, 28.5, 31.0,26.6,28.4,29.6,26.2,25.2,21.5,20.4,23.4,26.4,25.0,25.5,26.8]]
        ), width=0.1
).tolist())
wav_i_fem = genwave_from_multiples(270, interpolate(
        db_to_multiples(
                [49.7, 43.0, 29.0] + [14.7, 18.6, 16.4, 13.3, 12.4, 18.1, 18.6, 28.3] + [39.1, 37.9, 37.0, 39.2, 40.6, 35.8, 35.6, 36.0, 36.3, 35.1, 24.2, None, 8.0, 15.0, 16.7, 11.1, None, 19.6, 18.0, 13.9, None, None, None, 14.0] + [None] * 6 + [21.0]
        ), width=0.1
).tolist())
wavinew_base = 94
# wav_i_new.freqs = {freq : amp * ((freq/border) if freq>border else 1) for index, (freq, amp) in enumerate(wav_i_new.freqs.items())}
wav_k = Wave({freq: 0.00001 for freq in np.linspace(0, 44099, 50000)})
wav_none = Wave({0: 0})

p = SimplePlayer([wav_i_new, wav_i_fem], [1000]*2)
p.play()
freq_in_order_m = np.array(sorted(wav_i_new.freqs))
plt.plot(freq_in_order_m,[wav_i_new.freqs[i] for i in freq_in_order_m]) 
freq_in_order_f = np.array(sorted(wav_i_fem.freqs))
plt.plot(freq_in_order_f,[wav_i_fem.freqs[i] for i in freq_in_order_f]) 
plt.show()