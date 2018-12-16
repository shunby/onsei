import numpy as np

class Wave:
    """
    周波数成分ごとの大きさ（の比率）を保持する、時間変化のない音波。

    Attributes
    -----
    freqs: dict[freq(float), amp(float)]
        周波数をキーにもち、その成分の大きさを保持する辞書。
    """
    def __init__(self, freqs):
        # ガード節
        if not isinstance(freqs, dict):
            print("Wave#__init__: 期待された型: dict, 受け取った型: " + type(freqs))
            raise TypeError()
        self.freqs = freqs
