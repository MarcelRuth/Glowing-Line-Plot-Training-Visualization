import cv2
import os

def images_to_video(image_folder, video_path, fps):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort(key=lambda x: int(x.split('_')[1].split('.png')[0]))  # Sort the images by epoch number
    
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'DIVX'), fps, (width, height))
    
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
        
    cv2.destroyAllWindows()
    video.release()
