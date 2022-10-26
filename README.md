# hash-gui-tkinter
Graphical Interface for storing text by hashing
# Overview
Any text or data can be converted to a hash using secure hash algorithms like sha256 or sha512.
We can generate hashes by using the hashlib library of python. 
For a user interface tkinter module of python can be used.
# Storing only few digits of the 64 digits of the hex code
  Storing only few digits of the hash code of any input is a simple and easy way to remember passwords or some data without the need to actually storing the passwords. We can use this code to check if the input we used for something generates the same hash initial digits.
  
  For example if we used a password 12345 for something then we can store the hash of the 12345 or combine a passphrase or pin and then store the few digits of the resultant hash.
  
  Now when we are using the same service and want to check if we used 12345 or 123456 then we can use this code to check if we are getting the same hash digits or not. The best part of the hashing algorithm is that any change in input will result in totally different hash digits. 
  
  You can also check that the sha256 hash of 12345 is 59944... and that of 123456 is 8d969..... .
  Now since yoy had stored 59944 as your code for your password you know that 123456 is not the correct password.
  This same concept can be further enhanced to use a passphrase along with an input/password or adding additional digits before generating hash. This will make the program a bit complex but will add more security. It is similar to adding a salt to the password.

  To demonstrate further we can have 
  a: input data or password
  p: passphrase
  h(a): hash of a
  h(p): hash of p
  simple hashing: we can use the few digits of h(a)
  next level: we can join (a) and (p) and then get hash(a+p) and store the few digits
  next level: we can join hash(a) + hash(p) to get hash( hash(a) + hahs(p) ) and then store the few digits.
  next level: we can have any method to join hash(a) + 'someting' + hash(p) + 'sometging else' and then get the hash of the result and thus have infinite possibilities to make our own code for few digits.
  So if someone else doesn't have the your program, they will not be able to make out anything of the few hash digits you have stored somewhere.

  next level: store the characters of the input or password with your own way to join hashes of the character, the passphrase and any other sequence data. Then you can use the same code to get the characters back and thus getting your input or password back using the phassphrase and the program. The code for such a program is in my repository https://github.com/satverm/Password-Manager where some structured sequence is used to generate hashes uing a passphrase and then the same passphrase is used to recover the characters in case you forgot.




