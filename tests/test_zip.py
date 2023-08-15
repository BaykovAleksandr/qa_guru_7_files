import os
import zipfile
from conftest import RESOURCES_DIR


def test_zip_file():
    with zipfile.ZipFile(os.path.join(RESOURCES_DIR, 'file_hello.zip')) as zip_file:
        zip_file.extract('file_hello.txt', path=RESOURCES_DIR)
        name_list = zip_file.namelist()
        print(name_list)
        text = zip_file.read('file_hello.txt')
        print(text)
        assert 'file_hello.txt' in name_list
        assert text == b'Hello'
        assert os.path.isfile(os.path.join(RESOURCES_DIR, 'file_hello.txt'))

        os.remove(os.path.join(RESOURCES_DIR, 'file_hello.txt'))
