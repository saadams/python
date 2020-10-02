import os

'''f = open("pyTest.txt","a")
f.write( "hello world how are u\n")
f.write("hello")
f.close()


f = open("pyTest.txt", "rt")

print(f.readline())
f.close()
'''
def main():
	if os.path.exists("newPyFile.txt"):
		#os.remove("newPyFile.txt")
		f = open("newPyFile.txt", "r+")
		print("newPyFile: \n" + f.read())
		inputText = input("what would you like to add tto the file? ")
    
		f.write(inputText)
		print("newPyFile: \n" + f.read())
		f.close()
	else:
		f = open("newPyFile.txt", "x")
		print("file has been created")

    
'''
f = open("newPyFile.txt","a") #w to overwrite
f.write("file writting...")
f.close()

f = open("newPyFile.txt","rt")
print(f.read())
'''
main()