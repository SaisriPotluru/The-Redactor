import nltk
import glob
import re
 
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet
nltk.download('wordnet')
from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.tokenize import word_tokenize

tdata=[]

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


def input(text):
   # print(text)

    textf=glob.glob(text)

    for i in range(len(textf)):
        data=open(textf[i]).read()
        tdata.append(data)

    return tdata

def Convert(string):
    li = list(string.split(" "))
    return li


def listToString(s):

    str1 = " "

    return (str1.join(s))

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


def extractnames(files_read):
    readacted_name_files = []
    for i in range(len(files_read)):
        lnames=[]
        stop = stopwords.words('english')
        Sentences = nltk.sent_tokenize(files_read[i])
        Tokens = []
        for Sent in Sentences:
            Tokens.append(nltk.word_tokenize(Sent)) 
            Words_List = [nltk.pos_tag(Token) for Token in Tokens]
     
        Nouns_List = []
        for List in Words_List:
            for Word in List:
                if re.match('[NN*]', Word[1]):
                    Nouns_List.append(Word[0])
        Names = []
        for Nouns in Nouns_List:
            if not wordnet.synsets(Nouns):
                Names.append(Nouns)
                
        for name in Names:
            files_read[i] = files_read[i].replace(name,'██')
        
        
        readacted_name_files.append(files_read[i])   
               
        countnames=[]
        
        countnames.append(len(re.findall('██',files_read[i])) + 1)     
             
    return readacted_name_files,countnames
           

        
def extractdates(files_read):
        redacted_date_files=[]
        countdate=[]
        countdate=0
        for i in range(len(files_read)):
            d = re.findall(r'\d+\S\d+\S\d+', files_read[i])
            for date in d:
                files_read[i] = files_read[i].replace(date,'██')
                countdate+=1
                
            redacted_date_files.append(files_read[i]) 
            
      
        return redacted_date_files,countdate; 
           

def extractgender(readacted_date):
    redacted_gender_files=[]
    countgender =0
    newls=[]
    gender=['mr.','sir','his','mister','mr','prince','king','mrs.','ms.','miss','her','lady','madameoiselle','baroness','mistress','mrs','ms','queen','princess','madam','madame']
    for i in range(len(readacted_date)):
        tokenize=word_tokenize(readacted_date[i])
        for n,i in enumerate(tokenize):
            for j in range(len(gender)):
                if i.lower() == gender[j]:
                    tokenize[n] = '██'
                    countgender+=1
        file = TreebankWordDetokenizer().detokenize(tokenize)
        

        redacted_gender_files.append(file)  

    return redacted_gender_files,countgender
    
            
def concept(w, redacted_gender):
    concept_files=[]
    countconcept=0
    sys = wordnet.synsets(w)
    fs=[]
    synonyms=[]
    for sys in wordnet.synsets(w):
        for l in sys.lemmas():
            synonyms.append(l.name())
    synonyms=Remove(synonyms)
   
    for i in range(len( redacted_gender)):
        stoken= sent_tokenize( redacted_gender[i])
        for k in range(len(stoken)):
            for j in range(len(synonyms)):
                if synonyms[j] in stoken[k].lower():
                    fs.append(stoken[k])
                      
    for i in range(len( redacted_gender)):
        h= redacted_gender[i]
        for g in range(len(fs)):
            if fs[g] in h:
                h=h.replace(fs[g],'██')
                countconcept+=1
        concept_files.append(h)
    return concept_files, countconcept        
    





