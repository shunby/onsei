from .player import Player
import pyaudio

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
        pass
