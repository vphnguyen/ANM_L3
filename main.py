import hashlib

# File to check
salt="salty_sonny"
file_name = 'noidung.txt'
# Correct original md5 goes here
original_md5 = '5d41402abc4b2a76b9719d911017c592'  
hashed_filename = hashlib.md5(file_name.encode()).hexdigest()
print("Hashed file name: "+hashed_filename)


# Open,close, read file and calculate MD5 on its contents 
with open(file_name , "rb") as file_to_check:
    # read contents of the file
    data = file_to_check.read()    
    # pipe contents of the file through
    md5_returned = hashlib.md5(data+(hashed_filename+salt).encode()).hexdigest()
    print(file_name +" MD5: "+ md5_returned)
# Finally compare original MD5 with freshly calculated
if original_md5 == md5_returned:
    print ("MD5 verified.")
else:
    print ("MD5 verification failed!.")