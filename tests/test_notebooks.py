import os
import glob
import pytest

from testbook import testbook

notebook_files = glob.glob("notebooks/**/*.ipynb", recursive=True)

# FIXME: Mark some tests xfail for now.
def mark_xfail(nb, **kwargs):
    nb_index = None
    for i, nb_file in enumerate(notebook_files):
        if nb in nb_file:
            nb_index = i

    if nb_index is None:
        raise ValueError(f"Cannot set notebook {nb} to xfail because it could not be found")

    notebook_files[nb_index] = pytest.param(nb, marks=pytest.mark.xfail(**kwargs))

mark_xfail('htfa.ipynb', reason="Index out of range error")
mark_xfail('rtcloud_notebook.ipynb', reason="Needs to have a web server installed, will probably need to run this in singularity on della")

@pytest.fixture(autouse=True)
def chdir_back_to_root():
    """
    This fixture sets up and tears down state before each example is run. Certain examples
    require that they are run from the local directory in which they reside. This changes
    directory. It reverses this after the test finishes.
    """

    # Get the current directory before running the test
    cwd = os.getcwd()

    yield

    # After the test, we need chdir back to root of the repo
    os.chdir(cwd)


@pytest.mark.parametrize("notebook_file", notebook_files)
def test_notebook(notebook_file):

    os.chdir(os.path.dirname(notebook_file))

    with testbook(os.path.basename(notebook_file), execute=True, timeout=3600) as tb:
        pass