#!/usr/bin/env python

import fsk

path_mk = "/Users/gregoireh/data/spice/tmp/mk/orx_2023_v01.tm"
url_root = "https://naif.jpl.nasa.gov/pub/naif/pds/pds4/orex/orex_spice/spice_kernels"
fsk.fetch_metakernel(path_mk, url_root, overwrite=False)
