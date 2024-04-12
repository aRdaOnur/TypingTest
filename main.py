import curses
from curses import wrapper
import time
import random
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr(10,3,'To Start press any key : ')
    stdscr.getch()
    stdscr.clear()

def when_finished(user_finished,current_time,count_of_key):
    if user_finished == False :
        print('Your WPM : ' + str((count_of_key/5)))
    elif user_finished == True:
        print('Your WPM : ' + str(int(count_of_key*12/current_time)))
    print(count_of_key/5)


def random_word_generator():
    # there are 100 words in text.txt and all words are going to in text variable
    with open('text.txt','r') as word:
        text = word.readlines(1)
    
    # All of the words will be in the wordList and they will be shuffle
    wordList = ''.join(text).split()
    random.shuffle(wordList)
    #--


    # after going through the list, these codes will create new text_list 
    # which contains 10 piece of wordList and all of the piece are going to ready for print to screen 
    estr = ''
    text_list = []
    for i in range(0, 100, 10):
        for j in wordList[i:i+10]:
            estr += j + ' '
        text_list.append(estr)
        estr = ''
    return text_list
    #------



def text_printer(stdscr,text_to_be_written,text):
    stdscr.clear()
    stdscr.addstr(0,0,str(text[text_to_be_written]))

def main(stdscr):

    curses.curs_set(0) # hides to cursor

    #colors
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_BLACK,curses.COLOR_RED)
    #--
    
    

    start_screen(stdscr)
    text = random_word_generator()
    
    
    user_finished = False
    key_index = 0
    start_time = time.time()
    text_index = 0
    count_of_key = 0
    text_printer(stdscr,text_index,text)

    while True:
        
        # if someone finished at the 60 seconds the test will finished
        current_time = int(time.time() - start_time)
        if current_time >= 60 or user_finished:
            count_of_key+=key_index
            return user_finished, current_time, count_of_key
        ###-----



        ### if someone finished the test before 60 seconds 
        # user_finished will be True 
        # and these codes control the text, well if came end of the line 
        # the text should be change
        if key_index == len(text[text_index]):
            text_index+=1 
            if text_index == 9:
                user_finished = True

            count_of_key+=key_index
            key_index = 0
            text_printer(stdscr,text_index,text) # it takes new index of the text and it'll print 
        #---------


        key = stdscr.getch() # key catcher
        

        '''
        These codes are very simple 
        if pressed any key not equal to same index of the letter
        it'll be red or if equal it'll be green

        

        key = 10 is ENTER
        key = 263 is BACKSPACE in windows backspace key is 8 because of that i changed
        key = 32 is SPACE 

        '''
        if chr(key) == text[text_index][key_index]:
            stdscr.addstr(0,key_index,str(chr(key)), curses.color_pair(1))
            key_index+=1
        
        else:
            if key == 8 and key_index !=0:# backspace
                key_index-=1
                stdscr.addstr(0,key_index,str(text[text_index][key_index])) 

            elif key == 32:# space
                stdscr.addstr(0,key_index,' ', curses.color_pair(3))
                key_index+=1
            elif key == 10:
                continue
            else:
                stdscr.addstr(0,key_index,str(chr(key)), curses.color_pair(2))
                key_index+=1
        ##-------------------
    
    

user_finished, current_time, count_of_key = wrapper(main) 
when_finished(user_finished,current_time, count_of_key) # it gives some attribute to print result 
