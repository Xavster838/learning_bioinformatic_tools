#June 23, 2021: Trying out recan simgen to generate window aligner plots for my CYP2D duplicons
from recan.simgen import Simgen
import os

#specify prototype data
HOME_DIR="os.getcwd()"
#input data needs to be an MSA
proto_fa="prototype_data/sample_CYP2D6_duplicons.fa" 

sim_obj = Simgen(proto_fa)