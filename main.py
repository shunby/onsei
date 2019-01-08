from onsei.player.simple_player import SimplePlayer
from onsei.player.player import Player
from onsei.wave import Wave
from onsei.wave_util import db_to_ratio, db_to_multiples, interpolate, genwave_from_multiples, interpolate2
import pyaudio
import numpy as np
import matplotlib.pyplot as plt

freq = 400

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
wav_k = Wave({freq: 0.00001 for freq in np.linspace(0, 44099, 50000)})
wav_none = Wave({0: 0})


p = SimplePlayer([wav_k, wav_a], [10, 107])
p.play()