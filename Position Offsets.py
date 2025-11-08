import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 设置随机种子以确保结果的可重复性
np.random.seed(42)

# 模拟数据参数
num_samples = 200  # 每秒10个数据点，共20秒
time = np.linspace(0, 20, num_samples)

# 无风状态下的位置偏移数据
no_wind_position = {
    "time": time,
    "x": np.random.normal(0, 0.1, num_samples),    # x位置偏移，均值0，标准差0.1
    "y": np.random.normal(0, 0.1, num_samples),    # y位置偏移，均值0，标准差0.1
    "z": np.random.normal(1, 0.05, num_samples),   # z位置（高度），均值1，标准差0.05
}

# 三级风自然状态下的位置偏移数据
wind_level3_natural_position = {
    "time": time,
    "x": np.random.normal(0, 0.3, num_samples),    # x位置偏移，均值0，标准差0.3
    "y": np.random.normal(0, 0.3, num_samples),    # y位置偏移，均值0，标准差0.3
    "z": np.random.normal(1, 0.1, num_samples),    # z位置（高度），均值1，标准差0.1
}

# 三级风强化学习控制状态下的位置偏移数据
wind_level3_rl_position = {
    "time": time,
    "x": np.random.normal(0, 0.15, num_samples),   # x位置偏移，均值0，标准差0.15
    "y": np.random.normal(0, 0.15, num_samples),   # y位置偏移，均值0，标准差0.15
    "z": np.random.normal(1, 0.07, num_samples),   # z位置（高度），均值1，标准差0.07
}

# 将数据转换为DataFrame
no_wind_pos_df = pd.DataFrame(no_wind_position)
wind_level3_natural_pos_df = pd.DataFrame(wind_level3_natural_position)
wind_level3_rl_pos_df = pd.DataFrame(wind_level3_rl_position)

# 可视化位置偏移
plt.figure(figsize=(15, 10))

# 绘制无风状态下的位置偏移
plt.subplot(1, 3, 1)
plt.plot(no_wind_pos_df["time"], no_wind_pos_df["x"], label="X Offset")
plt.plot(no_wind_pos_df["time"], no_wind_pos_df["y"], label="Y Offset")
plt.plot(no_wind_pos_df["time"], no_wind_pos_df["z"], label="Z Offset")
plt.title("No Wind - Position Offsets")
plt.xlabel("Time (s)")
plt.ylabel("Offset (m)")
plt.legend()
plt.grid(True)

# 绘制三级风自然状态下的位置偏移
plt.subplot(1, 3, 2)
plt.plot(wind_level3_natural_pos_df["time"], wind_level3_natural_pos_df["x"], label="X Offset")
plt.plot(wind_level3_natural_pos_df["time"], wind_level3_natural_pos_df["y"], label="Y Offset")
plt.plot(wind_level3_natural_pos_df["time"], wind_level3_natural_pos_df["z"], label="Z Offset")
plt.title("Level 3 Wind - Position Offsets")
plt.xlabel("Time (s)")
plt.ylabel("Offset (m)")
plt.legend()
plt.grid(True)

# 绘制三级风强化学习控制状态下的位置偏移
plt.subplot(1, 3, 3)
plt.plot(wind_level3_rl_pos_df["time"], wind_level3_rl_pos_df["x"], label="X Offset")
plt.plot(wind_level3_rl_pos_df["time"], wind_level3_rl_pos_df["y"], label="Y Offset")
plt.plot(wind_level3_rl_pos_df["time"], wind_level3_rl_pos_df["z"], label="Z Offset")
plt.title("RL Control - Position Offsets")
plt.xlabel("Time (s)")
plt.ylabel("Offset (m)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()