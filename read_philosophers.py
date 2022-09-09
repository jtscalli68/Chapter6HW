# This program reads and displays the contents of the philosophers.txt file.
def main():
    # Open a file named philosophers.txt.
    infile = open('philosopher.txt', 'r')
    
    # Read the file's contents.
    line1 = infile.readline().rstrip('\n')
    line2 = infile.readline().rstrip('\n')
    line3 = infile.readline().rstrip('\n')

    # Print the data that was read into memory.
    print(line1)
    print(line2)
    print(line3)
 
 # Call the main function.
main()