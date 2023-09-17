import unittest
from unittest.mock import Mock, patch
from src.sound.music_manager import MusicManager
class TestMusicManager(unittest.TestCase):
    def setUp(self):
            self.manager = MusicManager()
            self.audio_path = 'test_audio.mp3'

    @patch('pygame.mixer.init')
    @patch('pygame.mixer.music.set_volume')
    def test_get_volume(self, mock_get_volume, mock_init):
        volume = self.manager.change_volume(.5)
        self.assertAlmostEquals(volume, 0.5)

    @patch('pygame.mixer.init')
    @patch('pygame.mixer.music.play')
    def test_play(self, mock_play, mock_init):
        result = self.manager.play()
        self.assertTrue(result)
        self.assertTrue(self.manager.get_is_playing())  # Accessing private attribute

    @patch('pygame.mixer.init')
    @patch('pygame.mixer.music.pause')
    def test_pause(self, mock_pause, mock_init):
        result = self.manager.pause()
        self.assertFalse(result)
        self.assertFalse(self.manager.get_is_playing())  # Accessing private attribute

    @patch('pygame.mixer.init')
    @patch('os.path.isfile', return_value=True)
    @patch('pygame.mixer.music.load')
    def test_load_existing_file(self, mock_load, mock_isdir, mock_init):
        self.manager.load(self.audio_path)
        mock_load.assert_called_once_with(self.audio_path)

    @patch('pygame.mixer.init')
    @patch('os.path.isfile', return_value=False)
    def test_load_nonexistent_file(self, mock_isdir, mock_init):
        with self.assertRaises(FileNotFoundError):
            self.manager.load(self.audio_path)
if __name__=="__main__":
    unittest.main()