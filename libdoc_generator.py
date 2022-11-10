from robot import libdoc, testdoc


def create_libdoc_for_dir(in_path:str, out_path:str) -> None:
    check_path_exists(in_path)

    with testdoc.os.scandir(in_path) as dirs:
        for entry in dirs:
            if entry.is_dir():
                new_out_path = testdoc.os.path.join(out_path, entry.name)
                create_libdoc_for_dir(entry.path, new_out_path)
            else:
                split_name = entry.name.split(".")
                if split_name[1] != "resource":
                    break

                in_file_path = entry.path
                out_file_name = split_name[0] + ".html"
                out_file_path = libdoc.os.path.join(out_path, out_file_name)

                libdoc.libdoc(in_file_path, out_file_path)

def create_testdoc_for_dir(in_path:str, out_path:str) -> None:
    check_path_exists(in_path)

    with testdoc.os.scandir(in_path) as dirs:
        for entry in dirs:
            if entry.is_dir():
                new_out_path = testdoc.os.path.join(out_path, entry.name)
                create_testdoc_for_dir(entry.path, new_out_path)
            else:
                split_name = entry.name.split(".")
                if split_name[1] != "robot":
                    break

                in_file_path = entry.path
                out_file_name = split_name[0] + ".html"
                out_file_path = testdoc.os.path.join(out_path, out_file_name)

                testdoc.testdoc(in_file_path, out_file_path)


def check_path_exists(path:str):
    if  not libdoc.os.path.exists(path):
        filename=libdoc.os.path.basename(__file__)
        error_message = f'{path} existiert nicht. Bei relativem Pfad: Wurde {filename} im richtigen Verzeichnis ausgeführt? Aktueller Arbeitspfad: {libdoc.os.getcwd()}'

        raise FileNotFoundError(error_message)

                                
def main():
    resource_in_dir_path = r".\resources"
    tests_in_dir_path = r".\tests"

    resource_out_dir_path = r".doc\keywords"
    tests_out_dir_path = r".doc\tests"

    create_libdoc_for_dir(resource_in_dir_path, resource_out_dir_path)
    create_testdoc_for_dir(tests_in_dir_path, tests_out_dir_path)

if __name__ == "__main__":
    main()



