import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

if __name__ == "__main__":
    # 経験と自信の相関を定義
    x = np.array([0, 0.3, 0.6, 1])
    y = np.array([0, 0.6, 0.2, 0.6])

    # 補間関数を作成
    f = interp1d(x, y, kind="cubic")

    # 0から2までのx座標を生成
    xnew_1 = np.linspace(0, 2, 900)

    # ynewを初期化
    ynew_1 = f(np.linspace(0, 1, 300))

    # パターンを繰り返す
    for i in range(1, 2):
        start_y = ynew_1[-1]  # 前の区間の最終値を取得
        y_segment = f(np.linspace(0, 1, 300)) + \
            (start_y - y[0])  # 各区間を前の区間の終点から始まるように調整
        ynew_1 = np.concatenate([ynew_1, y_segment])

    # 2から6までのx座標を生成
    xnew_2 = np.linspace(2, 6, 900)

    # ynewを初期化
    ynew_2 = f(np.linspace(0, 1, 300)) + ynew_1[-1] - y[0]

    # パターンを繰り返す
    for i in range(1, 4):
        start_y = ynew_2[-1]  # 前の区間の最終値を取得
        y_segment = f(np.linspace(0, 1, 300)) * 0.5 + (start_y -
                                                       y[0] * 0.5)  # 各区間を前の区間の終点から始まるように調整し、yの上昇幅を半分にする
        ynew_2 = np.concatenate([ynew_2, y_segment])

    # 合体
    xnew = np.concatenate([xnew_1, xnew_2])
    ynew = np.concatenate([ynew_1, ynew_2])

    # グラフの生成
    plt.figure(figsize=(10, 6))
    plt.plot(xnew, ynew, label="master")
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

    plt.savefig("images/dunning_kruger_master.png",
                dpi=300, bbox_inches='tight')
