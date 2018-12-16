import numpy as np
from .wave import Wave


def genwave_from_multiples(base_freq, multiples):
    """
    基本周波数・倍音の比率リストから倍音構造を持つ音波を作る。

    Attributes
    -----
    base_freq: float
        この音波の基本周波数(Hz)
    multiples: list(float)
        基本周波数の音及び倍音の大きさの比率
        multiples[i]は base_freq*(i+1) Hzの音の大きさの比率を保持する。
    """
    # ガード節
    if not (isinstance(base_freq, (int, float)) 
            and isinstance(multiples, list)):
        raise TypeError()
    # 与えられた倍音リストをもとに各周波数成分を保持する辞書を作成
    freqs = dict()
    for index, val in enumerate(multiples):
        freqs[base_freq * (index + 1)] = val
    return Wave(freqs)


def db_to_multiples(dbs):
    """
    デシベル表示の倍音の大きさリストから、Waveインスタンス生成に使える倍音比率リストを生成する
    ただし、渡されたリストのうち、要素の内容がNoneの部分は0に変換される

    Parameters
    -----
    dbs: list(float)
        デシベル表示の倍音の大きさリスト
    """
    # NoneをMINの値に変換
    # Noneのまま処理するとmax関数がエラーを吐く
    MIN = -1e10
    dbs = [MIN if i is None else i for i in dbs]

    max_db = max(dbs)
    # dBが1増えると10^(1/20)倍になる
    ret = [0 if i == MIN else 1 / (10 ** ((max_db - i)/20)) for i in dbs]
    return ret
def db_to_ratio(dbs):
    """
    デシベル表示の倍音の大きさリストから、Waveインスタンス生成に使える周波数成分リストを生成する
    ただし、渡されたリストのうち、要素の内容がNoneの部分は0に変換される

    Parameters
    -----
    dbs: dict(float, float)
        デシベル表示の倍音の大きさリスト
    """
    # NoneをMINの値に変換
    # Noneのまま処理するとmax関数がエラーを吐く
    MIN = -1e10
    dbs = {freq:(MIN if i is None else i) for freq, i in dbs.items()}

    max_db = max(dbs.values())
    # dBが1増えると10^(1/20)倍になる
    ret = {freq : (0 if i == MIN else 1 / (10 ** ((max_db - i)/20))) for freq, i in dbs.items()}
    return ret
def interpolate(multiples, width=1.4):
    """
    渡された倍音リストの内、Noneになっている部分を補間・出力する。

    Parameters
    -----
    multiples: list(float)
        補間元の倍音リスト
    width: float
        ガウス関数における、eの指数の分母の平方根
        大きいほど周波数の周りのすそ野が広くなる
    """
    
    # 先頭がNoneの場合、0と1番目の要素の値との間を補間する
    last_value = 0
    last_value_index = -1
    
    x = np.arange(len(multiples))
    # 与えられた周波数と振幅からガウス関数に基づきその周囲の値を決める
    gauss = lambda x, pos, width, height: height * np.exp(-((x - pos) ** 2)/(width))

    ret = np.sum([gauss(x, index, width, val) for index, val in enumerate(multiples)],axis=0)
    return ret
def interpolate2(ratio, N, width=30000):
    """
    渡された周波数成分リストの内、Noneになっている部分を補間・出力する。

    Parameters
    -----
    ratio: dict(float, float)
        補間元の周波数成分リスト
    N: int
        補間後の周波数リストの要素数
    width: float
        ガウス関数における、eの指数の分母
        大きいほど周波数の周りのすそ野が広くなる
    """
    # 周波数軸
    x = np.linspace(0.1, max(ratio.keys()), N)
    # 与えられた周波数と振幅からガウス関数に基づきその周囲の値を決める
    gauss = lambda x, pos, width, height: height * np.exp(-((x - pos) ** 2)/(width))
    ret = np.sum([gauss(x, freq, width, val) for freq, val in ratio.items()],axis=0)
    print(x)
    # print([gauss(x, freq, width, val) for freq, val in ratio.items()])
    import matplotlib.pyplot as plt
    plt.subplot(121)
    plt.plot(np.linspace(0.1, max(ratio.keys()), len(ratio)), ratio.values())
    plt.subplot(122)
    plt.plot(x, ret)
    # plt.show()

    return {x[index]: ret[index] for index in range(N)}