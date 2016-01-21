'''Author: Victoria Nikolich'''
'''File: find.py '''
'''find.py looks for filenames contianing a specified pattern'''

import sys, glob

'''the following segment reads the command line'''
if(len(sys.argv)!=2):
    ''' exits if  incorrect number of arguments'''
    print "error - usage: find.py name\\*ext"
    sys.exit(2)

def recursiveSearch(folderpath, foundlist, pattern):
    '''recursively searches through folders to find files matching the pattern'''
    foundlist.extend(glob.glob(folderpath+"/"+pattern))
    '''remove the following from this method - they are placeholders'''
    foundlist.append('fillerA')
    foundlist.append('fillerB')
    foundlist.append('filllerC')

''' sys.argv[1] contains the pattern from the command line'''
foundlist = []
recursiveSearch("",foundlist, sys.argv[1])

''' the following prints each item of the result list on a new line'''
for f in foundlist:
    '''print an element in foundlist'''
    print f+"\n"

