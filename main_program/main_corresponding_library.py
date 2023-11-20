import os
import pybullet as p
import time
import numpy as np
import imageio
from PIL import Image
import random
from weight_current import weight_current  # Import weight_current

def vib_1(cup_id):
    vibration_amplitude = 0.02  # Vibration amplitude
    vibration_frequency_x = 1.5  # X-axis vibration frequency
    vibration_frequency_y = 1.5  # Y-axis vibration frequency
    total_time = 5.0  # Total simulation time
    time_step = 1 / 240  # Time step
    num_steps = int(total_time / time_step)  # Total number of steps

    images = []

    for i in range(num_steps):
        t = i * time_step
        displacement_x = vibration_amplitude * np.sin(2 * np.pi * vibration_frequency_x * t)
        displacement_y = vibration_amplitude * np.cos(2 * np.pi * vibration_frequency_y * t)
        new_pos = [displacement_x, displacement_y, 0]  # Vibration on the horizontal plane
        p.resetBasePositionAndOrientation(cup_id, new_pos, p.getQuaternionFromEuler([0, 0, 0]))
        
        width, height, rgba, _, _ = p.getCameraImage(240, 240)
        rgba_array = np.array(rgba)
        rgba_array = np.reshape(rgba_array, (height, width, 4))  # Convert RGBA data to an array
        image = Image.fromarray(rgba_array, mode='RGBA')
        images.append(image)

        p.stepSimulation()
        time.sleep(time_step)
        # X-Y plane Vibration example

def vib_2(cup_id):
    vibration_amplitude = 0.01  # Vibration amplitude
    vibration_frequency_z = 1.5  # Z-axis vibration frequency
    vibration_frequency_y = 1.5  # Y-axis vibration frequency
    total_time = 5.0  # Total simulation time
    time_step = 1 / 240  # Time step
    num_steps = int(total_time / time_step)  # Total number of steps

    images = []

    for i in range(num_steps):
        t = i * time_step
        displacement_y = vibration_amplitude * np.sin(2 * np.pi * vibration_frequency_y * t)
        displacement_z = vibration_amplitude * np.cos(2 * np.pi * vibration_frequency_y * t) * 0.8
        new_pos = [0, displacement_y, displacement_z]  # Vibration on the YZ plane
        p.resetBasePositionAndOrientation(cup_id, new_pos, p.getQuaternionFromEuler([0, 0, 0]))
        
        width, height, rgba, _, _ = p.getCameraImage(240, 240)
        rgba_array = np.array(rgba)
        rgba_array = np.reshape(rgba_array, (height, width, 4))  # Convert RGBA data to an array
        image = Image.fromarray(rgba_array, mode='RGBA')
        images.append(image)

        p.stepSimulation()
        time.sleep(time_step)
        # Y-Z plane Vibration example

def vib_3(cup_id):
    vibration_amplitude = 0.02  # Vibration amplitude
    vibration_frequency_z = 1.5  # Z-axis vibration frequency
    vibration_frequency_x = 1.5  # X-axis vibration frequency
    total_time = 5.0  # Total simulation time
    time_step = 1 / 240  # Time step
    num_steps = int(total_time / time_step)  # Total number of steps

    images = []

    for i in range(num_steps):
        t = i * time_step
        displacement_x = vibration_amplitude * np.sin(2 * np.pi * vibration_frequency_x * t)
        displacement_z = vibration_amplitude * np.cos(2 * np.pi * vibration_frequency_z * t) * 0.8
        new_pos = [displacement_x, 0, displacement_z]  # Vibration on the XZ plane
        p.resetBasePositionAndOrientation(cup_id, new_pos, p.getQuaternionFromEuler([0, 0, 0]))
        
        width, height, rgba, _, _ = p.getCameraImage(240, 240)
        rgba_array = np.array(rgba)
        rgba_array = np.reshape(rgba_array, (height, width, 4))  # Convert RGBA data to an array
        image = Image.fromarray(rgba_array, mode='RGBA')
        images.append(image)

        p.stepSimulation()
        time.sleep(time_step)
        # X-Z plane Vibration example

def vib_4(cup_id):
    vibration_amplitude = 0.02  # Vibration amplitude
    vibration_frequency_x = 1.5  # X-axis vibration frequency
    vibration_frequency_y = 1.5  # Y-axis vibration frequency
    total_time = 5.0  # Total simulation time
    time_step = 1 / 240  # Time step
    num_steps = int(total_time / time_step)  # Total number of steps

    images = []

    for i in range(num_steps):
        t = i * time_step
        displacement_x = vibration_amplitude * np.sin(2 * np.pi * vibration_frequency_x * t)
        displacement_y = vibration_amplitude * np.cos(2 * np.pi * vibration_frequency_y * t) * 0.8
        new_pos = [displacement_x, displacement_y, 0]  # Vibration on the horizontal plane with different amplitude
        p.resetBasePositionAndOrientation(cup_id, new_pos, p.getQuaternionFromEuler([0, 0, 0]))
        
        width, height, rgba, _, _ = p.getCameraImage(240, 240)
        rgba_array = np.array(rgba)
        rgba_array = np.reshape(rgba_array, (height, width, 4))  # Convert RGBA data to an array
        image = Image.fromarray(rgba_array, mode='RGBA')
        images.append(image)

        p.stepSimulation()
        time.sleep(time_step)
        # Modified horizontal plane Vibration example

def vib_5(cup_id):
    vibration_amplitude = 0.02  # Vibration amplitude
    vibration_frequency_x = 1.5  # X-axis vibration frequency
    vibration_frequency_y = 1.5  # Y-axis vibration frequency
    total_time = 5.0  # Total simulation time
    time_step = 1 / 240  # Time step
    num_steps = int(total_time / time_step)  # Total number of steps

    images = []

    for i in range(num_steps):
        t = i * time_step
        displacement_x = vibration_amplitude * np.sin(2 * np.pi * vibration_frequency_x * t) * random.uniform(0.5, 1.5)
        displacement_y = vibration_amplitude * np.cos(2 * np.pi * vibration_frequency_y * t) * random.uniform(0.5, 1.5)
        new_pos = [displacement_x, displacement_y, 0]  # Random vibration on the horizontal plane
        p.resetBasePositionAndOrientation(cup_id, new_pos, p.getQuaternionFromEuler([0, 0, 0]))
        
        width, height, rgba, _, _ = p.getCameraImage(240, 240)
        rgba_array = np.array(rgba)
        rgba_array = np.reshape(rgba_array, (height, width, 4))  # Convert RGBA data to an array
        image = Image.fromarray(rgba_array, mode='RGBA')
        images.append(image)

        p.stepSimulation()
        time.sleep(time_step)
        # Random horizontal plane Vibration example


def vib_6(cup_id):
    vibration_amplitude = 0.02  # Vibration amplitude
    vibration_frequency_x = 1.5  # X-axis vibration frequency
    vibration_frequency_y = 1.5  # Y-axis vibration frequency
    total_time = 5.0  # Total simulation time
    time_step = 1 / 240  # Time step
    num_steps = int(total_time / time_step)  # Total number of steps

    images = []

    for i in range(num_steps):
        t = i * time_step
        displacement_x = vibration_amplitude * np.sin(2 * np.pi * vibration_frequency_x * t)
        displacement_y = vibration_amplitude * np.cos(2 * np.pi * vibration_frequency_y * t)
        new_pos = [displacement_x, displacement_y, 0]  # Vibration on the horizontal plane
        p.resetBasePositionAndOrientation(cup_id, new_pos, p.getQuaternionFromEuler([0, 0, 0]))
        
        width, height, rgba, _, _ = p.getCameraImage(240, 240)
        rgba_array = np.array(rgba)
        rgba_array = np.reshape(rgba_array, (height, width, 4))  # Convert RGBA data to an array
        image = Image.fromarray(rgba_array, mode='RGBA')
        images.append(image)

        p.stepSimulation()
        time.sleep(time_step)
        # Vibration example for a differently shaped object




        


__factory = {
    "what_material1": vib_1,
    "what_material2":vib_2,
    "what_material3":vib_3,
    "what_material4":vib_4,
    "what_material5":vib_5,
    "what_material6":vib_6,
}


def names():
    return sorted(__factory.keys())


def vib_type(name, *args, **kwargs):
    """
    Create a model instance.

    Parameters
    ----------
    name : str
        Model name. Can be one of 'inception', 'resnet18', 'resnet34',
        'resnet50', 'resnet101', and 'resnet152'.
    pretrained : bool, optional
        Only applied for 'resnet*' models. If True, will use ImageNet pretrained
        model. Default: True
    cut_at_pooling : bool, optional
        If True, will cut the model before the last global pooling layer and
        ignore the remaining kwargs. Default: False
    num_features : int, optional
        If positive, will append a Linear layer after the global pooling layer,
        with this number of output units, followed by a BatchNorm layer.
        Otherwise these layers will not be appended. Default: 256 for
        'inception', 0 for 'resnet*'
    norm : bool, optional
        If True, will normalize the feature to be unit L2-norm for each sample.
        Otherwise will append a ReLU layer after the above Linear layer if
        num_features > 0. Default: False
    dropout : float, optional
        If positive, will append a Dropout layer with this dropout rate.
        Default: 0
    num_classes : int, optional
        If positive, will append a Linear layer at the end as the classifier
        with this number of output units. Default: 0
    """
    if name not in __factory:
        raise KeyError("Unknown model:", name)
    return __factory[name](*args, **kwargs)