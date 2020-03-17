import os

def removeFastaContaining(path, contains):
    """
    This function will take a path to a folder containg FASTA files and will remove all FASTA files from that 
    directory containg a given string i.e 'plasmid' in the description of the sequence (first line of FASTA)
    
    :param path: Path to folder of FASTA Files (str)
    :param contains: Word that identifies FASTA files you want to remove (str)
    """
    
    os.chdir(path)
    files = os.listdir()
    originalFileCount = len(files)
    countRemoved = 0
    for file in files:
        # read the first line
        firstLine = open(file, 'rb').readline()
    
        firstLine = str(firstLine)
        # if the first line contains 'plasmid' remove the file from the directory
        if 'plasmid' in firstLine:
            os.remove(file)
            countRemoved += 1
    newFileCount = len(os.listdir())
    
    print('OG Number of Files: %s' % originalFileCount)
    print('New Number of Files: %s' % newFileCount)
    print('Number of Files Removed: %s' % countRemoved)