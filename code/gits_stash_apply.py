import subprocess
from subprocess import PIPE
import helper


def gits_stash_apply(args):
    """
    This function is used to execute stash operations and also
    track your stashes easily in a visual manner
    Usage: gits stash
    """
    try:
        stash_executor: list = ["git", "stash", "apply"]

        process0 = subprocess.Popen(stash_executor,
                                    stdout=PIPE, stderr=PIPE)
        stdout, stderr = process0.communicate()
        print(stdout.decode("utf-8"))

        if stderr:
            print(f"Error encountered while applying stashed files: {stderr}")

    except Exception as e:
        print("ERROR: gits stash command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
