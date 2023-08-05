import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

if __name__ == "__main__":
    # 経験と自信の相関を定義
    x = np.array([0, 0.3, 0.6, 1])
    y = np.array([0, 0.6, 0.2, 0.6])

    # 補間関数を作成
    f = interp1d(x, y, kind="cubic")

    # 0から1.2までのx座標を生成
    xnew = np.linspace(0, 6, 1800)

    # ynewを初期化
    ynew = f(np.linspace(0, 1, 300))

    # パターンを繰り返す
    for i in range(1, 6):
        start_y = ynew[-1]  # 前の区間の最終値を取得
        y_segment = f(np.linspace(0, 1, 300)) + \
            (start_y - y[0])  # 各区間を前の区間の終点から始まるように調整
        ynew = np.concatenate([ynew, y_segment])

    # グラフの生成
    plt.figure(figsize=(10, 6))
    plt.plot(xnew[:330], ynew[:330], label="beginner", color="black")
    plt.title("Dunning-Kruger Effect")
    plt.xlabel("Knowledge and Experience")
    plt.ylabel("Confidence")
    plt.legend()
    plt.xlim(0, 6.2)
    plt.ylim(0, 4)
    # plt.grid(True)

    # 軸の線と数値を削除
    plt.xticks([])  # x軸の目盛りを削除
    plt.yticks([])  # y軸の目盛りを削除

    # 画像ファイルとして出力
    plt.savefig("images/dunning_kruger_beginner.png",
                dpi=300, bbox_inches='tight')
