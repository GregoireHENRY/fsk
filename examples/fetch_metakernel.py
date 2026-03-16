#!/usr/bin/env python

import fsk

# wgc https://naif.jpl.nasa.gov/pub/naif/pds/wgc/kernels
# orex https://naif.jpl.nasa.gov/pub/naif/pds/pds4/orex/orex_spice/spice_kernels
# hera https://spiftp.esac.esa.int/data/SPICE/HERA/kernels

fsk.core.fetch_metakernel(
    "/Users/gregoireh/projects/fetch-spice-kernels/out/mk/hera_study_v000.tm",
    "https://spiftp.esac.esa.int/data/SPICE/HERA/kernels/",
    overwrite=True,
)