# Applied Data Science, Ian Langmore & Daniel Krasner
# Matius Celcius Sinaga
# Ubuntu 32 bit Python 2.7

import nltk
from os import listdir
from os.path import isfile, join
import sys

def main():
	basepath = '/home/stifen/Desktop/AppliedDataScience/'
	allfiles = [f for f in listdir(basepath) if isfile(join(basepath, f))]
	
	# bagian percakapan yang akan tetap disimpan
	pos_type = 'NN'
	for filename in allfiles:
		result = process_file(pos_type, basepath, filename)
		sys.stdout.write(result + '\n')
		
	def process_file(pos_type, basepath, filename):
		"""
		Baca satu file pada satu waktu, ekstrak kata tanpa berhenti pada bagian
		kata pos_type, ulangi perhitungan.
		
		Parameters
		----------
		pos_type : String
		Beberapa bagian nltk dari tipe ucapan, contohnya 'NN'
		
		basepath : String
		Bagian path dasar direktori menghandel file-file
		
		filename : String
		Nama dari file
		
		Ulangi
		------
		counts : String
		filename | word1:n1 word2:n2 word3:n3
		"""
		path = join(basepath, filename)
		
		with open(path, 'r') as f:
			text = f.read()
			tokens = nltk.tokenize.word_tokenize(text)
			good_words = [t for t in tokens if t.isalpha() and not is_stopword(t)]
			word_pos_tuples = nltk.pos_tag(good_words)
			typed= [wt[0] for wt in word_pos_tuples if wt[1] == pos_type]
			freq_dist = nltk.FreqDist(typed)
			
			# format hasil keluaran dari string
			outstr = filename+ '|'
			for word, count in freq_dist.iteritems():
				outstr +=word + ':' + str(count) + ''
				
			return outstr
			
	def is_stopword(string):
		return string.lower() in nltk.corpus.stopwords.words('indonesia')
			
	if __name__ == '__main__':
		main()	
