import hashlib
import glob, os
#==========================    INIT
salt="salty_sonny"
file_name = 'noidung.txt'
#==========================    MD5 Filename
original_md5 = '5d41402abc4b2a76b9719d911017c592'  
hashed_filename = hashlib.md5(file_name.encode()).hexdigest()
print("Hashed file name: "+hashed_filename)

#==========================    MD5 File content
with open(file_name , "rb") as file_to_check:
    #==========================    get byte
    data = file_to_check.read()    
    #==========================    MD5 with salt and md5 file name
    md5_overall = hashlib.md5(data+(hashed_filename+salt).encode()).hexdigest()
    print(file_name +" MD5: "+ md5_overall)

print("-"*50)
infile =open ('md5_db.txt','r')
found=False
for line in infile:
    line=line.strip()
    print(" -Checking with: "+ line)
    if md5_overall == line :
        print (" MD5 CHECK OKE.")
        found=True
        break
    else:
        print (" MD5 verification failed!.")
    print("-"*30)
infile.close()
if not found :
    if input("Wanna write to db ? ")=="yes":
        outfile =open ('md5_db.txt','a')
        print(md5_overall,file=outfile)
        outfile.close()
#==== FOLDER control
print(os.getcwd())
print(glob.glob(os.getcwd()+"\\*"))
slice = glob.glob(os.getcwd()+"\\*"
