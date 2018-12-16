from ..wave import Wave
from abc import ABCMeta, abstractmethod
class Player(metaclass=ABCMeta):
    """
    再生可能な、時間変化する音声。
    
    Attributes
    -----
    wave: Wave
        この音声の元となる音波。これに各Player固有の加工を施した音声が再生される。
    """
    def __init__(self, waves):
        """
        コンストラクタ。与えられた音波をもとに新しい音声を作る。
        
        Parameters
        -----
        waves: list[Wave]
            この音声のもとになる音波。
        
        """
        if not isinstance(waves, list):
            raise TypeError()
        self.waves = waves
    
    @abstractmethod
    def play(self):
        """
        [抽象]
        この音声を再生する。
        """