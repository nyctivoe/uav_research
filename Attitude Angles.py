import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 设置随机种子以确保结果的可重复性
np.random.seed(42)

# 模拟数据参数
num_samples = 200  # 每秒10个数据点，共20秒

# 时间序列
time = np.linspace(0, 20, num_samples)

# 无风状态下的模拟数据
no_wind_data = {
    "time": time,
    "pitch": np.random.normal(0, 1, num_samples),  # 俯仰角，均值0，标准差1
    "roll": np.random.normal(0, 1, num_samples),   # 横滚角，均值0，标准差1
    "yaw": np.random.normal(0, 2, num_samples),    # 偏航角，均值0，标准差2
    "x": np.random.normal(0, 0.1, num_samples),    # x位置偏移，均值0，标准差0.1
    "y": np.random.normal(0, 0.1, num_samples),    # y位置偏移，均值0，标准差0.1
    "z": np.random.normal(1, 0.05, num_samples),   # z位置（高度），均值1，标准差0.05
    "motor1": np.random.normal(1000, 10, num_samples),  # 电机1转速，均值1000，标准差10
    "motor2": np.random.normal(1000, 10, num_samples),  # 电机2转速，均值1000，标准差10
    "motor3": np.random.normal(1000, 10, num_samples),  # 电机3转速，均值1000，标准差10
    "motor4": np.random.normal(1000, 10, num_samples)   # 电机4转速，均值1000，标准差10
}

# 三级风自然状态下的模拟数据（风速3.4-5.4米/秒）
wind_level3_natural_data = {
    "time": time,
    "pitch": np.random.normal(2, 3, num_samples),  # 俯仰角，均值2，标准差3
    "roll": np.random.normal(2, 3, num_samples),   # 横滚角，均值2，标准差3
    "yaw": np.random.normal(5, 5, num_samples),    # 偏航角，均值5，标准差5
    "x": np.random.normal(0, 0.3, num_samples),    # x位置偏移，均值0，标准差0.3
    "y": np.random.normal(0, 0.3, num_samples),    # y位置偏移，均值0，标准差0.3
    "z": np.random.normal(1, 0.1, num_samples),    # z位置（高度），均值1，标准差0.1
    "motor1": np.random.normal(1050, 20, num_samples),  # 电机1转速，均值1050，标准差20
    "motor2": np.random.normal(1050, 20, num_samples),  # 电机2转速，均值1050，标准差20
    "motor3": np.random.normal(1050, 20, num_samples),  # 电机3转速，均值1050，标准差20
    "motor4": np.random.normal(1050, 20, num_samples)   # 电机4转速，均值1050，标准差20
}

# 三级风强化学习控制状态下的模拟数据
wind_level3_rl_data = {
    "time": time,
    "pitch": np.random.normal(1, 2, num_samples),  # 俯仰角，均值1，标准差2
    "roll": np.random.normal(1, 2, num_samples),   # 横滚角，均值1，标准差2
    "yaw": np.random.normal(3, 3, num_samples),    # 偏航角，均值3，标准差3
    "x": np.random.normal(0, 0.15, num_samples),   # x位置偏移，均值0，标准差0.15
    "y": np.random.normal(0, 0.15, num_samples),   # y位置偏移，均值0，标准差0.15
    "z": np.random.normal(1, 0.07, num_samples),   # z位置（高度），均值1，标准差0.07
    "motor1": np.random.normal(1030, 15, num_samples),  # 电机1转速，均值1030，标准差15
    "motor2": np.random.normal(1030, 15, num_samples),  # 电机2转速，均值1030，标准差15
    "motor3": np.random.normal(1030, 15, num_samples),  # 电机3转速，均值1030，标准差15
    "motor4": np.random.normal(1030, 15, num_samples)   # 电机4转速，均值1030，标准差15
}

# 将数据转换为DataFrame
no_wind_df = pd.DataFrame(no_wind_data)
wind_level3_natural_df = pd.DataFrame(wind_level3_natural_data)
wind_level3_rl_df = pd.DataFrame(wind_level3_rl_data)

# 可视化处理
plt.figure(figsize=(15, 10))

# 姿态角可视化
plt.subplot(2, 2, 1)
plt.plot(no_wind_df["time"], no_wind_df["pitch"], label="No Wind - Pitch")
plt.plot(no_wind_df["time"], no_wind_df["roll"], label="No Wind - Roll")
plt.plot(no_wind_df["time"], no_wind_df["yaw"], label="No Wind - Yaw")
plt.title("No Wind - Attitude Angles")
plt.xlabel("Time (s)")
plt.ylabel("Angle (degrees)")
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(wind_level3_natural_df["time"], wind_level3_natural_df["pitch"], label="Level 3 Wind - Pitch")
plt.plot(wind_level3_natural_df["time"], wind_level3_natural_df["roll"], label="Level 3 Wind - Roll")
plt.plot(wind_level3_natural_df["time"], wind_level3_natural_df["yaw"], label="Level 3 Wind - Yaw")
plt.title("Level 3 Wind - Attitude Angles")
plt.xlabel("Time (s)")
plt.ylabel("Angle (degrees)")
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(wind_level3_rl_df["time"], wind_level3_rl_df["pitch"], label="RL Control - Pitch")
plt.plot(wind_level3_rl_df["time"], wind_level3_rl_df["roll"], label="RL Control - Roll")
plt.plot(wind_level3_rl_df["time"], wind_level3_rl_df["yaw"], label="RL Control - Yaw")
plt.title("RL Control - Attitude Angles")
plt.xlabel("Time (s)")
plt.ylabel("Angle (degrees)")
plt.legend()

# 位置偏移可视化
plt.subplot(2, 2, 4)
plt.plot(no_wind_df["time"], no_wind_df["x"], label="No Wind - X Offset")
plt.plot(no_wind_df["time"], no_wind_df["y"], label="No Wind - Y Offset")
plt.plot(no_wind_df["time"], no_wind_df["z"], label="No Wind - Z Offset")
plt.title("No Wind - Position Offsets")
plt.xlabel("Time (s)")
plt.ylabel("Offset (m)")
plt.legend()

plt.tight_layout()
plt.show()

# 保存数据到CSV文件（如果需要）
no_wind_df.to_csv("no_wind_data.csv", index=False)
wind_level3_natural_df.to_csv("wind_level3_natural_data.csv", index=False)
wind_level3_rl_df.to_csv("wind_level3_rl_data.csv", index=False)