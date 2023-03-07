import os
import time


def sec_to_time(start, end):
    seconds = end - start
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{int(hours):0>2}:{int(minutes):0>2}:{int(seconds):0>2}"


def write_file(filename, content):
    with open(filename, "a") as f:
        f.write(content + "\n")


def list_files(path: str):
    files_found = 0
    dirs_found = 0

    # Liste aller Verzeichnisse und Dateien, die noch nicht bearbeitet wurden
    directories = [path]
    # Solange noch Verzeichnisse vorliegen, die nicht bearbeitet wurden
    while directories:
        try:
            # Verzeichnis aus der Liste entfernen und auslesen
            current_dir = directories.pop()
            for file in os.listdir(current_dir):
                # Vollständigen Pfad für das Element erstellen
                file_path = os.path.join(current_dir, file)
                # Wenn das Element ein Verzeichnis ist, zur Liste hinzufügen
                if os.path.isdir(file_path):
                    directories.append(file_path)
                    dirs_found += 1
                    write_file(FILENAME, f"DIR: {dirs_found} - {file_path}")
                # Wenn das Element eine Datei ist, den Namen ausgeben
                else:
                    files_found += 1
                    write_file(
                        FILENAME, f"FILE: {files_found} - {file_path.split('/')[-1]}"
                    )
        except PermissionError:
            # Fehlermeldung ausgeben, wenn keine Berechtigungen vorliegen
            write_file(FILENAME, f"Keine Berechtigungen für {file_path}")
    return files_found, dirs_found


if __name__ == "__main__":
    # Beispielaufruf
    FILENAME = "./loop.txt"
    DIR = "/Volumes/PH_MAIN_SSD/"
    # DIR = "/Users/peerhoffmann/PEERS_DOCUMENTS/"
    write_file(FILENAME, "=== RECURSIVE BASED SEARCH OF ALL DIRS STARTING FROM :")
    write_file(FILENAME, "=== " + DIR)

    start = time.time()
    print("process started and working...")
    files_found, dirs_found = list_files(DIR)
    print(f"This took {sec_to_time(start, time.time())}")
    write_file(
        FILENAME,
        f"This took {sec_to_time(start, time.time())} found {files_found} files and {dirs_found} directories, in sum {files_found + dirs_found} items.",
    )
