import cryptography
from cryptography.fernet import Fernet # for encryption and decryption
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
import base64
import sys
# if you get an error on the above line, you might need to run 
# pip install INSERT_LIBRARY_NAME or install the library another way.

#Below are some TODO comments.


def generate_mq_key(key_string="please don't use the default"):
    if(len(key_string)<32):
       key_string = str(key_string + "abcdefghijklmnopqrstuvwxyz012345")
    key_string = key_string[0:32]
    key_string_bytes = str(key_string).encode("ascii")
    key = base64.urlsafe_b64encode(key_string_bytes)
    return key

def encrypt_file(input_filename, output_filename, key = ""):
    #TODO: use fernet, open the file input_filename
    #read and encrypt the contents of the file
    #store the encrypted contents in another file who's name
    #is stored in output_filename
    #https://cryptography.io/en/latest/fernet
    f = Fernet(key)
    with open(input_filename, 'rb') as input_file, \
         open(output_filename, 'wb') as output_file:
        plain = f.encrypt(input_file.read())
        output_file.write(plain)

    return None


def decrypt_file(input_filename, output_filename, key = ""):
    #TODO: use fernet, open the file input_filename
    #read and decrypt the contents of the file
    #store the decrypted contents in another file who's name
    #is stored in output_filename
    #https://cryptography.io/en/latest/fernet/
    f = Fernet(key)
    with open(input_filename, 'rb') as input_file, \
         open(output_filename, 'wb') as output_file:
        plain = f.decrypt(input_file.read())
        output_file.write(plain)

    return None


def generate_hash(input_filename, output_filename, key = ""):
    #TODO: use the hazmat section of cryptography to generate a hash.
    #take the contents from the file named input_filename
    #hash the contents, 
    #store the decrypted contents in another file who's name
    #is stored in output_filename
    #https://cryptography.io/en/latest/hazmat/primitives/cryptographic-hashes/
    hasher = hashes.Hash(hashes.SHA256())
    with open(input_filename, "rb") as input_file, \
         open(output_filename, "wb") as output_file:
        hasher.update(input_file.read())
        output_file.write(hasher.finalize())
    return None 


###############################################################################

def task_1(student_id,input_file_name , output_file_name):
    # remember, use the command console to run the argument
    # python   crypto_a1_activity.py   40000000  task1   encrypteddata.txt   decrypteddata.txt
    key = generate_mq_key(str(student_id))
    #decrypt_file(input_file_name, output_file_name, key)
    #TODO: call the functions needed for task 1 and pass the parameters as needed
    #TODO: update the line below to say "Completed Task 1"
    print("Completed Task 1")
    decrypt_file(input_file_name, output_file_name, key)

def task_2(student_id, input_file_name , output_file_name):
    # remember, use the command console to run the argument
    # python   crypto_a1_activity.py   YOUR_STUDENT_NUMBER  task2   datafile.encrypted   datafile_enc_decr
    key = generate_mq_key(str(student_id))
    #TODO: call the functions needed for task 2 and pass the parameters as needed
    #TODO: update the line below to say "Completed Task 2"
    print("Completed Task 2")
    encrypt_file(input_file_name, output_file_name, key)

def task_3(student_id, input_file_name , output_file_name):
    #TODO: call the functions needed for task 3 and pass the parameters as needed
    #TODO: update the line below to say "Completed Task 3"
    print("Completed Task 3")
    cipher_file = f'{output_file_name.replace(".txt", "")}_encrypted.txt' # the file that will store the encrypted file to be re-decrypted
    task_2(student_id, input_file_name, cipher_file)
    task_1(student_id, cipher_file, output_file_name)



def task_4(student_id, input_file_name , output_file_name):
    #TODO: call the functions needed for task 4 and pass the parameters as needed
    #TODO: update the line below to say "Completed Task 4"
    print("Completed Task 4")
    generate_hash(input_file_name, output_file_name)

def task_5(student_id, input_file_name , output_file_name):
    #TODO: call the functions needed for task 5 and pass the parameters as needed
    #TODO: update the line below to say "Completed Task 5"
    print("Completed Task 5")
    generate_hash(input_file_name,output_file_name)


###############################################################################
#You don't need to edit anything below here.
def main():
    if len(sys.argv) < 5:
        print("not enough arguments have been entered. Use the following format from the IDE console:")
        print("\npython crypto_a1_activity.py 41234567 task1 inputFileName outputFileName\n\nor")
        print("\npython3 crypto_a1_activity.py 41234567 task1 inputFileName outputFileName\n\n")
    else:
        student_id = sys.argv[1] # student ID
        encryption_actitiy = sys.argv[2] # encrypt, decrypt, or hash
        input_file_name = sys.argv[3]
        output_file_name = sys.argv[4]
        if(encryption_actitiy == "task1"):
            task_1(student_id,input_file_name , output_file_name)

        elif(encryption_actitiy == "task2"):
            task_2(student_id,input_file_name , output_file_name)

        elif(encryption_actitiy == "task3"):
            task_3(student_id,input_file_name , output_file_name)

        elif(encryption_actitiy == "task4"):
            task_4(student_id,input_file_name , output_file_name)

        elif(encryption_actitiy == "task5"):
            task_5(student_id,input_file_name , output_file_name)
        else:
            print("couldn't work out what to do.")
            print("Please use the following format when running the file:\n")
            print("python   crypto_a1_activity.py   STUDENT_NUMBER  ACTIVITY   INPUT_FILENAME   OUTPUT_FILENAME")
            print("\nACTIVITY can be any of the following words:")
            print("task1")
            print("task2")
            print("task3")
            print("task4")
            print("task5")



if __name__ == "__main__":
    main()