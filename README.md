Substitution Cipher Hacker

Usage:
	python main.py [options] [--in input-file] [--out output-file]


If there are no options, --in or --out, program will work with standard stream

For more help use command:
	python main.py -h
	

Structure of project:
	- cipher - folder contains main algo to decrypt or encrypt message
		- decrypt.py - hack the cipher
		- encrypt.py - encrypt the message
		- cracker - folder contains class of substitution cipher's hacker
			- cracker.py - crack the text
			- scoring.py - score of quadrograms
		- tests.py - tests for all project
	- dictionaries - folder contains settings, ABC and dictionaries for other languages
		- settings.py - settings for other languages. For example, pattern of word in text.
		- prepare_dict.py - procedure for preparing dictionaries and downloading its to memory
		- lang - folder with languages
			- en - English dictionaries
				- ...
			- ru - Russian dictionaries
				- ...
	- examples - folder contains tests
	- main.py - entry poing for program
	- options.py - parses options from command line
	
	
