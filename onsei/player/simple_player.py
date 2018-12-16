from .player import Player
import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import random

SAMPLING_RATE  = 44100

class SimplePlayer(Player):
    """
    与えられた音波を順番にそのまま再生する音声。

    Attributes
    -----
    wave: Wave
        この音声の元となる音波。これに各Player固有の加工を施した音声が再生される。
    duration: int
        再生時間(ms)
    """
    def __init__(self, waves, durations):
        """
        コンストラクタ。与えられた音波をもとに新しい音声を作る。
        

        Parameters
        -----
        wave: list[Wave]
            この音声のもとになる音波。
        duration: list[int]
            各音声の再生時間(ms)
        """
        super().__init__(waves)
        if not isinstance(durations, list):
            raise TypeError()
        if len(waves) != len(durations):
            raise ValueError()
        self.durations = durations


    def _genwave(self, stream, wave, duration):
        #sin(2 * pi * f * t)
        # 時間軸
        t   = np.linspace(0, duration / 1000, duration / 1000 * SAMPLING_RATE)
        # 周波数データの内容から波形生成
        wav = np.sum([2 ** 10 * wave.freqs[freq] * np.sin(2 * np.pi * freq * t) for freq in wave.freqs.keys()], axis=0)
        # 下限が0の整数値にする
        wav = wav - np.min(wav)
        wav = np.ceil(wav)
        # バイナリ列に変換
        binary = b""
        for i in wav:
            binary += int(i).to_bytes(2, "little")

        return binary

    def play(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(rate=SAMPLING_RATE, channels=1, format=pyaudio.paInt16, output=True)
        bin = b""
        for index, wav in enumerate(self.waves):
            bin += self._genwave(stream, wav, self.durations[index])
        stream.write(bin)
        stream.close()
        audio.terminate()