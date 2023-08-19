# Glowing Line Plot Training Visualization

This repository contains code to visualize the training of a regression model. 
At each epoch where the model improves (i.e., reaches a lower loss), 
a "glowing" plot of true vs. predicted values is saved. 
After training, these images are compiled into a video.

## Usage

1. **Generate and Save Glowing Images During Training:**
   - In your training loop, call the `save_glowing_image` function from `src/glowing_image_generator.py` 
     whenever your model reaches a lower loss.
   
2. **Create a Video from Saved Images After Training:**
   - After training, call the `images_to_video` function from `src/video_creator.py` to compile 
     the saved images into a video.

## Requirements

Install the necessary packages with:

pip install -r requirements.txt

## Instructions:

### Clone the Repository:
git clone https://github.com/yourusername/Glowing-Line-Plot-Training-Visualization.git
### Navigate to the Project Directory:
cd Glowing-Line-Plot-Training-Visualization
### Install the Requirements:
pip install -r requirements.txt
### Run Your Training Script:
Integrate the save_glowing_image function into your training loop.
### Create the Video After Training:
Call the images_to_video function after training is complete to create a video from the saved images.