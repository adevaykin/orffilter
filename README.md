# Python script for obsolete ORF files removal

## What?

The script was created to remove ORF files from the home photo archieve. JPGs are usually removed by hand while filtering good photos from photo sessions, while ORF files are backed up. ORF files corresponding to the manually removed JPGs should be removed too, as they don't have any value. This script does the job.

1. Find all ORF files in the specified directory recursively
2. Find all JPG and JPEG files in the specified directory recursively
3. Delete ORF files who's filenames are not present in the set of found JPG/JPEG files

## How?

Run script with input directory as the first argument to have a dry run with a short report:
`python orffilter.py input_dir`

Run it with additional 'delete' argument to get a real run with the actual files deletion:
`python orffilter.py input_dir delete`
