import warnings

import shub.tool


# Suppress all warnings for the time being (avoid PEP425 RuntimeWarnings)
# TODO: Investigate why they occur in the first place
warnings.simplefilter('ignore')

# Run cli
shub.tool.cli()
