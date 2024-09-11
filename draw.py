import cv2
import os
import torch
import numpy as np

from ultralytics.engine.results import Results

# def get_text_color(box_color):
#     text_color = (255,255,255)

#     brightness = box_color[2]*0.299 + box_color[1]*0.587 + box_color[0]*0.114

#     if(brightness > 180):
#         text_color = (0, 0, 0)

#     return text_color

def draw_plus_sign(image, center, size, color, thickness=2):
    half_size = size // 2
    cv2.line(image, (center[0] - half_size, center[1]), (center[0] + half_size, center[1]), color, thickness)
    cv2.line(image, (center[0], center[1] - half_size), (center[0], center[1] + half_size), color, thickness)

def box(img, detection_output, class_list, colors=None):    
    # Copy image, in case that we need original image for something
    out_image = img 

    for run_output in detection_output:
        # Unpack
        _, _, box = run_output        

        # Calculate the center and radius of the bounding circle
        center_x = int((box[0] + box[2]) / 2)
        center_y = int((box[1] + box[3]) / 2)
        width = int(box[2] - box[0])
        height = int(box[3] - box[1])
        radius = int(max(width, height) / 2)

        # Draw bounding circle in red
        circle_color = (0, 0, 255)  # Red color in BGR
        cv2.circle(out_image, (center_x, center_y), radius, circle_color, 2)

        # Draw plus sign in yellow
        plus_color = (0, 255, 255)  # Yellow color in BGR
        plus_size = radius // 2  # Make the plus sign size relative to the circle radius
        draw_plus_sign(out_image, (center_x, center_y), plus_size, plus_color)

    return out_image



def fps(avg_fps, combined_img):        
    avg_fps_str = float("{:.2f}".format(avg_fps))
    
    cv2.putText(combined_img, "FPS: "+str(avg_fps_str), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    return combined_img

