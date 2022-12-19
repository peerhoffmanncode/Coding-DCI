import time
import os


def sec_to_time(start, end):
    seconds = end - start
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{int(hours):0>2}:{int(minutes):0>2}:{int(seconds):0>2}"


def write_file(filename, content):
    with open(filename, "a") as f:
        f.write(content + "\n")


def list_files(file_path: str, files_found: int, dirs_found: int):
    try:
        # breakpoint()
        # Wenn der Pfad ein Verzeichnis ist, dann alle Dateien und Ordner darin auslesen
        if os.path.isdir(file_path):
            for file in os.listdir(file_path):
                # Rekursiver Aufruf für jedes Element im Verzeichnis
                files_found, dirs_found = list_files(
                    os.path.join(file_path, file), files_found, dirs_found
                )
            dirs_found += 1
            write_file(FILENAME, f"DIR: {dirs_found} - {file_path}")
            return files_found, dirs_found
        # Wenn der Pfad eine Datei ist, dann den Namen ausgeben
        else:
            files_found += 1
            write_file(FILENAME, f"FILE: {files_found} - {file_path.split('/')[-1]}")
            return files_found, dirs_found

    except PermissionError:
        # Fehlermeldung ausgeben, wenn keine Berechtigungen vorliegen
        write_file(FILENAME, f"Keine Berechtigungen für {file_path}")
        return files_found, dirs_found


if __name__ == "__main__":
    # Beispielaufruf
    FILENAME = "./rec.txt"
    DIR = "/Volumes/PH_MAIN_SSD/"
    # DIR = "/Users/peerhoffmann/PEERS_DOCUMENTS/"
    write_file(FILENAME, "=== RECURSIVE BASED SEARCH OF ALL DIRS STARTING FROM :")
    write_file(FILENAME, "=== " + DIR)

    start = time.time()
    print("process started and working...")
    files_found, dirs_found = list_files(DIR, 0, 0)
    print(f"This took {sec_to_time(start, time.time())}")
    write_file(
        FILENAME,
        f"This took {sec_to_time(start, time.time())} found {files_found} files and {dirs_found} directories, in sum {files_found + dirs_found} items.",
    )
