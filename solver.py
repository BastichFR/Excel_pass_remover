import os
import sys

from src.GUI import run_gui, get_selected_files
from src.FileHandling import operator

def main():
    run_gui()
    operator(get_selected_files())
    
if __name__ == "__main__":
    main()