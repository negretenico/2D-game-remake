from src.sprite.animation_manager import AnimationManager
from unittest.mock import Mock, patch
from pygame import Surface
import unittest


class TestAnimationManager(unittest.TestCase):
    @patch("pygame.image.load",returnValue =  Surface((0,0)))
    def test_add_animation(self,mock_load_images):
        animation_manager = AnimationManager()
        animations = animation_manager.add_animation("name",["path"])
        self.assertTrue("name" in animations)
        mock_load_images.assert_called()

    @patch("pygame.image.load",returnValue =  Surface((0,0)))
    def test_set_current_animation(self,mock):
        animation_manager = AnimationManager()
        animation_manager.add_animation("foo",["animation"])
        animation_manager.set_current_animation("foo")
        self.assertIsNotNone(animation_manager.current_animation)

    def test_set_current_animation_none(self):
        animation_manager = AnimationManager()
        animation_manager.set_current_animation("foo")
        self.assertIsNone(animation_manager.current_animation)
    
    @patch("pygame.image.load",returnValue =  Surface((0,0)))
    def test_get_current_frame(self,mock):
        animation_manager = AnimationManager()
        animation_manager.add_animation("foo",["animation"])
        animation_manager.set_current_animation("foo")
        surf = animation_manager.get_current_frame()
        self.assertIsNotNone(surf)

    def test_get_current_frame_none(self):
        animation_manager = AnimationManager()
        surf = animation_manager.get_current_frame()
        self.assertIsNone(surf)

    @patch("pygame.image.load",returnValue =  Surface((0,0)))
    def test_update(self,mock):
        animation_manager= AnimationManager()
        animation_manager.add_animation("foo",["animation"])
        animation_manager.set_current_animation('foo')
        animation_manager.update()
        self.assertEqual(1,animation_manager.animations['foo']['frame_counter'])
if __name__ =="__main__":
    unittest.main()