# ---------------------------------------------------------------------------
#
#  ExampleGUI: An example GUI for the ESDLab.
#
#  Copyright (C) 2017 by Energy Systems Design Laboratory, University of Alberta
#
#  This software is distributed under the MIT License.
#  For more information, see LICENSE.txt file
#
#  - Class: fileInput
#  - Description: Reads initial conditions from a file and
#                 outputs to a dictionary.
#  - Developers: J. Cook
#
# ---------------------------------------------------------------------------
"""Reads initial conditions from a file and outputs to a dictionary."""
from examplegui.InputOutput.ParamToLabel import labelToParam_MD


class fileInput(object):
    """Loads data then outputs an initial parameters dictionary."""

    def updateDict(initParams, filename=None):
        """Update and return the initial parameter dictionary from a file."""
        updatedDict = {}
        if filename is not None:
            with open(filename) as f:
                content = f.readlines()
            # remove white space
            content = [x.strip('\n') for x in content]

            for itm in content:
                for key in labelToParam_MD.keys():
                    if itm.find(key) == 0:
                        stripedStr = itm[len(key):]
                        stripedStr = stripedStr.strip('*')
                        try:
                            updatedDict[labelToParam_MD[key]] = float(stripedStr)
                        except ValueError:
                            updatedDict[labelToParam_MD[key]] = stripedStr
                        break

        initParams.update(updatedDict)
        return initParams


if __name__ == "__main__":
    pass
