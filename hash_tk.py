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
root.geometry('600x400')

# reusable hash function
def get_sha256(input_str= None):
	if input_str is None:
		input_str= input("Enter any text or passphrase to get sha256 hash: ")
	hash_op = hs.sha256(input_str.encode('utf-8')).hexdigest()
	return(hash_op)

def get_hsh_cmd():
	hsh_input = e1.get()
	hsh_confirm = e2.get()
	if hsh_input == hsh_confirm:
		hsh_output = get_sha256(hsh_input)
		lbl2 = tk.Label(root, text= hsh_output)
		lbl2.pack()
	else:
		lbl3= tk.Label(root, text= "The inputs don't match")
		lbl3.pack()
	e1.delete(0, tk.END) # we can use END without tk in case we import * from tkinter
	e2.delete(0, tk.END)

		
		
def salted_hsh_cmd():
	ip_text_hsh = get_sha256(e1.get())
	salt_hsh=   get_sha256(e_salt.get())
	salted_ip = ip_text_hsh + salt_hsh
	hsh_salted_ip = get_sha256(salted_ip)
	lbl4= tk.Label(root, text= hsh_salted_ip)
	lbl4.pack()
	e1.delete(0, tk.END)
	e2.delete(0, tk.END)
	e_salt.delete(0,tk.END)

def get_smallest_hash():
	pass
	
label1 = tk.Label(root, text="Lets have fun with hashing")
label1.pack(padx=10,pady=(10,20))
label2=tk.Label(root, text="Enter the input to get hash")
label2.pack(padx=10,pady=(10,5))
e1= tk.Entry(root,  show= '*')
e1.pack(pady=(0,20))

label3 = tk.Label(root, text="Enter the input again to confirm:")
label3.pack(padx=10,pady=(0,5))

e2= tk.Entry(root, show= '*')
e2.pack(pady=(0,10))

btn1= tk.Button(root, text="Click to get  hash of input ", command= get_hsh_cmd)
btn1.pack(padx=5,pady=(0,10))
label4= tk.Label(root, text="Add a passphrase or pin (salt) for more security")
label4.pack(pady=(10,0))
e_salt= tk.Entry(root, show= '*')
e_salt.pack(pady=(5,10))
btn2 = tk.Button(root, text= 'Click to get hash of hashed input+hashed passphrase )', command= salted_hsh_cmd)
btn2.pack(padx=5,pady=(0,5))


root.mainloop()
