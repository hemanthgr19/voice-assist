from selenium import webdriver

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_info(self,query):
        self.query = query
        self.driver.get(url='https://www.wikipedia.org/')
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()

#assist = infow()
#assist.get_info('python')

    #if 'information' and 'search' in text2:
        #speak("what kind of information do you want?")

        #with sr.Microphone() as source:
            #r.energy_threshold = 10000
            #r.adjust_for_ambient_noise(source, 1.2)
            #print("listining...")
           # audio = r.listen(source)
           # infor = r.recognize_google(audio)

       # assist = infow()
       # assist.get_info(infor)#