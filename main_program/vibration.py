
import os
import pybullet as p
import time
import numpy as np
import imageio
from PIL import Image
from main_corresponding_library import vib_type
from weight_current import weight_current
from what_material import what_material

#Initialize environment
p.connect(p.GUI)
p.setGravity(0, 0, -10)
# p.setGravity(0, 0, 0)  ##without gravity,and to change the last contant can present any gravity condition

light_direction = [1, 0, 0] # Lighting direction, such as [-1, -1, -1]
p.configureDebugVisualizer(p.COV_ENABLE_SHADOWS, 0) # Enable or disable shadows as needed

camera_distance = 0.2 #The distance between the camera and the target point
camera_yaw = 50 # The horizontal rotation angle of the camera around the target point
camera_pitch = -35 # Camera pitch angle
camera_target_position = [0, 0, 0] # The target point pointed by the camera

# Update camera perspective
p.resetDebugVisualizerCamera(cameraDistance=camera_distance,
                             cameraYaw=camera_yaw,
                             cameraPitch=camera_pitch,
                             cameraTargetPosition=camera_target_position)

# Load cups
cup_urdf_path = "D:/Graduate/6401/container-imagination-only-container-visualize/container-imagination-only-container-visualize/object/Cup_GeoCenter.urdf"
cup_id = p.loadURDF(cup_urdf_path, [0, 0, 0])
images = [] # Initialize an empty list to store images

# friction_coefficient = 0.8
# p.changeDynamics(cup_id, -1, lateralFriction=friction_coefficient) ##if want to add friction and its constant

# Add filling
filler_ids = []
filler_urdf_path = "D:/Graduate/6401/container-imagination-only-container-visualize/container-imagination-only-container-visualize/object/m&m.urdf"  # Filler URDF path
for i in range(50):  # Assume there are 50 fillers
    x, y = np.random.uniform(0, 0.03), np.random.uniform(-0.05, 0.05) 
    filler_id = p.loadURDF(filler_urdf_path, [x, y, 0.01])  # inside the cup
    filler_ids.append(filler_id)

    # p.changeDynamics(filler_id, -1, lateralFriction=friction_coefficient)

# # Initialize environment
# p.connect(p.GUI)
# p.setGravity(0, 0, -10)

# light_direction = [1, 0, 0] # Lighting direction, such as [-1, -1, -1]
# p.configureDebugVisualizer(p.COV_ENABLE_SHADOWS, 0) # Enable or disable shadows as needed

# camera_distance = 0.1 # The distance between the camera and the target point
# camera_yaw = 50 # The horizontal rotation angle of the camera around the target point
# camera_pitch = -35 # Camera pitch angle
# camera_target_position = [0, 0, 0] # The target point pointed by the camera

# # Update camera perspective
# p.resetDebugVisualizerCamera(cameraDistance=camera_distance,
#                              cameraYaw=camera_yaw,
#                              cameraPitch=camera_pitch,
#                              cameraTargetPosition=camera_target_position)

# # Load cup
# cup_urdf_path = "D:/Graduate/6401/container-imagination-only-container-visualize/container-imagination-only-container-visualize/object/Cup_GeoCenter.urdf"
# cup_id = p.loadURDF(cup_urdf_path, [0, 0, 0])
# images = []  # Initialize an empty list to store images

# # friction_coefficient = 0.8
# # p.changeDynamics(cup_id, -1, lateralFriction=friction_coefficient)

## Add padding
# filler_ids = []
# filler_urdf_path = "D:/Graduate/6401/container-imagination-only-container-visualize/container-imagination-only-container-visualize/object/s-m&m.urdf"  # Filler URDF path
# for i in range(100):  # Assume there are 100 fillers
#     x, y = np.random.uniform(0, 0.03), np.random.uniform(-0.005, 0.005) 
#     filler_id = p.loadURDF(filler_urdf_path, [x, y, 0.01])  # inside the cup
#     filler_ids.append(filler_id)

#     # p.changeDynamics(filler_id, -1, lateralFriction=friction_coefficient)
##Fine-tuned preprocessing to adapt to small objects

# # Initialize environment
# p.connect(p.GUI)
# p.setGravity(0, 0, -10)

# light_direction = [1, 0, 0] # Lighting direction, such as [-1, -1, -1]
# p.configureDebugVisualizer(p.COV_ENABLE_SHADOWS, 0) # Enable or disable shadows as needed

# camera_distance = 0.1 # The distance between the camera and the target point
# camera_yaw = 50 # The horizontal rotation angle of the camera around the target point
# camera_pitch = -35 # Camera pitch angle
# camera_target_position = [0, 0, 0] # The target point pointed by the camera

# # Update camera perspective
# p.resetDebugVisualizerCamera(cameraDistance=camera_distance,
#                              cameraYaw=camera_yaw,
#                              cameraPitch=camera_pitch,
#                              cameraTargetPosition=camera_target_position)

# # load cup
# cup_urdf_path = "D:/Graduate/6401/container-imagination-only-container-visualize/container-imagination-only-container-visualize/object/Cup_GeoCenter.urdf"
# cup_id = p.loadURDF(cup_urdf_path, [0, 0, 0])
# images = []  # Initialize an empty list to store images

# # friction_coefficient = 0.8
# # p.changeDynamics(cup_id, -1, lateralFriction=friction_coefficient)

# # Add filling
# filler_ids = []
# filler_urdf_path = "D:/Graduate/6401/container-imagination-only-container-visualize/container-imagination-only-container-visualize/object/cubic.urdf"  # Filler URDF path
# for i in range(100):  # Assume there are 100 fillers
#     x, y = np.random.uniform(0, 0.03), np.random.uniform(-0.005, 0.005) 
#     filler_id = p.loadURDF(filler_urdf_path, [x, y, 0.01])  # inside the cup
#     filler_ids.append(filler_id)

#     # p.changeDynamics(filler_id, -1, lateralFriction=friction_coefficient)
##Fine-tuned preprocessing to adapt to cubic objects


# p.connect(p.GUI)
# p.setGravity(0, 0, -10)

# light_direction = [1, 0, 0] # Lighting direction, such as [-1, -1, -1]
# p.configureDebugVisualizer(p.COV_ENABLE_SHADOWS, 0) # Enable or disable shadows as needed

# camera_distance = 0.2 # The distance between the camera and the target point

# camera_yaw = -150 # The horizontal rotation angle of the camera around the target point
# camera_pitch = -35 # Camera pitch angle
# camera_target_position = [0, 0, 0] # The target point pointed by the camera

# # Update camera perspective
# p.resetDebugVisualizerCamera(cameraDistance=camera_distance,
#                              cameraYaw=camera_yaw,
#                              cameraPitch=camera_pitch,
#                              cameraTargetPosition=camera_target_position)

# # load cup
# cup_urdf_path = "D:/Graduate/6401/container-imagination-only-container-visualize/container-imagination-only-container-visualize/object/copa.urdf"
# cup_id = p.loadURDF(cup_urdf_path, [0, 0, 0])
# images = []  # Initialize an empty list to store images

# # friction_coefficient = 0.8
# # p.changeDynamics(cup_id, -1, lateralFriction=friction_coefficient)

# # Add filling
# filler_ids = []
# filler_urdf_path = "D:/Graduate/6401/container-imagination-only-container-visualize/container-imagination-only-container-visualize/object/m&m.urdf"  # Filler URDF path
# for i in range(50):  # Assume there are 50 fillers
#     x, y = np.random.uniform(0, 0.03), np.random.uniform(0, 0.05) 
#     filler_id = p.loadURDF(filler_urdf_path, [x, y, 0.01])  # inside the cup
#     filler_ids.append(filler_id)

#     # p.changeDynamics(filler_id, -1, lateralFriction=friction_coefficient)
##Fine adjustments made by changing the container (cup)

material=what_material
vib_type(material,cup_id) #If the filled object is changed to a smile object or a cube block or others, you need to use the 1st and 2nd sections of code commented above or re-fine-tune it to get the appropriate simulation results; for the file replacement of the container (cup), please refer to Section 1 3 paragraphs
p.disconnect()

# image = images[0]  # Get the first image
# image.save(r'D:\Graduate\6401\container-imagination-only-container-visualize\container-imagination-only-container-visualize\gif\first_image.png')  # Save the first image as a PNG file

# mp4_path = r'D:\Graduate\6401\container-imagination-only-container-visualize\container-imagination-only-container-visualize\gif\simulation.mp4'
# with imageio.get_writer(mp4_path, fps=40,codec='libx264') as writer:
#     for img in images:
#         writer.append_data(np.array(img.convert("RGB")))

