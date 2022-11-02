from robot import libdoc


def create_libdoc_for_dir(in_path: str, out_path: str) -> None:
    with libdoc.os.scandir(in_path) as dirs:
        for entry in dirs:
            if entry.is_dir():
                new_out_path = libdoc.os.path.join(out_path, entry.name)
                create_libdoc_for_dir(entry.path, new_out_path)
            else:
                in_file_path = entry.path
                out_file_name = entry.name.split(".")[0] + ".html"
                out_file_path = libdoc.os.path.join(out_path, out_file_name)
                libdoc.libdoc(in_file_path, out_file_path)

def main():
    in_dir_path = r"..\resources"
    out_dir_path = r"."

    if  not libdoc.os.path.exists(in_dir_path):
        filename=libdoc.os.path.basename(__file__)
        print(in_dir_path + "existiert nicht.")
        print("Bei relativem Pfad: Wurde "+ filename +" im richtigen Verzeichnis ausgeführt?")

    if not libdoc.os.path.exists(out_dir_path):
        libdoc.os.makedirs(out_dir_path)

    create_libdoc_for_dir(in_dir_path, out_dir_path)

if __name__ == "__main__":
    main()



