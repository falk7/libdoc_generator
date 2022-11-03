from enum import Enum

from robot import libdoc, testdoc


class DocType(Enum):
    KEYWORDS = 'libdoc'
    TESTS = 'testdoc'       

def create_doc_for_dir(doc_type:DocType, in_path:str, out_path:str) -> None:
    check_path_exists(in_path)

    with testdoc.os.scandir(in_path) as dirs:
        for entry in dirs:
            if entry.is_dir():
                new_out_path = testdoc.os.path.join(out_path, entry.name)
                create_doc_for_dir(entry.path, new_out_path)
            else:
                in_file_path = entry.path
                out_file_name = entry.name.split(".")[0] + ".html"
                out_file_path = testdoc.os.path.join(out_path, out_file_name)

                if doc_type==DocType.KEYWORDS:
                    libdoc.libdoc(in_file_path, out_file_path)
                elif doc_type==DocType.TESTS:
                    testdoc.testdoc(in_file_path, out_file_path)


def check_path_exists(path:str):
    if  not libdoc.os.path.exists(path):
        filename=libdoc.os.path.basename(__file__)
        print(path + "existiert nicht.")
        print("Bei relativem Pfad: Wurde "+ filename +" im richtigen Verzeichnis ausgeführt?")

                                
def main():
    resource_in_dir_path = r"..\resources"
    tests_in_dir_path = r"..\tests"

    resource_out_dir_path = r".\keywords"
    tests_out_dir_path = r".\tests"

    create_doc_for_dir(DocType.KEYWORDS,resource_in_dir_path, resource_out_dir_path)
    create_doc_for_dir(DocType.TESTS,tests_in_dir_path, tests_out_dir_path)

if __name__ == "__main__":
    main()



