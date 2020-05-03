import sys, getopt, os, shutil
from datetime import datetime
from os import listdir
from os.path import isfile, join

def formatedMonth(month): 
  formated = ["1 - January", "2 - February", "3 - March", "4 - April", "5 - May", "6 - June", "7 - July", "8 - August", "9 - September", "10 - October", "11 - November", "12 - December"]
  return formated[month - 1]

def main(argv):
  inputfile = ''
  outputfile = ''
  try:
    opts, args = getopt.getopt(argv,"hi:o:")
  except getopt.GetoptError:
    print 'sort.py -i <inputfile> -o <outputfile>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'sort.py -i <inputfile> -o <outputfile>'
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputfile = arg
    elif opt in ("-o", "--ofile"):
      outputfile = arg
  if inputfile == '' or outputfile == '':
    print 'sort.py -i <inputfile> -o <outputfile>'
    sys.exit()

  allFiles = [f for f in listdir(inputfile) if isfile(join(inputfile, f)) and not f.startswith(".")]
  
  for file in allFiles: 
    oldFileLocation = inputfile + "/" + file
    # get file creation timestamp
    birthTime = os.stat(oldFileLocation).st_birthtime
    dt_object = datetime.fromtimestamp(birthTime)
    # get year of creation
    year = dt_object.year
    # get month of creation
    month = dt_object.month
    # move to new location 
    newFileLocation = outputfile + "/" + str(year) + "/" + formatedMonth(month) + "/" + file
    directory = os.path.dirname(newFileLocation)
    # create newLocation if it doesn't exist
    if not os.path.exists(directory):
      os.makedirs(directory)
    # move file
    shutil.move(oldFileLocation, newFileLocation)

if __name__ == "__main__":
  main(sys.argv[1:])