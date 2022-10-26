'''
A simple tkinter widget for hashing
Get sha256 hash of any input
Get sha256 hash by adding a salt(any text which acts as a pass phrase or your secret code )which further generates a hash of input string joined with secret passphrase or pin 
You can store first four to five digits of the generated hash for any password or input and later use this code to test if you are using the correct password for something.
Caution: If you forget the passphrase then there is no way to get the same digits.
Storing obly first four to five digits ensures that no one can guess both either the input or the pass phrase as there will be almost unlimited possibilities for getting the same digits which you have stored.
You can even modify the code to get so many variations for hashing to have even more complexity but this code is for demonstarting the concept
get_smallest_hash function used to store the characters of your password using the same basic concept and you can get back the password or input uaing the same passphrase you used to store them.

'''
import tkinter as tk
import hashlib as hs
root = tk.Tk()
root.title("Hash Generator")
root.geometry('1000x1000')

# reusable hash function
def get_sha256(input_str= None):
	if input_str is None:
		input_str= input("Enter any text or passphrase to get sha256 hash: ")
	hash_op = hs.sha256(input_str.encode('utf-8')).hexdigest()
	return(hash_op)

def get_hash():
	hsh_input = e1.get()
	hsh_confirm = e2.get()
	if hsh_input == hsh_confirm:
		hsh_output = get_sha256(hsh_input)
		lbl2 = tk.Label(root, text= hsh_output)
		lbl2.pack()
	else:
		lbl3= tk.Label(root, text= "The inputs don't match")
		lbl3.pack()
		
def get_salted_hash():
	ip_text_hsh = get_sha256(e1.get())
	salt_hsh=   get_sha256(e_salt.get())
	salted_ip = ip_text_hsh + salt_hsh
	hsh_salted_ip = get_sha256(salted_ip)
	lbl4= tk.Label(root, text= hsh_salted_ip)
	lbl4.pack()
	
def get_smallest_hash():
	pass
	
label1 = tk.Label(root, text="Lets have fun with hashing", padx=20, pady=20)
label1.pack()
label2=tk.Label(root, text="Enter the input to get hash")
label2.pack()
e1= tk.Entry(root,  show= '*')
e1.pack(pady=40)

label3 = tk.Label(root, text="Enter the input again to confirm:")
label3.pack()

e2= tk.Entry(root, show= '*')
e2.pack(pady=40)

btn1= tk.Button(root, text="Click to get  hash of input ", padx=20, pady=20,command= get_hash)
btn1.pack()
label4= tk.Label(root, text="Add a passphrase or pin (salt) for more security", pady=40)
label4.pack()
e_salt= tk.Entry(root, show='*')
e_salt.pack(pady=40)
btn2 = tk.Button(root, text= 'Click to get hash of hashed input+hashed passphrase )' , command= get_salted_hash)
btn2.pack()


root.mainloop()
