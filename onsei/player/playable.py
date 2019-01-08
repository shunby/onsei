from abc import ABCMeta, abstractmethod

class Playable(metaclass=ABCMeta):
    """
    playメソッドを通して再生可能な音声を表す。
    """
    @abstractmethod
    def play(self):
        """
        [抽象]
        この音声を再生する。
        """