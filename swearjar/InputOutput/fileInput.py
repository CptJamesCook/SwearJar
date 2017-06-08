"""Reads initial conditions from a file and outputs to a dictionary."""


class fileInput(object):
    """Loads data then outputs an initial parameters dictionary."""

    def updateDict(initParams, filename=None):
        """Update and return the initial parameter dictionary from a file."""
        labelToParam_MD = initParams.labelToParam_MD()
        if filename is not None:
            with open(filename) as f:
                content = f.readlines()
            # remove new line char
            content = [x.strip('\n') for x in content]

            for itm in content:
                for label in initParams.labels_MD():
                    if itm.find(label) == 0:
                        stripedStr = itm[len(label):]

                        val = stripedStr.strip('*')
                        param = labelToParam_MD[label]

                        try:
                            initParams[param] = float(val)
                        except ValueError:
                            initParams[param] = val
                        break

        return initParams


if __name__ == "__main__":
    pass
