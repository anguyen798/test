import filecmp
import os.path

def comparedirectory(dir1, dir2):
    dirs_cmp = filecmp.dircmp(dir1, dir2)
    if len(dirs_cmp.left_only)>0 or len(dirs_cmp.right_only)>0 or \
        len(dirs_cmp.funny_files)>0:
        return False
    (_, mismatch, errors) =  filecmp.cmpfiles(dir1, dir2, dirs_cmp.common_files, shallow=False)
    if len(mismatch)>0 or len(errors)>0:
        return False
    for common_dir in dirs_cmp.common_dirs:
        new_dir1 = os.path.join(dir1, common_dir)
        new_dir2 = os.path.join(dir2, common_dir)
        if not comparedirectory(new_dir1, new_dir2):
            return False
    return True

def main():
    a=input("Enter path to first directory: ")
    b=input("Enter path to second directory: ")
    if comparedirectory(a,b):
            print("Two directories are equal")
    else:
            print("Two directories are different")
main()

