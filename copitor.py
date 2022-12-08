
def write_story(text):
    ''' 
    This function creates a file.
    
    Parameters:
    str: a string that the file will content

    '''
    with open ('Python\\story.txt', 'a') as f:
        f.write(text)

line1 ="CHAPTER I"

# call the funstion to create a file
write_story(line1)

def copy(file1, file2):
    '''
    This function  takes in two file names and copies the contents of the first file into the second file.
    '''
    with open('Python\\story.txt', 'r') as first, open ('Python\\story_copy.txt', 'w') as second:
        for text in first:
            second.write(text)

# call the function
copy('story.txt','story_copy.txt' )