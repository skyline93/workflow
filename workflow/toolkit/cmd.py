import subprocess

from workflow.config import settings


def run_cmd(cmd, cwd=None, to_file=False, out_file=None, **kwargs):
    print(cmd)
    cmd = cmd.split(" ")

    if to_file is False:
        c = subprocess.run(cmd, cwd=cwd, check=True, **kwargs)
        return c.stdout

    elif to_file is True and out_file is not None:
        fp = open(out_file, "w")
        c = subprocess.run(cmd, cwd=cwd, check=True, stdout=fp, **kwargs)
        fp.flush()
        fp.close()
    else:
        raise Exception("should have 'out_file' param")


def run_app_cmd(cmd, **kwargs):
    cmd = f"{settings.app.pyenv}/{cmd}"
    return run_cmd(cmd, cwd=settings.app.home, **kwargs)
