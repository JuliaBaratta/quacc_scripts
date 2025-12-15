from ase.io import read
from quacc.calculators.vasp import Vasp
from shutil import copy
import os 
import json
from pprint import pprint
os.environ["QUACC_WORKFLOW_ENGINE"] = "jobflow"
from monty.serialization import loadfn
from jobflow import Flow
from jobflow_remote import submit_flow, set_run_config
from jobflow import job

@job 
def relax(atoms): 
    results = Vasp(atoms, preset="RosenSetPBE", isif=3, nsw=200, kspacing = 0.4, lwave = True)
    atoms.calc = results
    atoms.get_potential_energy()
    return atoms
@job
def single_point(atoms):
    results = Vasp(atoms, preset="RosenSetPBE", isif=2, nsw=0, lwave = True, lcharg = True, lelf = True)
    atoms.calc = results
    atoms.get_potential_energy()
    return atoms
