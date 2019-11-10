

def filenamemk(filepath):
    #GIVES FILE NAME OF FILEPATH
    import os
    a = os.path.abspath(filepath)
    #print(a)
    #filepathmk = os.path.dirname(os.path.abspath(filepath))
    #print(b)
    outputmk = (os.path.basename(filepath))
    #print(c)
    return outputmk

def filefoldermk(filepath):
    #GIVES PARENT FOLDER OF FILELOCATION
    import os
    a = os.path.abspath(filepath)
    #print(a)
    outputmk = os.path.dirname(os.path.abspath(filepath))
    #print(b)   
    #outputmk = (os.path.basename(filepath))
    #print(c)
    return outputmk


def hello(what):
    print("what")
    
    



def pdf_to_text(filepath):
# give pdf filepath as input
# output is text of pdf    
    import os
    import PyPDF2
    file_location = filefoldermk(filepath)
    file_name = filenamemk(filepath)

    os.chdir(file_location)
    
    pdfFileObj = open(file_name, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text_mk = pageObj.extractText()
    return text_mk

def regularexmk(text,word,option):
    #finds a word in text, and based on the option you choose will give the type of output
    #regex
    import re
    word_to_find__formated = re.compile(word)
    thesearch = word_to_find__formated.search(text)
    output = ""

    #things you can do:
    a = thesearch
    
    if a is not None:
        a = thesearch
        b = thesearch.group() # thing we were searching for (if found)
        c = thesearch.start() # starting position (if found)
        d = thesearch.end()   # ending position (if found)
        #give me:
        output = eval(option)

    if output is "":
        output = "Not Found"
    return output

def regularexmkfind(text,word):
    #finds a word in text, and based on the option you choose will give the type of output
    import re
    word_to_find__formated = re.compile(word)
    thesearch = word_to_find__formated.findall(text)
    output = ""

    #things you can do:
    a = thesearch
    
    if a is not None:
        a = thesearch
        #b = thesearch.group() # thing we were searching for (if found)
        #c = thesearch.start() # starting position (if found)
        #d = thesearch.end()   # ending position (if found)
        #give me:
        output = a

    if output is "":
        output = "Not Found"
    return output





def text_between(text, first_word,second_word):
    start = regularexmk(text,first_word,"d")
    end = regularexmk(text,second_word,"c")
    #print(start)
    #print(end)
    return text[start:end]
    
    


def listwords_intext(listmk,text):
    #looks through a list of words and find which ones appear in a text
    import re
    for eachthing in listmk:
        word_to_find_formated = re.compile(eachthing)
        thesearch = word_to_find_formated.search(text)
        if thesearch is not None:
            dog = eachthing
            return(dog)
            
        
def pull_fromtext(text,expression,length):
    #looks for expression in text then pulls out text after it
    import re
    word_to_find_formated = re.compile(expression)
    thesearch = word_to_find_formated.search(text)
    if thesearch is not None:
        output_startmk = text[thesearch.end():thesearch.end()+length]
        return(output_startmk)
    
def indexmatch(inputword,listone,listtwo):
    #looks for inputword in listone and outputs the matching word in listtwo
    indexofword = listone.index(inputword)
    outputword = listtwo[indexofword]
    #error handling:
    if outputword is not None:
            return(outputword)
    else:
        print("index match didn't work")



def readtextsupplier(text):
    #give text, i'll give you supplier
    #list of suppliers:
    import pandas as  pd
    import mkfunk as mk
    filepathname =  r"C:\Users\Second Login\Sync2\Sync\Finance\Accounts\supplier list for python .csv"
    supplierlist_text = pd.read_csv(filepathname)
    supplierlist = supplierlist_text['Supplier'].tolist()
    #look through list of suppliers, find my supplier and then note it.
    thistextsupplier = mk.listwords_intext(supplierlist,text)

    return thistextsupplier

def text_to_bill(text,thingiwant):
    #get supplier:
    output = readtextsupplier(text)
    return output


def dataf_to_csv(dataframemk,filepath):
    #give me a dataframe, a filepath and i'll save it for you
    export_csv = dataframemk.to_csv ((filepath), index = None, header=True)


def listadder(listmk,text):
    #give me some text and i'll add it to your list
    listmk.append(text)
    return listmk


def twowaymatch(listmk,indexmk,array):
    #give me those and i'll give you what's in the cell
    print("nothing")


def text_to_invoice_ref(text,invoiceref):
    readtextsupplier(cleantext(text))
    text = cleantext(text)
    expression = "Invoice Ref:"
    length = 8
    output = pull_fromtext(text,expression,length)
    return output


def cleantext(text):
    #give me text and i'll remove \n
    text = text.replace("\n","")    
    return text

def listtolists(listmk):
    #i'll create a list for each list:
    for eachcell in listmk:
        eachcell



def windowupright():
    #not working, need a way of sticking variable in
    import os
    import time
    from pynput.keyboard import Key, Controller
    keyboard = Controller()
    #hold window key
    keyboard.press(Key.cmd)
    
    for each in (1,2):
        #up
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    #right  
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(0.5)
    #up
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    #release window key
    keyboard.release(Key.cmd)

def windowdownright():
    #not working, need a way of sticking variable in
    import os
    import time
    from pynput.keyboard import Key, Controller
    keyboard = Controller()
    #hold window key
    keyboard.press(Key.cmd)
    
    for each in (1,2):
        #up
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    #right  
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(0.5)
    #up
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    #release window key
    keyboard.release(Key.cmd)


def windowdownleft():
    #not working, need a way of sticking variable in
    import os
    import time
    from pynput.keyboard import Key, Controller
    keyboard = Controller()
    #hold window key
    keyboard.press(Key.cmd)
    
    for each in (1,2):
        #up
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    #right  
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    time.sleep(0.5)
    #up
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    #release window key
    keyboard.release(Key.cmd)

def windowupleft():
    #not working, need a way of sticking variable in
    import os
    import time
    from pynput.keyboard import Key, Controller
    keyboard = Controller()
    #hold window key
    keyboard.press(Key.cmd)
    
    for each in (1,2):
        #up
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    #right  
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    time.sleep(0.5)
    #up
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    #release window key
    keyboard.release(Key.cmd)

def windowleft():
    #not working, need a way of sticking variable in
    import os
    import time
    from pynput.keyboard import Key, Controller
    keyboard = Controller()
    #hold window key
    keyboard.press(Key.cmd)
    
    for each in (1,2):
        #up
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    #right  
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    time.sleep(0.5)
    #release window key
    keyboard.release(Key.cmd)

def windowright():
    #not working, need a way of sticking variable in
    import os
    import time
    from pynput.keyboard import Key, Controller
    keyboard = Controller()
    #hold window key
    keyboard.press(Key.cmd)
    
    for each in (1,2):
        #up
        keyboard.press(Key.up)
        keyboard.release(Key.up)
    #right  
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(0.5)
    #release window key
    keyboard.release(Key.cmd)
    

def bdwdotstring1(inputsomething):
    '''
    This Function dates a name with two parts, and where the second part is a date and creates a new name where the second part is a week later. 
    '''
    from datetime import datetime
    from datetime import timedelta
    old_string = inputsomething
    print("old_string = "+old_string)
    #splits the string into two after the space
    datepart_string = old_string.split(" ")
    #picks the second part of split
    datepart_string[1]
    str1 = ''.join(datepart_string[1])
    
    #converts date part of string into date format
    a = datetime.strptime(str1, '%Y.%m.%d')
    
    #add seven days to date
    a = a + timedelta(days=7)
    #convert to date (from datetime)
    a = a.date()
    
    a = str(a)
    #replace - with dots
    a = a.replace("-",".")
    a = ''.join(["WE ",a])

    print("new_string = "+a)
    return a
    


def opposite_of_split(original,split):
    #where the orignal was split due to regex, it returns all the things that were removed
    import re
    for each in split:
        each = re.compile(str(each))
        #print(str(type(each))+str(type(original)))
        original = each.sub('',original,1)
        print(original)
    print("final "+str(original))
          

def csv_load(csv_filepath):
    #make sure csv_path has got an "r" before the path. 
    #give me a filepath (assuming csv) and i'll load it into pandas
    # Load the Pandas libraries with alias 'pd' 
    import pandas as pd
    import os
    import mkfunk as mk
    # Read data from file 'filename.csv' 
    # (in the same directory that your python process is based)
    # Control delimiters, rows, column names with read_csv (see later)

    filepath = csv_filepath
    namemk = mk.filenamemk(filepath)
    pathmk = mk.filefoldermk(filepath)

    os.chdir(pathmk) # go to where excel is
    data = pd.read_csv(namemk) 
    # Preview the first 5 lines of the loaded data 
    data.head()
    return data


def files_in_folder(folderpath):
    #make sure there is an "r" a the front of the filepath and no "\" at the end
    #give me a folder path and i'll give you the full filepath of all filesinside
    import os
    #list directories in filepath:
    alist = os.listdir(folderpath)
    alist2 = []
    for each in alist:
            print (each)
            each2 = os.path.join(folderpath,"\\",each)
            print(each2)
            alist2.append(each2)
            print(alist2)
    return alist2


def files_in_folder(folderpath):
    #make sure there is an "r" a the front of the filepath and no "\" at the end
    #give me a folder path and i'll give you the names of the files inside
    import os
    alist = os.listdir(folderpath)
    return alist
    
   


def runmacrofrom_tofile_overwrite(macroname,fromexcel,toexcel):
    #macro name in format "!Macro1"
    #excel's both in absolute path fromat with an "r" at the front
    import os, os.path
    import win32com.client
    import mkfunk as mk
    #file1 one with Macro
    filemk = fromexcel
    filemk2= mk.filenamemk(filemk)
    workingdirectory = mk.filefoldermk(filemk)
    os.chdir(workingdirectory)
    macro_name = macroname
    #start of file
    xlapp=win32com.client.Dispatch("Excel.Application")
    xlapp.Visible = 1
    xlwb = xlapp.Workbooks.Open(filemk)

    #file2 do something to me. 
    filemk = toexcel
    workingdirectory = mk.filefoldermk(filemk)
    os.chdir(workingdirectory)
    #start of file
    #xlapp.Visible = 1
    xlwb2 = xlapp2.Workbooks.Open(filemk)

    print(os.getcwd())
    xlapp2.Application.Run(filemk2+macro_name)
    xlwb.Close(True)
    xlwb2.Close(True)
    xlapp.Application.Quit() # Comment this out if your excel script closes

def runmacrofrom_tofile(macroname,fromexcel,toexcel):
    #macro name in format "!Macro1"
    #excel's both in absolute path fromat with an "r" at the front
    import os, os.path
    import win32com.client
    import mkfunk as mk
    #file1 one with Macro
    filemk = fromexcel
    filemk2= mk.filenamemk(filemk)
    workingdirectory = mk.filefoldermk(filemk)
    os.chdir(workingdirectory)
    macro_name = macroname
    #start of file
    xlapp=win32com.client.Dispatch("Excel.Application")
    xlapp.Visible = 1
    xlapp.DisplayAlerts = False
    xlwb = xlapp.Workbooks.Open(filemk)

    #file2 do something to me. 
    filemk = toexcel
    workingdirectory = mk.filefoldermk(filemk)
    os.chdir(workingdirectory)
    #start of file
    xlapp2=win32com.client.Dispatch("Excel.Application")
    xlapp.Visible = 1
    xlapp.DisplayAlerts = False
    xlwb2 = xlapp2.Workbooks.Open(filemk)

    print(os.getcwd())
    xlapp2.Application.Run(filemk2+macro_name)
    xlwb.Close(False)
    toexcel_len = len(toexcel) 
    xlwb2.SaveAs(mk.add_version(toexcel))
    xlwb2.Close(False)
    xlapp.Application.Quit() # Comment this out if your excel script closes

def runmacro_samefile_addversion(macroname,fromexcel,toexcel):
    #macro name in format "!Macro1"
    #excel's both in absolute path fromat with an "r" at the front
    import os, os.path
    import win32com.client
    import mkfunk as mk
    #file1 one with Macro
    filemk = fromexcel
    filemk2= mk.filenamemk(filemk)
    workingdirectory = mk.filefoldermk(filemk)
    os.chdir(workingdirectory)
    macro_name = macroname
    #start of file
    xlapp=win32com.client.Dispatch("Excel.Application")
    xlapp.Visible = 1
    xlapp.DisplayAlerts = False
    xlwb = xlapp.Workbooks.Open(filemk)

    print(os.getcwd())
    xlapp.Application.Run(filemk2+macro_name)
    toexcel_len = len(toexcel) 
    xlwb.SaveAs(mk.add_version(toexcel))
    xlwb.Close(False)
    xlapp.Application.Quit() # Comment this out if your excel script closes
    

def filterlist(searchword,alist):
    #this is like filtering a list on stuff that matches the search term)
    #give me a word and a list and return a list with items that match the search
    alist2 = []
    for each in alist:
        findme = searchword
        result = regularexmk(each,findme,"a")
        if result != "Not Found":
            alist2.append(each)
    return alist2


def add_version(filepath):
    c_filename = filenamemk(filepath)
    parentdirectory = filefoldermk(filepath)
    #regex:
    expression = "\sv\d+"
    #location of regex:
    b = regularexmk(c_filename,expression,"c")
    c = regularexmk(c_filename,expression,"d")
    #snippet of version:
    version = int(c_filename[b+2:c])
    #add 1 to file name:
    version +=1
    #reconstruct name:
    newfilenamepath = parentdirectory+"\\"+c_filename[:b+2]+str(version)+get_filetype(c_filename.replace(".", "",c_filename.count(".")-1))
    return newfilenamepath

def get_filetype(filepath):
    #give filepath and i'll give you the format of the file + the dot infront
    c_filename = filenamemk(filepath)
    #regex:
    expression = "\."
    #location of regex:
    b = regularexmk(c_filename,expression,"c")
    print(b)
    #snippet of filetype:
    filetype = c_filename[b:]
    ##reconstruct name:
    #newfilename = c_filename[:b+2]+str(version)
    return filetype


def findlatestversion(folderpath,basename):
    #Give me a folder and the basename of a file, i'll give you the latest version's filepath
    #filename hsa to be in  format " v12." (space before v and dot after last number)
    #Input1. choose folder path "folderpath"
    #Input2. choose folder path "searchword"                      
    #list all directories
    alist = files_in_folder(folderpath)

    #get list of this base
    newlist = filterlist(basename, alist)

    ###test next two lines:
    #get list of this base
    word = "\sv\d+"
    newlist = filterlist(word, alist)

    #create list of versions
    list3 =[]
    #word = "\sv\d+"
    word = "\sv\d+"
    for each in newlist:
        b = regularexmk(each,word,"c")
        c = regularexmk(each,word,"d")
        newtext = each[b+2:c]
        list3.append(newtext)
    #Get the lastest version by sorting and picking top one

    sortedlist = sorted(list3, reverse=True)
    #look for this version number in original list of version, and choose the same number down on the original list. 
    filename = indexmatch(sortedlist[0],list3,newlist)

    filepathname = filefoldermk(folderpath)
    newfilepath = filepathname+"\\"+filename
    return(newfilepath)
        
    
def merge_csvs_in_folder(foldermk):
    #give me a folder and i'll merge all csv's in it (as long as they've got same heading length)
    #i'll save merged file in same folder.
    import os
    import pandas as pd
    #Get size of headings:
    mkdirectory = os.listdir(foldermk)
    firstdmk = csv_load(os.path.join(foldermk,mkdirectory[0]))
    headingsmk = list(firstdmk.columns)
    #create blank dataframe with these headings:
    dataframemk = pd.DataFrame(columns=headingsmk)
    #for each in folder open in dataframe, append to master dataframe
    for each in mkdirectory:
        thing = csv_load(os.path.join(foldermk,each))
        dataframemk = dataframemk.append(thing)
    #save new dataframe in folder as merged
    export_csv = dataframemk.to_csv (os.path.join(foldermk,"MERGED_CSVs.csv"), index = None, header=True)












