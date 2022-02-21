import sys
import os
import venv
import subprocess
import tempfile
import shutil

new_dir = tempfile.mkdtemp()
venv.create(new_dir, with_pip=True)
subprocess.run([os.path.join(new_dir, 'bin','pip'), 'install', 'pyfiglet'])
subprocess.run([os.path.join(new_dir, 'bin', 'python3'), '-m', 'figdate', *sys.argv[1:]])
shutil.rmtree(new_dir)