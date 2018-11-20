class Wave:
    """
    基本周波数・倍音の比率を保持する音声。

    Attributes
    -----
    base_freq: float
        この音声の基本周波数(Hz)
    multiples: list(float)
        基本周波数の音及び倍音の大きさの比率
        multiples[i]は base_freq*(i+1) Hzの音の大きさの比率を保持する。
    """
    def __init__(self, base_freq, multiples):
        # ガード節
        if not (isinstance(base_freq, (int, float)) 
                and isinstance(multiples, list)):
            raise ValueError()
        
        self.base_freq = base_freq
        self.multiples = multiples
        
