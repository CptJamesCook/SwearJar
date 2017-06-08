"""
Contains the initial parameters dictionary.

Adding new features with new parameters should be done here. How the data
object works is described within the class.

Credit:https://stackoverflow.com/questions/3387691/how-to-perfectly-override-a-dict
"""
from collections.abc import MutableMapping


class InitialParameters(MutableMapping):
    """
    A dictionary where the variables can have a heading, label and label_MD.

    This class overloads the basic MutableMapping class. This gives the object
    flexibility to add functionality like adding a heading, a label, and a
    label with markdown (label_MD) to each parameter.

    - heading: Used to sort the different variables under a sub-section. This
               is used to create different tabs as well as outputting the
               results.
    - label: This is the text used in the GUI to describe the parameter.
    - label_MD: This is the text used in outputting the results to describe
                the parameter.

    Remember: It's a feature to keep the heading parameters sorted,
              so the order of parameters in the tuple counts.
              i.e. (C1, C2, C3) shows up as C1, C2, C3 in the GUI,
              and in the output text file.

    """

    _headings = []
    _labels = []
    _labels_MD = []

    def __init__(self, *args, **kwargs):
        """Initialize a dictionary with appropriate arguments."""
        self.store = dict()
        self.heading = dict()
        self.label = dict()
        self.label_MD = dict()
        self.update(dict(*args, **kwargs))

    def __getitem__(self, key):
        """The get item function of a dictionary."""
        return self.store[key]

    def __setitem__(self, key, value):
        """The set item function of a dictionary."""
        self.store[key] = value

    def __delitem__(self, key):
        """The delete function of a dictionary."""
        del self.store[key]
        del self.heading[key]
        del self.label[key]
        del self.label_MD[key]

    def __iter__(self):
        """The iter function of a dictionary."""
        return iter(self.store)

    def __len__(self):
        """The length function of a dictionary."""
        return len(self.store)

    def setlabel(self, label, *params):
        """Set one label for one or more parameters."""
        if label not in self._labels:
            self._labels.append(label)
        for param in params:
            self.label[param] = label

    def setlabels(self, **kwargs):
        r"""
        Set multiple labels for multiple parameters.

        Proper useage of this would be either a dictionary decomposed with
        \*\* notation or a series of params=label.
        """
        for param, label in kwargs.items():
            self.setlabel(label, param)

    def getlabel(self, param):
        """
        Return a label for a given parameter.

        Default is None.
        """
        try:
            label = self.label[param]
        except KeyError:
            print("No label has been set for " + param)
            label = param
        return label

    def labels(self):
        """Return a list containing all labels."""
        return self._labels

    def setlabel_MD(self, label, *params):
        """Set one markdown label for one or more parameters."""
        if label not in self._labels_MD:
            self._labels_MD.append(label)
        for param in params:
            self.label_MD[param] = label

    def setlabels_MD(self, **kwargs):
        r"""
        Set multiple markdown labels at once.

        Proper useage of this would be either a dictionary decomposed with
        \*\* notation or a series of params=label_MD.
        """
        for param, label in kwargs.items():
            self.setlabel_MD(label, param)

    def getlabel_MD(self, param):
        """The get label function for the dictionary."""
        try:
            label = self.label_MD[param]
        except KeyError:
            print("No markdown label has been set for " + param)
            label = param
        return label

    def labels_MD(self):
        """Return a list containing all markdown labels."""
        return self._labels_MD

    def setheading(self, heading, *params):
        """Add the parameters to the headings definition."""
        if heading not in self._headings:
            self._headings.append(heading)
        paramsList = []
        for param in params:
            if param in self.store.keys():
                paramsList.append(param)
        self.heading[heading] = tuple(paramsList)

    def setheadings(self, **kwargs):
        r"""
        Add multiple definitions to different headings.

        Proper useage of this would be either a dictionary decomposed with
        \*\* notation or a series of heading=params. Params should be either a
        list or a tuple.
        """
        for heading, params in kwargs.items():
            self.setheading(heading, *params)

    def getParamsFromHeading(self, heading):
        """Return a tuple of params corresponding to a heading."""
        return self.heading[heading]

    def headings(self):
        """Return a list containing all headings."""
        return self._headings

    def labelToParam(self):
        """Return dict mapping a label to corresponding parameter."""
        return {v: k for k, v in self.label.items()}

    def labelToParam_MD(self):
        """Return dict mapping a markdown label to corresponding parameter."""
        return {v: k for k, v in self.label_MD.items()}


# Initialize the initial parameters with default values.
initParams = InitialParameters({
                        'Sorp': 9000,
                        'Merp': 420,
                        'Doot': 69,
                        'banana': 42069,
                        'Bloot': 9001,
                        'Blort': 2001,
                        'Zarg': 5138008
                                })

# Divide the parameters by headings.
initParams.setheadings(**{
                        'Example Tab 1': ('Sorp', 'Merp', 'Doot', 'banana'),
                        'Example Tab 2': ('Bloot', 'Blort', 'Zarg', 'banana')
                           })

# Set the label for each parameter. This shows up on the GUI.
initParams.setlabels(**{
                        'Sorp': 'Sorp',
                        'Merp': 'Merp',
                        'Doot': 'Doot',
                        'banana': 'banana',
                        'Bloot': 'Bloot',
                        'Blort': 'Blort',
                        'Zarg': 'Zarg'
                            })

# Set the markdown label for each parameter. This shows up on the output file.
initParams.setlabels_MD(**{
                        'Sorp': '**Sorp**',
                        'Merp': '**Merp**',
                        'Doot': '**Doot**',
                        'banana': '**banana**',
                        'Bloot': '**Bloot**',
                        'Blort': '**Blort**',
                        'Zarg': '**Zarg**'
                        })


if __name__ == "__main__":
    pass
