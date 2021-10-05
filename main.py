import hashlib
import glob, os
import fileinput
#==============================================================================    FUNC
def hash_file(path,salt):
    #==========================    MD5 Filename 
    hashed_filename = hashlib.md5(file_name.encode()).hexdigest()
    print(" File name: "+hashed_filename)
    #==========================    MD5 File content
    with open(path , "rb") as file_to_check:
        #==========================    get byte
        data = file_to_check.read()    
        #==========================    MD5 with salt and md5 file name
        md5_overall = hashlib.md5(data+(hashed_filename+salt).encode()).hexdigest()
        print(" Path: "+file_name +"\n MD5: "+ md5_overall)
    return md5_overall

def hash_dir():
    print("Hello from a function")
def check_hash(hash,path,file,type):
    infile =open (file,'r')
    found=False
    for line in infile:
        print("-"*30)
        print ("Scanning: ",line.strip())
        #if: DIRRRRRRRRR
        if type=="file":
            if line.strip().find(type) == 0:
                # Diff Path
                if path not in line:
                    continue
                # Same Path
                else:
                    array_in= line.rstrip().split("|")
                    print ("With:\n\tType: "+array_in[0]+"\n\tPath: "+array_in[1]+"\n\tMD5: "+array_in[2])
                    # Correct hash code
                    if array_in[2] == hash:
                        print("-"*50)
                        print (" MD5 CHECK OKE.")
                        return
                    # Different hash code (Ask for update)
                    else:
                        print("-"*50)
                        found=True
                        print (" Found file but MD5 verification failed!.")
                        if input("Update with new hash code (yes) ? ").strip()=="yes":
                            #replace
                            infile.close()
                            with fileinput.FileInput(file, inplace=True, backup='.bak') as file_replace:
                                for line_r in file_replace:
                                    print(line_r.replace(str(array_in[2]), hash), end='')
                            print("-"*50)
                            print ("-- UPDATE DONE (Created .bak)--")
                            return
                        return
        #if: DIRRRRRRRRR   
    print("-"*50)
    infile.close()   
    # Scanned all content (Could not found)
    if not found:
        if input("Not EXIST. Add this file to DB (yes) ? ").strip()=="yes":
            outfile =open (file,'a')
            print(type+"|"+file_name+"|"+hash,file=outfile)
            outfile.close()
            return
    
#==============================================================================    MAINNNNNNNNNNNNNNNNNNNNNNNNN
salt="password"
print("C:\\Users\\nguye\\Source\\Repos\\ANM_L3\\noidung.txt")
file_name = input("File at: ").strip()
#==========================    CHECK FILE EXIST
if not os.path.exists(file_name):
    print("Path not exist")
    os._exit(0)
#==========================    DIR OR FILE
if os.path.isdir(file_name):  
    print("It is a directory")  
elif os.path.isfile(file_name):  
    print("It is a normal file")
    print("-"*50)
    hashed = hash_file(file_name,salt)
    result = "file|"+file_name+"|"+ hashed 
    check_hash(hashed,file_name,"md5_db.txt","file")







#==== FOLDER control
print(os.getcwd())
print(glob.glob(os.getcwd()+"\\biggest_folder\\"))
for root, dirs, files in os.walk(os.getcwd()+"\\biggest_folder\\"):
    for file in files:
        print(file)