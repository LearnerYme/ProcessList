# conditions
prod=P21ic
name=production_19GeV_2019
ftype=daq_reco_picoDst
storage=nfs
storageSign=
# run id location
# usually, 10 for NFS, 12 for local or hpss
rloc=10

all: help

get:
	@echo "Now getting raw list from server."
	get_file_list.pl -keys path,filename -cond production=$(prod),trgsetupname=$(name),filetype=$(ftype),storage$(storageSign)=$(storage) -limit 0 -delim / > raw.list
	sort -t '/' -k $(rloc) raw.list > file.list
	cut -d '/' -f $(rloc) file.list | sort | uniq > run.list
	@echo "Done."

add:
	@echo "Now adding prefix (only for root files from D.D.)."
	sed -i "s/^\/home\/starlib/root:\/\/xrdstar\.rcf\.bnl\.gov:1095\/\/home\/starlib/g" file.list
	@echo "Done."

rej: reject.py
	@echo "Please run python3 file.list run.list bad.run.list tag. Details see make help."

reject: rej

help:
	@echo "=================================="
	@echo "Quick Start"
	@echo "1. run 'make get' to get raw file list."
	@echo "2. run 'make add' to add the prefix for those path which is in D.D. (instead of NFS)."
	@echo "3. if you want to reject bad runs, prepare the bad run list, and run 'python3 reject.py file.list run.list bad.run.list tag', here file.list is the full file list, run.list is the run list, bad.run.list is the bad run list, and tag is the prefered new list (for run and file)."
	@echo "Note that, you may need to modify some arguments in this 'Makefile', and 'rloc' in 'reject.py'."
	@echo "You can find more information about the dataset in the following webpage:"
	@echo "https://www.star.bnl.gov/public/comp/prod/DataSummary.html"
	@echo "Quick Get List Script v2.0"
	@echo "By yghuang"
	@echo "v3.0: July 26th 2023"
	@echo "v2.0: July 19th 2023"
	@echo "v1.0: May  19th 2022"
	@echo "=================================="

