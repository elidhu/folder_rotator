from folder_rotator import Rotator
import os


def touch(path):
    with open(path, 'a'):
        os.utime(path, None)


def test_init(tmpdir):
    fr = Rotator(tmpdir)
    assert fr, "Object not created."


def test_get_output_path(tmpdir):
    fr = Rotator(tmpdir)
    path = fr.get_output_path()
    pathlist = os.path.split(path)
    output_folder = pathlist[-1]
    assert output_folder == "output_folder_0000", "Output folder not created with the expected name"


def test_increment_output_folder(tmpdir):
    fr = Rotator(tmpdir, max_output_files=1)
    testfile = 'temp.txt'
    for i in range(5):
        path = fr.get_output_path()
        pathlist = os.path.split(path)
        output_folder = pathlist[-1]
        assert output_folder == f"output_folder_000{i}", "Output folder not incremented as expected"
        touch(os.path.join(fr.get_output_path(), testfile))


def test_folder_already_exists(tmpdir):
    fr = Rotator(tmpdir, max_output_files=1)
    testfile = 'temp.txt'
    touch(os.path.join(fr.get_output_path(), testfile))
    fr = Rotator(tmpdir, max_output_files=1)
    assert fr.current_output_folder_index == 1, "Failed to initialise to the correct index when folders already exist"
    touch(os.path.join(fr.get_output_path(), testfile))
    fr = Rotator(tmpdir, max_output_files=1)
    assert fr.current_output_folder_index == 2, "Failed to initialise to the correct index when folders already exist"
