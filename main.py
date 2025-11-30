import numpy as np
import matplotlib.pyplot as plt

# 1. 関数の定義 (y = x^2)
def f(x):
    return x**2

# 2. 真の微分 (f'(x) = 2x)
def df_analytic(x):
    return 2 * x

# --- 設定 ---
target_x = 1.5  # 接線を引く点
h = 1.0         # 差分 h (あえて大きく設定)

# --- 計算 ---
# a. 真の値
true_slope = df_analytic(target_x)

# b. 前方差分 (Forward)
fwd_slope = (f(target_x + h) - f(target_x)) / h

# c. 中心差分 (Central)
cnt_slope = (f(target_x + h) - f(target_x - h)) / (2 * h)

# --- ターミナルへの出力 (ここを追加) ---
print("-" * 40)
print(f"対象の関数: y = x^2,  点 x = {target_x},  差分 h = {h}")
print("-" * 40)
print(f"1. 真の微分 (解析解) : Slope = {true_slope:.4f}")
print(f"2. 前方差分 (青線)   : Slope = {fwd_slope:.4f}  (誤差: {fwd_slope - true_slope:.4f})")
print(f"3. 中心差分 (緑線)   : Slope = {cnt_slope:.4f}  (誤差: {cnt_slope - true_slope:.4f})")
print("-" * 40)
print("※ 2次関数では中心差分の誤差が数学的に0になるため、真の値と一致します。")


# --- グラフ描画の準備 ---
x_range = np.linspace(0, 4, 100)
target_y = f(target_x)

# 接線の式: y = slope * (x - x0) + y0
tangent_true = true_slope * (x_range - target_x) + target_y
tangent_fwd  = fwd_slope  * (x_range - target_x) + target_y
tangent_cnt  = cnt_slope  * (x_range - target_x) + target_y

plt.figure(figsize=(10, 8))

# 関数 y=x^2
plt.plot(x_range, f(x_range), color='black', linewidth=2, label="Function: $y=x^2$")

# 1. 前方差分 (青): 大きくズレていることを示す
plt.plot(x_range, tangent_fwd, color='blue', alpha=0.6, linewidth=2, 
         label=f"Forward Diff (h={h}): Slope={fwd_slope:.2f}")

# 2. 真の接線 (赤): 太く、少し薄く描く (背景として)
plt.plot(x_range, tangent_true, color='red', alpha=0.3, linewidth=8, linestyle='-',
         label=f"True Tangent: Slope={true_slope:.2f}")

# 3. 中心差分 (緑): 赤線の上に細く描く -> 重なっていることを可視化
plt.plot(x_range, tangent_cnt, color='green', linewidth=2, linestyle='--',
         label=f"Central Diff (h={h}): Slope={cnt_slope:.2f} (Matches True!)")

# ポイントの描画
plt.scatter(target_x, target_y, color='red', s=100, zorder=5) # 中心点
plt.scatter(target_x + h, f(target_x + h), color='blue', s=50, zorder=5) # x+h
plt.scatter(target_x - h, f(target_x - h), color='green', s=50, zorder=5) # x-h

# 補助線
plt.vlines(target_x, 0, target_y, linestyles=':', colors='gray')
plt.vlines(target_x + h, 0, f(target_x + h), linestyles=':', colors='blue', alpha=0.5)
plt.vlines(target_x - h, 0, f(target_x - h), linestyles=':', colors='green', alpha=0.5)

plt.title(f"Visualizing Numerical Differentiation (x={target_x}, h={h})")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim(0, 16)
plt.legend(loc='upper left', fontsize=11)
plt.grid(True)

plt.show()

