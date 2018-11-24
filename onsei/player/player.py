from .. import Wave
from .. import ABCMeta, abstractmethod
class Player(metaclass=ABCMeta):
    """
    再生可能な、時間変化する音声。
    
    Attributes
    -----
    wave: Wave
        この音声の元となる音波。これに各Player固有の加工を施した音声が再生される。
    """
    def __init__(self, wave):
        if not isinstance(wave, Wave):
            raise ValueError()
        self.wave = wave
    
    @abstractmethod
    def play(self):
        """
        [抽象]
        この音声を再生する。
        """