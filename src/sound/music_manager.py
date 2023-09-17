from pygame import mixer
import os
class MusicManager:
    def __init__(self):
        self.__volume =0.0
        self.__is_playing = False
        mixer.init()

    def get_volume(self)->float:
        return self.__volume
    
    def play(self)->bool:
        mixer.music.play()
        self.__is_playing = True
        return self.__is_playing
    
    def change_volume(self,magnitude)->float:
        new_volume = self.get_volume()+magnitude
        mixer.music.set_volume(new_volume)
        self.__volume= new_volume
        return new_volume
        

    def pause(self)-> bool:
        mixer.music.pause()
        self.__is_playing= False
        return self.__is_playing
    
    def load(self,audio_path:str)->None:
        if not os.path.isfile(audio_path):
            raise FileNotFoundError(f"The audio file {audio_path} does not exist")
        mixer.music.load(audio_path)

    def get_is_playing(self):
        return self.__is_playing