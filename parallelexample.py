# Applied Data Science, Ian Langmore & Daniel Krasner
# Matius Celcius Sinaga
# Ubuntu 32 bit Python 2.7

import nltk
from os import listdir
from os.path import isfile, join
import sys

import itertools
from functools import partial
from multiprocessing import Pool
from multiprocessing.pool import IMapUnorderedIterator, IMapIterator

def main():
	basepath = '/home/stifen/Desktop/AppliedDataScience/'
	allfiles = [f for f in listdir(basepath) if isfile(join(basepath, f))]
	
	# jumlah dari proses slave untuk memulai
	n_procs = 2
	
	# ukuran potongan untuk dikirim diantar slave dan master
	chunksize = 10
	
	# bagian dari type speech yang akan disimpan
	pos_type = 'NN'
	
	# membentuk sebuah fungsi dari satu variable dengan memperbaiki 
	# seluruhnya namun pada argumen berikutnya
	# f(filename) = process_file(..., filename)
	f = partial(process_file, post_type, basepath)
	
	# membentuk iterator yang sama
	# (f(filename) = process_file(..., filename)
	
	# jika kita menggunakan 1 prosessor, gunakan saja fungsi normal itertools.imap
	# kalau tidak gunakan worker_pool
	if n_procs == 1:
		results_iter = itertools.imap(f, allfiles)
	else:
		worker_pool = Pool(n_procs)
		results_iter = worker_pool.imap_unordered(f, allfiles, chunksize=chunksize

	for result in results_iter:
		sys.stdout.writer(result + '\n')
		
	def imap_wrap(func):
		def wrap(self, timeout=None):
			return func(self, timeout=timeout if timeout is not None else 1e100)
		return wrap
		
# Redefine IMapUnorderedIterator so we can exit with Ctrl-C
IMapUnorderedIterator.next = imap_wrap(IMapUnorderedIterator.next)
IMapIterator.next = imap_wrap(IMapIterator.next)
	
