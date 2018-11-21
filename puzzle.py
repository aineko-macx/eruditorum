import string
import hashlib

""" 
Upon visual inspection, puzzle.txt contains 100073 lines, each consisting of 32 hex characters (consistent with md5 hashes). The first corresponds to the md5 hash of the empty string, the second to the letter W, the third to the string 'Wh', the fourth to the string 'Who'. Idea is to loop through all printable characters and append each to the previous plaintext string. After each append operation, hash the resulting string with md5 and compare the result to the next line of ciphertext.
"""


input_file = open('puzzle.txt', 'r')

md5_LineArray = input_file.read().splitlines()[1:] #strip off empty string

plaintext = ""
Chars = []

##***********SECTION 1: MD5***************************

"""Optimization:
1.) Wrap the for loops into a function, then simply call the function 3 times, instead of repeatedly opening and closing files. the function can take as args the input file, the desired algorithm, and output file.
"""


#Create an array of all printable characters. We iterate through this later
for char in string.printable:
  Chars.append(char)

for line in md5_LineArray:
  
  #Assume the plaintext for each line is that of the previous line plus a printable char. This methodology fails if this assumption does.
  next_line = plaintext

  for char in Chars:

    #Iterate through the Char array and try adding each printable char
    next_line = plaintext + char

    #Hash each potential next_line  using md5 from hashlib
    #Compare each md5 digest to the next plaintext line
    if getattr(hashlib, 'md5')(next_line.encode()).hexdigest() == line:
      plaintext = next_line

      break



#Split the remaining plaintext (on newline) into an array
md5_plaintext = plaintext.splitlines()

#Upon inspection, First line is printable text; print to screen
#Upon inspection, rest of document appears to be more hash digests. Print to file
output_file = open('md5_plaintext', 'w')

print('\n',md5_plaintext[0])

for line in md5_plaintext[1:]:
  output_file.write("%s\n" % line)

#Cleanup
input_file.close()
output_file.close()

"""Upon inspection of md5_plaintext, the output of the previous section, there are 2440 lines of 40 hex digits each. These lines correspond in size to 160-bit SHA-1 digests. Again, the first corresponds to the hash of the empty string, the second to 'W,' and so we use the same methodology to determine plaintext that hashes to each line in the file."""


##***********SECTION 2: SHA1***************************
input_file = open('md5_plaintext', 'r')

sha1_LineArray = input_file.read().splitlines()[1:] #strip off empty string

plaintext = ""
Chars = []


#Create an array of all printable characters. We iterate through this later
for char in string.printable:
  Chars.append(char)

for line in sha1_LineArray:
  
  #Assume the plaintext for each line is that of the previous line plus a printable char
  next_lines = plaintext

  for char in Chars:

    #Iterate through the Char array and try adding each printable char
    next_line  = plaintext + char

    #Hash each guess using sha1 from hashlib
    #Compare each sha1 digest to the next plaintext line
    if getattr(hashlib, 'sha1')(next_line.encode()).hexdigest() == line:
      plaintext = next_line

      break



#Split the remaining plaintext (on newline) into an array
sha1_plaintext = plaintext.splitlines()

#Print the first line to screen and remaining hashes to output file
output_file = open('sha1_plaintext', 'w')

print('\n',sha1_plaintext[0])

for line in sha1_plaintext[1:]:
  output_file.write("%s\n" % line)

output_file.close()
input_file.close()

""" sha1_plaintext file contains 38 lines of 64 hex chars (256 bits) each. Through (numerous)  trial and error), the first corresponds to the empty string and the second to the char 'W' when hashed using SHA-3 with 256 bit digests.
"""

##***********SECTION 3: SHA3_256***************************
input_file = open('sha1_plaintext', 'r')

sha3_LineArray = input_file.read().splitlines()[1:] #strip off empty string

plaintext = ""
Chars = []


#Create an array of all printable characters. We iterate through this later
for char in string.printable:
  Chars.append(char)

for line in sha3_LineArray:
  
  #Assume the plaintext for each line is that of the previous line plus a printable char
  next_line = plaintext

  for char in Chars:

    #Iterate through the Char array and try adding each printable char
    next_line = plaintext + char

    #Compare each 256 bit sha3 digest to the next plaintext line
    if getattr(hashlib, 'sha3_256')(next_line.encode()).hexdigest() == line:
      plaintext = next_line

      break



#Split the remaining plaintext (on newline) into an array
sha3_plaintext = plaintext.splitlines()



#Print the first line to screen and remaining hashes to output file
#Output file is empty upon inspection, so solution has been reached. 
output_file = open('sha3_plaintext', 'w')

print('\n',sha3_plaintext[0])

for line in sha3_plaintext[1:]:
  output_file.write("%s\n" % line)
input_file.close()
output_file.close()


