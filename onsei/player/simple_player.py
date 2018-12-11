from .player import Player
import pyaudio
import numpy as np
import matplotlib.pyplot as plt

SAMPLING_RATE  = 44100

class SimplePlayer(Player):
    """
    与えられた音波をそのまま再生する音声。

    Attributes
    -----
    wave: Wave
        この音声の元となる音波。これに各Player固有の加工を施した音声が再生される。
    duration: int
        再生時間(ms)
    """
    def __init__(self, wave, duration):
        """
        コンストラクタ。与えられた音波をもとに新しい音声を作る。
        
        Parameters
        -----
        wave: Wave
            この音声のもとになる音波。
        duration: int
            再生時間(ms)
        """
        super().__init__(wave)
        self.duration = duration


    def play(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(rate=SAMPLING_RATE, channels=1, format=pyaudio.paInt16, output=True)
        #sin(2 * pi * f * t)
        # 時間軸
        t   = np.linspace(0, self.duration / 1000, self.duration / 1000 * SAMPLING_RATE)
        # i番目の倍音のサイン波を計算するlambda
        mul = lambda i: 2**12 * self.wave.multiples[i] * np.sin(2 * np.pi * self.wave.base_freq * (i+1) * t)
        wav = np.sum([mul(i) for i in range(len(self.wave.multiples))], axis=0)
        # 下限が0の整数値にする
        wav = wav - np.min(wav)
        wav = np.ceil(wav)
        # バイナリ列に変換
        binary = b""
        for i in wav:
            binary += int(i).to_bytes(2, "little")
        # 再生
        stream.write(binary)
        stream.close()
        audio.terminate()
