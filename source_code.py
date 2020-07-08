#program_code
import wikipedia, webbrowser

def getPage():
    wikipage = wikipedia.random(1)
    wikiload = wikipedia.page(wikipage)
    
    userchoice = input('Would you like to read about {}? (Y/N/Q)'.format(wikipage)).lower().strip()
    if(userchoice == 'y' or userchoice == 'yes'):
        print("\n Summary: \n-------\n")
        print(wikiload.summary)
        wikiopen = input('\n Open wiki page in browser? (Y/N) ').lower().strip()
        if( wikiopen == 'y' or wikiopen == 'yes'):
            webbrowser.open(wikiload.url, new=2)
        else:
            getPage()
        exit(0)
    elif(userchoice == 'q' or userchoice == 'quit'):
        exit(0)
    else:
        getPage()

if __name__ == "__main__":
    getPage()          
        
        
        
