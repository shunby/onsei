from onsei.player.simple_player import SimplePlayer
from onsei.player.player import Player
from onsei.wave import Wave
from onsei.wave import db_to_multiples, interpolate
import pyaudio
import numpy as np
import matplotlib.pyplot as plt

freq = 400

wav_u = Wave(freq, interpolate(
        db_to_multiples(
        [18]+[None]*4+[1.4]+[None]*4+[-4.6]+[None]*6+[-6.3]),
        width=1.2
        ).tolist())
wav_e = Wave(freq, interpolate(
        db_to_multiples(
                [20] + [None] * 6 + [10.6] + [None] * 3 + [12.5] + [None] * 7 + [6]
        )
).tolist())
wav_o = Wave(freq, interpolate(
        db_to_multiples(
                [23.4] + [20.3] + [None] * 4 + [-13.6] + [None] * 3 + [-2]
        )
).tolist())
p = SimplePlayer(wav_u, 1000)
p.play()
p = SimplePlayer(wav_e, 1000)
p.play()
p = SimplePlayer(wav_o, 1000)
p.play()