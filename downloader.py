import subprocess
import sys
import urllib

arxiv_id = sys.argv[1]
user_input = sys.argv[2]

arxiv_download_url_template = "https://arxiv.org/pdf/%s.pdf"
tmp_folder = "/tmp/papers"
tmp_paper_template = tmp_folder + "/%s.pdf"

folders = ['/Users/erdicalli/Documents/papers/neurant/',
           '/Users/erdicalli/Documents/papers/internship/',
           '/Users/erdicalli/Documents/papers/fundamental/',
           '/Users/erdicalli/Documents/papers/interesting/']

downloaded = False
for command in user_input:
    if not downloaded and '5' > command > '0':
        subprocess.call(['mkdir', tmp_folder])
        urllib.urlretrieve(arxiv_download_url_template % arxiv_id, tmp_paper_template % (arxiv_id))
        downloaded = True
    if '5' > command > '0':
        subprocess.call(['cp', tmp_paper_template % arxiv_id, folders[int(command) - 1]])
