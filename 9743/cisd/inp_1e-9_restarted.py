#!/usr/bin/env python
# Author: Nike Dattani, nike@hpqc.org

import numpy as np
import pyscf
from pyscf import gto, scf, ao2mo, fci,ci

mol = pyscf.M(atom = 'Ne 0 0 0',basis = 'cc-pv5z',verbose=5,output='out_1e-9_restarted.txt')
mhf = scf.RHF(mol).run()
mci = ci.CISD(mhf).set(conv_tol=1e-9,nroots=3)
e, civec = mci.kernel(ci0=np.load('civec.npy'))
