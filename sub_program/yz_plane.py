import os
import pybullet as p
import time
import numpy as np
import imageio
from PIL import Image

# Initialize environment
p.connect(p.GUI)
p.setGravity(0, 0, -10)

light_direction = [1, 0, 0]  # Light direction, for example [-1, -1, -1]
p.configureDebugVisualizer(p.COV_ENABLE_SHADOWS, 0)  # Enable or disable shadows as needed

camera_distance = 0.2  # Distance of the camera from the target point
camera_yaw = 50  # Horizontal rotation angle of the camera around the target point
camera_pitch = -35  # Camera's pitch angle
camera_target_position = [0, 0, 0]  # Target point the camera is pointing at

# Update camera perspective
p.resetDebugVisualizerCamera(cameraDistance=camera_distance,
                             cameraYaw=camera_yaw,
                             cameraPitch=camera_pitch,
                             cameraTargetPosition=camera_target_position)

# Load the cup
cup_urdf_path = "D:/Graduate/6401/container-imagination-only-container-visualize/container-imagination-only-container-visualize/object/Cup_GeoCenter.urdf"
cup_id = p.loadURDF(cup_urdf_path, [0, 0, 0])
images = []  # Initialize an empty list to store images

# friction_coefficient = 0.8
# p.changeDynamics(cup_id, -1, lateralFriction=friction_coefficient)

# Add fillers
filler_ids = []
filler_urdf_path = "D:/Graduate/6401/container-imagination-only-container-visualize/container-imagination-only-container-visualize/object/m&m.urdf"  # Path for filler URDF
for i in range(50):  # Assuming there are 10 fillers
    x, y = np.random.uniform(0, 0.03), np.random.uniform(-0.05, 0.05)
    filler_id = p.loadURDF(filler_urdf_path, [x, y, 0.01])  # Inside the cup
    filler_ids.append(filler_id)

    # p.changeDynamics(filler_id, -1, lateralFriction=friction_coefficient)

# Simulate vibration
vibration_amplitude = 0.01  # Vibration amplitude
vibration_frequency_z = 1.5  # Vibration frequency on the z-axis
vibration_frequency_y = 1.5  # Vibration frequency on the y-axis
total_time = 5.0  # Total simulation time
time_step = 1 / 240  # Time step
num_steps = int(total_time / time_step)  # Total number of steps

images = []

for i in range(num_steps):
    t = i * time_step
    displacement_y = vibration_amplitude * np.sin(2 * np.pi * vibration_frequency_y * t)
    displacement_z = vibration_amplitude * np.cos(2 * np.pi * vibration_frequency_y * t) * 0.8
    new_pos = [0, displacement_y, displacement_z]  # Modified to vibrate on the YZ plane
    p.resetBasePositionAndOrientation(cup_id, new_pos, p.getQuaternionFromEuler([0, 0, 0]))
    
    width, height, rgba, _, _ = p.getCameraImage(240, 240)
    rgba_array = np.array(rgba)
    # print("RGBA array sample:", rgba_array[:10])  # Print some sample values for checking
    rgba_array = np.reshape(rgba_array, (height, width, 4))  # Convert RGBA data into an array
    image = Image.fromarray(rgba_array, mode='RGBA')
    images.append(image)

    p.stepSimulation()
    time.sleep(time_step)

p.disconnect()

# image = images[0]  # Get the first image
# image.save(r'D:\Graduate\6401\container-imagination-only-container-visualize\container-imagination-only-container-visualize\gif\first_image.png')  # Save the first image as a PNG file

# mp4_path = r'D:\Graduate\6401\container-imagination-only-container-visualize\container-imagination-only-container-visualize\gif\simulation.mp4'
# with imageio.get_writer(mp4_path, fps=40, codec='libx264') as writer:
#     for img in images:
#         writer.append_data(np.array(img.convert("RGB")))
