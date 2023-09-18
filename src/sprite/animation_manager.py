import pygame 
from typing import Dict
from pygame import Surface
class AnimationManager:
    def __init__(self):
        self.animations = {}
        self.current_animation = None
        self.current_frame_index = 0

    def add_animation(self, name, image_paths,frame_duration=5)->Dict[str,Surface]:
        frames = [pygame.image.load(image_path) for image_path in image_paths]
        self.animations[name] ={
            'frames': frames,
            "frame_duration": frame_duration,
            "frame_counter": 0,
        }
        return self.animations

    def set_current_animation(self, name)-> None:
        if name in self.animations:
            self.current_animation = name
            self.current_frame_index = 0

    def update(self):
        if self.current_animation:
                animation_info = self.animations[self.current_animation]
                animation_info["frame_counter"] += 1
                if animation_info["frame_counter"] >= animation_info["frame_duration"]:
                    animation_info["frame_counter"] = 0
                    self.current_frame_index += 1
                    if self.current_frame_index >= len(animation_info["frames"]):
                        self.current_frame_index = 0

    def get_current_frame(self)->Surface:
        if self.current_animation:
            return self.animations[self.current_animation]['frames'][self.current_frame_index]