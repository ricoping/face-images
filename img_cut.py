import os
import cv2

class imgCut():
	def __init__(self, image_folder, path="google_data"):
		self.folder=image_folder
		self.path=os.path.join(os.path.dirname(__file__), path, image_folder)
		self.target_path=os.path.join(os.path.dirname(__file__), path, image_folder+"_cut")

		if not os.path.exists(self.target_path):
			os.mkdir(self.target_path)

		for img in os.listdir(self.path):
			try:
				self.saveFace(img)
			except:
				print("error, skip")
				continue

	def saveFace(self, filename):
		src_image = cv2.imread(os.path.join(self.path, filename))
		dst_image = cv2.cvtColor(src_image,cv2.COLOR_RGB2GRAY)
		save_path = os.path.join(self.target_path, filename)
		cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
		facerect = cascade.detectMultiScale(dst_image, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

		if len(facerect) > 0:
			for rect in facerect:
				dst_image = dst_image[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]]
				#dst_image = cv2.cvtColor(dst_image,cv2.COLOR_GRAY2RGB)
				dst_image = cv2.resize(dst_image, (100, 100))
				cv2.imwrite(save_path, dst_image)


if __name__ == "__main__":
    # execute only if run as a script
	ic = imgCut("佐々木希")