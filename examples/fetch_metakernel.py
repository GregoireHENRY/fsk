#!/usr/bin/env python

import fsk

fsk.core.fetch_metakernel(
    "/Users/gregoireh/projects/fetch-spice-kernels/out/mk/hera_study_v000.tm",
    "https://spiftp.esac.esa.int/data/SPICE/HERA/kernels/",
    overwrite=True,
)
