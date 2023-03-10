from os import walk, makedirs, path
from subprocess import call
from threading import Thread

def test(root, file):
    num = file.split('-')[0]
    outdir = root.replace('7', 'out', 1) + "/" + num

    if not path.exists(outdir):
        makedirs(outdir, exist_ok=True)

    puzzle_filename = root + "/" + file
    smt_filename = outdir + "/" + num + ".smt"

    with open(puzzle_filename, "r") as puzzle:
        with open(smt_filename, "w") as smt:
            with open("/dev/null", "w") as dev_null:
                kenken2smt_response = call("./kenken2smt", stdin=puzzle, stdout=smt, stderr=dev_null)

                if kenken2smt_response != 0:
                    print("kenken2smt failed on " + puzzle_filename)
                    return

    # TODO: run mathsat and then smt2kenken

if __name__ == '__main__':
    dir_stream = walk("7")

    for root, subdirs, files in dir_stream:
        for file in files:
            if file.endswith("-solution.txt"):
                continue

            t = Thread(target=test, args=(root, file))
            t.start()
