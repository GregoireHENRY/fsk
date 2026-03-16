#!/usr/bin/env python

import fsk

path_mk = "/Users/gregoireh/data/spice/wgc/mk/solar_system_v0060.tm"
url_root = "https://naif.jpl.nasa.gov/pub/naif/pds/wgc/kernels"
fsk.fetch_metakernel(path_mk, url_root, overwrite=False)
