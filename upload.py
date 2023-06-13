import os, shutil

rootPath = 'C:\\CLD\\'

pdf = 'C:\\Users\\workadmin\\Desktop\\Samples\\sample.pdf'
doc = 'C:\\Users\\workadmin\\Desktop\\Samples\\Testing.docx'
pdfName = 'sample.pdf'
docName = 'Testing.docx'

file = open('docx.csv', 'r')

for line in file:
        #tempPath = rootPath
        path = line.strip().split('\\')
        tempPath = os.path.join(rootPath,path[0])
        if os.path.exists(tempPath) == False:
            print('making path')
            os.mkdir(tempPath)
        else:
            print(tempPath)
        
        tempPath = os.path.join(tempPath,path[1])
        if os.path.exists(tempPath) == False:
            print('making path')
            os.mkdir(tempPath)
        else:
            print(tempPath)
        
        tempPath = os.path.join(tempPath,path[2])
        if os.path.exists(tempPath) == False:
            print('making path')
            os.mkdir(tempPath)
        else:
            print(tempPath)
        
        tempPath = os.path.join(tempPath,path[3])
        if os.path.exists(tempPath) == False:
            print('making path')
            os.mkdir(tempPath)
        else:
            print(tempPath)
            
        tempPath = os.path.join(tempPath,path[4])
        if os.path.exists(tempPath) == False:
            print('making path')
            os.mkdir(tempPath)
        else:
            print(tempPath)
            
        tempPath = os.path.join(tempPath,path[5])
        if os.path.exists(tempPath) == False:
            print('making path')
            os.mkdir(tempPath)
        else:
            print(tempPath)
            
        path2 = path[6].strip().split('_')    
        tempPath = os.path.join(tempPath,path2[0])
        print(tempPath)
        if os.path.exists(tempPath) == False:
            print('making path')
            os.mkdir(tempPath) 
            #need a way to check if the directory has additonal text after path[6]
            nameOfFile = path2[1]
            print(nameOfFile)
            if 'ACROBAT' in path2[2]:
                shutil.copy(pdf, tempPath)
                print('added PDF to directory')
                os.rename(tempPath + '\\' + pdfName,tempPath + '\\' + nameOfFile + '.pdf')
                print('renamed file')
            elif 'WORD' in path2[2]:
                shutil.copy(doc, tempPath)
                print('added DOC to directory')
                os.rename(tempPath + '\\' + docName,tempPath + '\\' + nameOfFile + '.docx')
                print('renamed file')
                    
            #for file_name in files:
            #    shutil.copy(origin+file_name, tempPath)
            #    print('copying files')
            
        else:
            print(tempPath)
