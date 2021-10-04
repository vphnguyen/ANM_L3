import hashlib

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


infile =open ('md5_db.txt','r')
for line in infile:
    print("Checking with: "+ line)
    if md5_overall == line.strip() :
        print ("MD5 ton tai trong DB.")
    else:
        print ("Khong tim thay MD5 nao.")
infile.close()

if input("Wanna write to db ? ")=="yes":
    outfile =open ('md5_db.txt','w')
    print(md5_overall,file=outfile)
    outfile.close()
