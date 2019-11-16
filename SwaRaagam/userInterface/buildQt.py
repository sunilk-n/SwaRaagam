import os
import subprocess
import sys

from glob import glob
from distutils.cmd import Command
from datetime import datetime
import SwaRaagam

class BuildQt(Command):
    """ Defines a command for setup.py that compiles the *.ui and *.qrc files
        into python files.
        It looks for *.ui files in _UI_PATH subfolder.
    """
    _UI_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uiModels')
    description = "Run the PyQtUi files and generate `.py` files"
    user_options = [
        # The format is (long option, short option, description).
        # ('license=', None, 'Add license to python files'),
    ]

    def initialize_options(self):
        """
        Sets the proper command names for the compiling tools.
        """
        self.pyuic = 'pyside2-uic'
        projDir = SwaRaagam.__path__[0]
        licenseFile = os.path.join(projDir, os.path.pardir, 'docs', 'license.txt')
        self.license = "Here comes the doc strings to be added"
        if os.path.exists(licenseFile):
            with open(licenseFile) as fd:
                data = fd.readlines()
            self.license = "".join(data)

    def finalize_options(self):
        pass

    def _compile_ui(self, infile, outfile):
        try:
            subprocess.call([self.pyuic, infile, '-o', outfile])
        except OSError:
            print("uic command failed - make sure that pyside-uic "
                  "is in your $PATH")

    def _compileDocstrings(self, outfile):
        docs = """{}
        
        Created By: Sunil Kumar Nerella            
        """.format(self.license)
        now = datetime.now()
        currentTime = now.strftime("%d/%m/%Y %H:%M:%S")
        with open(outfile) as fd:
            code = fd.readlines()

        with open(outfile, 'w') as fd:
            fd.write('"""{}Generated on: {}\n"""'.format(docs, currentTime))
            for eachLine in code[9:]:
                fd.write(eachLine)

    def run(self):
        # compile ui files
        for infile in glob(os.path.join(self._UI_PATH, '*.ui')):
            directory, ui_filename = os.path.split(infile)
            py_filename = ui_filename.replace('.ui', '.py')
            outfile = os.path.join(directory, py_filename)
            print("Compiling: {0} -> {1}".format(infile, outfile))
            self._compile_ui(infile, outfile)
            self._compileDocstrings(outfile)
