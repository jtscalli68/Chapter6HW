#This program writes three lines of data to a file.
def main():

    # Open a file named philosophers.txt.
    outfile = open('philosopher.txt', 'a')

    
    # Write the names of three philosphers to the file – 
    # John Locke, David Hume and Edmund Burke
    outfile.write('Jonathan Scalli\n')

    # Close the file.
    outfile.close

# Call the main function.
main()