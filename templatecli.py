from optparse import OptionParser
import sys

def main():
	"""
	DESKRIPSI
	---------
	Menghapus setiap baris nth pada file atau stdin, 
	dimulai pada baris pertama, ditampilkan pada stdout
	
	CONTOH
	------
	Menghapus setiap baris kedua dari sebuah file dengan perintah
	python templatecli.py -n 2 data.csv
	
	"""
	usage = "penggunaan : %prog [options] dataset"
	usage += '\n'+main.__doc__
	parser = OptionParser(usage=usage)
	parser.add_option(
		"-n", "--deletion_rate",
		help="Menghapus setiap baris nth [default: %default] ",
		action="store", dest='deletion_rate', type=float, default=2)
		
	(option, args) = parser.parse_args()
	
	### Parse args
	# Raise an exception if the length of args is greater than 1
	assert len(args) <= 1
	infilename = args[0] if args else None
	
	## Get the infile
	if infilename:
		infile = open(infilename, 'r')
	else:
		infile = sys.stdin
		
	## Call the function that does the real work
	delete(infile, sys.stdout, option.deletion_rate)
	
	##Close the infile iff not stdin
	if infilename:
		infile.close()
		
def delete(infile, outfile, deletion_rate):
	"""
	Write later, if module interface is needed
	"""
	for linenumber, line in enumerate(infile):
		if linenumber % deletion_rate != 0:
			outfile.write(line)
			
if __name__=='__main__':
	main()
