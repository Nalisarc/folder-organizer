#!/usr/bin/env python3
import unittest
import os
import shutil
import sorter
class TestScript(unittest.TestCase):
    def setUp(self):
        #make test env
        if not os.path.isdir("./testenv"):
            os.mkdir("testenv")
        else:
            pass

        #Move into testenv
        os.chdir("./testenv")

        #make dummy files
        open("test.jpg",'a').close()
        open("test.mp3",'a').close()
        open("test.mp4",'a').close()
        open("test.zip",'a').close()
        open("test.pdf",'a').close()
        open("test.nyxie","a").close()

    def tearDown(self):
        os.chdir("../")
        shutil.rmtree("./testenv")

    def test_can_make_folders(self):
        if os.path.isdir("./Music"):
            shutil.rmtree("./Music")
        sorter.mkdirs()
        self.assertIn("Music", next(os.walk('.'))[1],
                         msg="Error Folder Not Present After Created"
        )

    def test_can_move_files(self):
        sorter.mkdirs()
        self.assertTrue(os.path.isfile("test.mp3"))
        sorter.movefiles()
        self.assertTrue(os.path.isfile("Music/test.mp3"))
        open("test.mp3","a").close()

    def test_doesnt_move_wrong_files(self):
        sorter.mkdirs()
        self.assertTrue(os.path.isfile("test.mp3"))
        sorter.movefiles()
        self.assertFalse(os.path.isfile("Documents/test.mp3"))

    def test_do_nothing_if_dir_empty(self):
        os.mkdir("./empty")
        os.chdir("./empty")
        sorter.main()
        self.assertEqual(len(os.listdir('.')),0)
        os.chdir("../")

    def test_doesnt_do_recurrsive(self):
        os.mkdir("dont-touch")
        open("dont-touch/test.pdf","a").close()
        sorter.main()
        self.assertFalse(os.path.isdir("dont-touch/Music"))

    def test_doesnt_touch_unknown_files(self):
        self.assertTrue(os.path.isfile("test.nyxie"))
        sorter.main()
        self.assertTrue(os.path.isfile("test.nyxie"))


if __name__ == '__main__':
    unittest.main()
