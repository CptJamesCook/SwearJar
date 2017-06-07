"""Outputs the solved equations and the initial conditions to a file."""
from swearjar.InputOutput.HeadingToParams import _dict as headToParams
from swearjar.InputOutput.ParamToLabel import paramToLabel_MD


class fileOutput(object):
    """Writes the results and initial conditions to a .txt file."""

    def writeReport(initParams, results, outputName=None):
        """Compose the report through a string and output to a file."""
        with open(outputName, 'w') as f:
            f.write("Results"
                    + "\n=======\n"
                    + "The resulting results, resulting "
                    + "in (**Results1**): "
                    + "**" + str(results[0]) + "**\n\n"
                    + "The resulting results, resulting "
                    + "in (**Results2**): "
                    + "**" + str(results[1]) + "**\n\n"
                    + "The resulting results, resulting "
                    + "in (**Results3**): "
                    + "**" + str(results[2]) + "**\n\n")

            for heading in headToParams.keys():
                numOfEqualSigns = len(heading)

                f.write(heading + "\n")
                for num in range(0, numOfEqualSigns):
                    f.write("=")
                f.write("\n")

                for param in headToParams[heading]:
                    f.write(paramToLabel_MD[param]
                            + "**" + str(initParams[param]) + "**\n\n")
                f.write("\n")


if __name__ == "__main__":
    pass
