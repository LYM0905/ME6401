
import os
import pybullet as p
import time
import numpy as np
import imageio
from PIL import Image


# 初始化环境
p.connect(p.GUI)
p.setGravity(0, 0, 0)

light_direction = [1, 0, 0]  # 光照方向，例如 [-1, -1, -1]
p.configureDebugVisualizer(p.COV_ENABLE_SHADOWS, 0)  # 根据需要启用或禁用阴影

camera_distance = 0.2  # 相机距离目标点的距离
camera_yaw = 50  # 相机围绕目标点的水平旋转角度
camera_pitch = -35  # 相机的俯仰角度
camera_target_position = [0, 0, 0]  # 相机指向的目标点

# 更新相机视角
p.resetDebugVisualizerCamera(cameraDistance=camera_distance,
                             cameraYaw=camera_yaw,
                             cameraPitch=camera_pitch,
                             cameraTargetPosition=camera_target_position)

# 加载杯子
cup_urdf_path = "D:/Graduate/6401/container-imagination-only-container-visualize/container-imagination-only-container-visualize/object/Cup_GeoCenter.urdf"
cup_id = p.loadURDF(cup_urdf_path, [0, 0, 0])
images = []  # 初始化一个空列表来存储图像

# friction_coefficient = 0.8
# p.changeDynamics(cup_id, -1, lateralFriction=friction_coefficient)

# 添加填充物
filler_ids = []
filler_urdf_path = "D:/Graduate/6401/container-imagination-only-container-visualize/container-imagination-only-container-visualize/object/m&m.urdf"  # 填充物 URDF 路径
for i in range(50):  # 假设有10个填充物
    x, y = np.random.uniform(0, 0.03), np.random.uniform(-0.05, 0.05) 
    filler_id = p.loadURDF(filler_urdf_path, [x, y, 0.01])  # 在杯子内部
    filler_ids.append(filler_id)

    # p.changeDynamics(filler_id, -1, lateralFriction=friction_coefficient)

# 模拟振动
vibration_amplitude = 0.02  # 振动幅度
vibration_frequency_x = 1.5  # x 轴振动频率
vibration_frequency_y = 1.5  # y 轴振动频率
total_time = 5.0  # 总模拟时间
time_step = 1 / 240  # 时间步长
num_steps = int(total_time / time_step)  # 总步数

images = []

for i in range(num_steps):
    t = i * time_step
    displacement_x = vibration_amplitude * np.sin(2 * np.pi * vibration_frequency_x * t)
    displacement_y = vibration_amplitude * np.cos(2 * np.pi * vibration_frequency_y * t)*0.8
    new_pos = [displacement_x, displacement_y, 0]  # 在水平平面上振动
    p.resetBasePositionAndOrientation(cup_id, new_pos, p.getQuaternionFromEuler([0, 0, 0]))
    
    width, height, rgba, _, _ = p.getCameraImage(240, 240)
    rgba_array = np.array(rgba)
    # print("RGBA array sample:", rgba_array[:10])  # 打印一些样本值以检查
    rgba_array = np.reshape(rgba_array, (height, width, 4))  # 将RGBA数据转换为数组
    image = Image.fromarray(rgba_array, mode='RGBA')
    images.append(image)

    p.stepSimulation()
    time.sleep(time_step)

p.disconnect()

# image = images[0]  # 获取第一个图像
# image.save(r'D:\Graduate\6401\container-imagination-only-container-visualize\container-imagination-only-container-visualize\gif\first_image.png')  # 将第一个图像保存为PNG文件

# mp4_path = r'D:\Graduate\6401\container-imagination-only-container-visualize\container-imagination-only-container-visualize\gif\simulation.mp4'
# with imageio.get_writer(mp4_path, fps=40,codec='libx264') as writer:
#     for img in images:
#         writer.append_data(np.array(img.convert("RGB")))

