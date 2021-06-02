from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")


PATH = "C:\Program Files (x86)\chromedriver.exe"

# TODO: Opera implementation is quite buggy annoyingly. It won't close at the moment
# Need to investigate.
driver = webdriver.Chrome(PATH, options=chrome_options)
channel = input('Channel Name: ')
print('''
----------------------------------
Loading URL for latest video...
----------------------------------
 ''')

if channel:
	link = f"https://www.youtube.com/c/{channel}/videos"

	driver.get(link)
	video = driver.find_element_by_id('video-title')
	title = video.text
	print(channel + " latest video is:")
	print(title)
	print('''
What would you like to do?
	1. Watch video
	2. Quit
	 ''')
	selection = input()
	if selection:
		if selection == '1':
			d = webdriver.Chrome(PATH)
			d.get(link)
			video = d.find_element_by_id('video-title')
			video.click()
			exit = input("type any key and press enter to exit\n")
			if exit:
				driver.quit()
		else:
			driver.quit()



