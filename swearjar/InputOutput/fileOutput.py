"""Outputs the solved equations and the initial conditions to a file."""


class fileOutput(object):
    """Writes the results and initial conditions to a .txt file."""

    def writeReport(initParams, results, outputName=None):
        """Compose the report through a string and output to a file."""
        with open(outputName, 'w') as f:
            # Hardcoded in results. Maybe a way to generalize for *results?
            f.write("Results"
                    + "\n=======\n"
                    + "Bloot 1: "
                    + "**" + str(results[0]) + "**\n\n"
                    + "Bloot 2: "
                    + "**" + str(results[1]) + "**\n\n"
                    + "Bloot 3: "
                    + "**" + str(results[2]) + "**\n\n"
                    + "Bloot 4: "
                    + "**" + str(results[3]) + "**\n\n")

            headings = initParams.headings()

            for heading in headings:
                if heading != 'Results':
                    f.write(heading + "\n")
                    for num in range(0, len(heading)):
                        f.write("=")
                    f.write("\n")
                    params = initParams.getParamsFromHeading(heading)
                    for param in params:
                        f.write(initParams.getlabel_MD(param)
                                + "**"
                                + str(initParams[param])
                                + "**\n\n")
                    f.write("\n")


if __name__ == "__main__":
    pass
