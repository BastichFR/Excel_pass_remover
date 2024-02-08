import xml.etree.ElementTree as ET
import multiprocessing
import os

from src.file_io import copy_file, move_file, create_folder, remove_folder
from src.zip_io import open_zip_file, extract_zip_file, overwrite_zip_file


def remove_xml_tag(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    elements_to_remove = []

    for elem in root.iter():
        if elem.tag and ('Protection' in elem.tag or 'fileSharing' in elem.tag):
            elements_to_remove.append(elem)

    for elem in elements_to_remove:
        if type(elem) == ET.Element:
            elem.clear()
            root.remove(elem)
            
    tree.write(xml_file)


def processing(file):
    
    actual_path = os.getcwd()
    new_path = actual_path + "/tmp" + f"/{os.getpid()}"

    create_folder(new_path)
    os.chdir(new_path)

    print(f"Processing (PID = {os.getpid()}) : {os.path.basename(file)}")

    # .xlsx -> .zip
    newfilename, _ = os.path.splitext(os.path.basename(file))
    temp_path = os.getcwd() + "/" + newfilename + ".zip"
    copy_file(file, temp_path)

    # .xlsx -> .xml
    zip_ref = open_zip_file(temp_path, 'r')
    
    
    if not zip_ref:
        print(f"Error while prodcessing {file}")
        return
    
    extracted_files = extract_zip_file(zip_ref, new_path)
    for file in extracted_files:
        remove_xml_tag(file)

    # .xml -> .zip
    overwrite_zip_file(temp_path, extracted_files)

    # .zip -> .xlsx
    create_folder(actual_path + "/out")
    move_file(temp_path, actual_path + "/out/" + newfilename + ".xlsx")

    print(f"Processing ended (PID = {os.getpid()}) : {os.path.basename(file)}")

    zip_ref.close()
    os.chdir(actual_path)


def operator(list_of_files):

    create_folder(os.getcwd() + "/tmp")

    processes = []
    for file in list_of_files:
        if not os.path.exists(file):
            print(f"File {file} does not exist")
            continue
        if not os.path.isfile(file):
            print(f"{file} is not a file")
            continue

        process = multiprocessing.Process(target=processing, args=(file,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    remove_folder(os.getcwd() + "/tmp")
