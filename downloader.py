import subprocess
import sys
import urllib

from settings import FOLDERS

arxiv_id = sys.argv[1]
user_input = sys.argv[2]

arxiv_download_url_template = "https://arxiv.org/pdf/%s.pdf"
tmp_folder = "/tmp/papers"
tmp_paper_template = tmp_folder + "/%s.pdf"

downloaded = False

num_folders = len(FOLDERS) + 1
highest_input_character = chr(num_folders + ord('0'))

for command in user_input:
    if not downloaded and highest_input_character > command > '0':
        subprocess.call(['mkdir', '-p', tmp_folder])
        urllib.urlretrieve(arxiv_download_url_template % arxiv_id, tmp_paper_template % (arxiv_id))
        downloaded = True
    if highest_input_character > command > '0':
        subprocess.call(['cp', tmp_paper_template % arxiv_id, FOLDERS[int(command) - 1]])
