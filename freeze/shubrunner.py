import warnings

import shub.tool


# Suppress RuntimeWarnings caused by pip 8.0.0 on Windows
# https://github.com/pypa/pip/issues/3383
# XXX: We should be able to remove this once pip 8.0.1 is published
warnings.simplefilter('ignore', RuntimeWarning)

# Run cli
shub.tool.cli()
