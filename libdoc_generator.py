from robot import libdoc

in_dir_path = r"..\resources"
out_dir_path = r"."


if  not libdoc.os.path.exists(in_dir_path):
    filename=libdoc.os.path.basename(__file__)
    print(in_dir_path + "existiert nicht.")
    print("Bei relativem Pfad: Wurde "+ filename +" im richtigen Verzeichnis ausgeführt?")

if not libdoc.os.path.exists(out_dir_path):
    libdoc.os.makedirs(out_dir_path)

with libdoc.os.scandir(in_dir_path) as dirs:
    for entry in dirs:
        in_file_path = entry.path
        out_file_name = entry.name.split(".")[0] + ".html"
        out_file_path = libdoc.os.path.join(out_dir_path, out_file_name)
        libdoc.libdoc(in_file_path,out_file_path)
