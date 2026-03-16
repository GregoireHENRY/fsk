#!/usr/bin/env python

import fsk

path_mk = "/Users/gregoireh/data/spice/tmp/mk/hera_crema_2_0_LPC_ECP_PDP.tm"
url_root = "https://s2e2.cosmos.esa.int/bitbucket/projects/SPICE_KERNELS/repos/hera/raw/kernels"
fsk.fetch_metakernel(path_mk, url_root, overwrite=False)