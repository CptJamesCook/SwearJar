"""Contains the variable to label dictionary as well as a markdown version."""
paramToLabel = {
              'Sorp': 'Investigatam diutissime quaestionem (Sorp): ',
              'Merp': 'At vel nobis comprehensam (Merp): ',
              'Doot': 'Stet clita kasd gubergren (Doot): ',
              'Bloot': 'Consetetur sadipscing elitr, sed diam (Bloot): ',
              'Blort': 'Invidunt ut labore et dolore magna aliquyam (Blort): ',
              'Zarg': 'Justo duo dolores et ea rebumjusto (Zarg): ',
              'banana': 'Justo duo dolores et ea rebumjusto (banana): '
              }

paramToLabel_MD = {
                 'Sorp': 'Investigatam diutissime quaestionem (**Sorp**): ',
                 'Merp': 'At vel nobis comprehensam (**Merp**): ',
                 'Doot': 'Stet clita kasd gubergren (**Doot**): ',
                 'Bloot': 'Consetetur sadipsci elitr, sed diam (**Bloot**): ',
                 'Blort': 'Invidunt ut labore et magna aliquyam (**Blort**): ',
                 'Zarg': 'Justo duo dolores et ea rebumjusto (**Zarg**): ',
                 'banana': 'Justo duo dolores et ea rebumjusto (banana): '
                 }

labelToParam_MD = dict(reversed(item) for item in paramToLabel_MD.items())

if __name__ == "__main__":
    pass
