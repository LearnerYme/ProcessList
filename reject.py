import sys

usage = '''
    Usage:
        python3 reject.py file.list run.list bad.run.list tag [tag2 (optional)] rloc

    :Args 5
    :file.list      :       The path to full file list.
    :run.list       :       The path to full run list.
    :bad.run.list   :       The path to bad run list.
    :tag            :       Tag of prefered good run and file list.
    :rloc           :       Index of run number in a file path.

    For example, the total file and run lists are 'full.file.list' and 'full.run.list', and bad run list is 'bad.run.list',
    you want good file and run lists to be 'rsd.file.list' and 'rsd.run.list', please do: 'python3 reject.py full.file.list full.run.list bad.run.list rsd 9'.

    If you don't want the good run and file list having the same name, tag is for good file list and tag2 for good run list.
    Note that you will need to add subfix for the lists with this mode. Example: 'python3 reject.py full.file.list full.run.list bad.run.list wow.file.list uwu.run.list 9'.
    
'''

if len(sys.argv) == 6: # same mode
    full_file_list = sys.argv[1]
    full_run_list = sys.argv[2]
    bad_run_list = sys.argv[3]
    tag = sys.argv[4]

    good_file_list = f'{tag}.file.list'
    good_run_list = f'{tag}.run.list'

    rloc = int(sys.argv[5])

elif len(sys.argv) == 7: # specified save name
    full_file_list = sys.argv[1]
    full_run_list = sys.argv[2]
    bad_run_list = sys.argv[3]

    good_file_list = sys.argv[4]
    good_run_list = sys.argv[5]

    rloc = int(sys.argv[6])

else: # print usage
    print(usage)
    exit(0)

ffl = open(full_file_list).readlines()
frl = open(full_run_list).readlines()
brl = open(bad_run_list).readlines()

nffl = len(ffl)
nfrl = len(frl)
nbrl = len(brl)

print(f'Full file list ({nffl}): {full_file_list}')
print(f'Full run list ({nfrl}): {full_run_list}')
print(f'Bad run list ({nbrl}): {bad_run_list}')

frl = [item.strip() for item in frl]
brl = [item.strip() for item in brl]

grl = [item for item in frl if item not in brl]
gfl = []

for item in ffl:
    cur_run = item.split('/')[rloc]
    if cur_run in brl:
        continue
    gfl.append(item)

with open(good_file_list, 'w') as f:
    for item in gfl:
        f.write(item)
with open(good_run_list, 'w') as f:
    for item in grl:
        f.write(f'{item}\n')

print(f'There are {len(grl)} good runs with {len(gfl)} files left after the rejection. This is the end of this program.')
