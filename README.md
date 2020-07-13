
## The Redactor
  The sensetive information which is publicly disclosed should be redactioned before setting it out.The sensitive data such as names,places, phone numbers,etc must be hidden.Documents such as police reports, court transcripts, and hospital records all containing sensitive information. Redacting this information is often expensive and time consuming.
# Author
 Saisri M Potluru.You can contact me at saisri.m.potluru-1@ou.edu .
 
 The packages which has been used are nltk,re,etc
#  structure

~~~
.
├── COLLABORATORS
├── LICENSE
├── README.md
├── project1
│   ├── Pipfile
│   ├── Pipfile.lock
│   ├── main.py
│   ├── otherfiles
│   │   └── rfamily.md
│   ├── redactor.py
│   └── textfile.txt
├── setup.cfg
├── setup.py
└── tests
    └── test_names.py

~~~


# Setup Info :
~~~
 > pipenv run python redactor.py --input '*.txt' \
 >                   --input 'otherfiles/*.md' \
 >                   --names --dates \
 >                   --concept 'family' \
 >                   --output 'files/' \
 >                   --stats stderr    
~~~

By running the program with a command line argument (specified below) should read all files given by the glob — in this case all the files ending in .txt in in the folder and also all files ending in .md from the folder called otherfiles/. All these files will be redacted by the program. The program will look to redact all names, dates, and gender. Notice the flag --concept, this flag asks the system to redact all portions of text that have anything to do with a particular concept. In this case, all paragraphs or sentences that contain information about “family” should be redacted.  The final parameter, --stats, describes the file or location to write the statistics of the redacted files. 

# Description of the functions:
 ## input():
 This function will read the data of the file and append all the data in the files with extention .txt and .md. Then the data after reading is retrived.
 
 ## extractnames()
  This function is used to redacted all the names in the total data for each of the files.
 
 ## extractdates()
  This function is used to redacted all the dates in the total data for each of the files.Here the date formatin      the text files  should be only in mm/dd/yy format
  
 ## extractgender() 
  This function is used to redacted all the gender types in the total data for each of the files.
  
 ## concepts() 
  This function is used to redact all the concept types which means those who have all the same synonyms those stated sentences will be redacted.I have used "family" as my concept for the my data.
  
 ## stats()  
 This function takes either the name of a file, or special files (stderr, stdout), and writes a summary of the redaction process. Some statistics to include are the types and counts of redacted terms and the statistics of each redacted file. 
 
## outfile()
 This function will help to store all the extracted redacted content into an individual type with a .redacted
 
# Assumptions 
  - This comand line arguments should be given in a specified format
  - The date in the files should be in a form mm/dd/yy
 
# External Resources: 

https://stackoverflow.com/questions/31088509/identifying-dates-in-strings-using-nltk
https://medium.com/@rajat.jain1/natural-language-extraction-using-spacy-on-a-set-of-novels-88b159d68686
https://www.guru99.com/wordnet-nltk.html
https://www.geeksforgeeks.org/python-remove-duplicates-list/
 
  
 
 
