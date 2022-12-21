'''
copitor.py: creates a file and a copy of the file

Created By  : stepanova13
'''
import logging

logging.basicConfig(filename='Python\copitor.log', filemode='w', level=logging.INFO)
logger = logging.getLogger()

def write_story():
    ''' 
    this function creates a file
    args: None
    return: None 
    '''
    with open ('Python\\story.txt', 'w') as f:
        f.write('Alice\'s Adventures in Wonderland\n')
        f.write('\nCHAPTER I\n')
        f.write('\nDown the Rabbit-Hole\n')
        f.write("\nAlice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, `and what is the use of a book,' thought Alice `without pictures or conversation?'\n")
        f.write("So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.\n")
        f.write("There was nothing so very remarkable in that; nor did Alice think it so very much out of the way to hear the Rabbit say to itself, `Oh dear! Oh dear! I shall be late!' (when she thought it over afterwards, it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but when the Rabbit actually took a watch out of its waistcoat-pocket, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and fortunately was just in time to see it pop down a large rabbit-hole under the hedge.\n")
    return

def copy(file1, file2):
    '''
    this function takes in two files and copies the contents of the first file into the second file
    args: file1(text file), file2(text file)
    return: None
    '''
    with open('Python\\story.txt', 'r') as first, open ('Python\\story_copy.txt', 'w') as second:
        for text in first:
            second.write(text)
    return None

# body of the main
if __name__ == '__main__':
    try:
        # call the funstion to create a file
        write_story()
        # call the copy function to create a second file and copy the content of the first file into the second file
        copy('story.txt','story_copy.txt' )

    # handle exceptions
    except FileNotFoundError:
        logger.error("This file does not exist. Please make sure the file you are trying to reach exists.")
    except TypeError:
        logger.error("You had a typo.")
    except MemoryError:
        logger.error("You ran out of memory. Try to delete some objects")
    except Exception as error:
        logger.error(f"There is an error: {error}")
