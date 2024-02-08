import zipfile
import os


def open_zip_file(zip_file_path, mode):
    try:
        zip_ref = zipfile.ZipFile(zip_file_path, mode)
        return zip_ref
    except zipfile.BadZipFile:
        print("Le fichier n'est pas un fichier ZIP valide.")
        return None

# extract_zip_file(zip_ref, "xl/worksheets/sheet*.xml", os.getcwd()):
def extract_zip_file(zip_ref, destination):
    files = []
    for file in zip_ref.namelist():
        if file.startswith("xl/worksheets/sheet") and file.endswith(".xml"):
            zip_ref.extract(file, destination)
            files.append(file)
        if file.startswith("xl/workbook.xml"):
            zip_ref.extract(file, destination)
            files.append(file)
    return files


def overwrite_zip_file(zip_file_path, extracted_files):      
    temp_zip_path = zip_file_path + '.temp'
    os.rename(zip_file_path, temp_zip_path)

    with zipfile.ZipFile(temp_zip_path, 'r') as old_zip, \
         zipfile.ZipFile(zip_file_path, 'w') as new_zip:
        
        # Copier tous les fichiers du fichier ZIP original sauf ceux à écraser
        for item in old_zip.infolist():
            if item.filename not in extracted_files:
                buffer = old_zip.read(item.filename)
                new_zip.writestr(item, buffer)

        # Ajouter les nouveaux fichiers pour les écraser dans le ZIP avec leur chemin relatif
        for file in extracted_files:
            new_zip.write(file, arcname=os.path.relpath(file))

    # Supprimer le fichier temporaire
    os.remove(temp_zip_path)


