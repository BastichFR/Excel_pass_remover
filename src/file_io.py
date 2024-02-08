import shutil
import os

def copy_file(src, dst):
    shutil.copy(src, dst)

def move_file(src, dst):
    shutil.move(src, dst)

def create_folder(folder):
    os.makedirs(folder, exist_ok=True)

def remove_folder(folder):
    shutil.rmtree(folder)
