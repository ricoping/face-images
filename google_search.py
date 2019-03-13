import os, time
import requests,bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

class googleSearch():
	def __init__(self, query, scroll_times=10, path="google_data"):
		self.path=path
		self.save_path=os.path.join(path, query)
		self.script_path=os.path.dirname(__file__)
		self.url="https://www.google.com/search?q=%s&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj43bOey_ngAhVDEbwKHdkbBh8Q_AUIDigB&biw=1178&bih=760" % query
		self.query=query
		self.scroll_times = scroll_times
		self.source=self.getSourceDynamic()

		if not os.path.exists(path):
			os.mkdir(path)

		if not os.path.exists(self.save_path):
			os.mkdir(self.save_path)

	def getSourceDynamic(self):
		try:
			print("Getting source...")
			options = Options()
			options.add_argument('-headless')
			exe_path = os.path.abspath(os.path.join(self.script_path, "geckodriver.exe"))
			browser = webdriver.Firefox(executable_path = exe_path, firefox_options=options)
			browser.get(self.url)

			for i in range(self.scroll_times):
				time.sleep(0.5)
				script = "window.scrollTo(0, window.pageYOffset + " + str(3000) + ");"
				browser.execute_script(script)

			source = browser.page_source
			browser.close()
			return source

		except:
			print("Couldn't get %s ." % self.url)

	def getUrls(self):
		sp = bs4.BeautifulSoup(self.source,"html.parser")
		imgs = sp.select('.rg_ic')
		urls=[]
		for img in imgs:
			try:
				urls.append(img["data-src"])
			except:
				continue
		return urls

	def imageDownload(self, url, filename):
		response = requests.get(url)
		response.raise_for_status

		imgFile = open(os.path.join(self.script_path, self.save_path, filename), 'wb')
		print("Downloading...." + str(filename))
		for chunk in response.iter_content(100000):
			imgFile.write(chunk)
		imgFile.close()

	def saveImages(self):
		urls=self.getUrls()
		for i, url in enumerate(urls):
			self.imageDownload(url, self.query + "_" + str(i) + ".jpg")


if __name__ == "__main__":
	gs = googleSearch("佐々木希")
	gs.saveImages()