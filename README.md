# Face image getter

## requirements
*cv2*, *bs4*, *selenium*

## How to
### 1. Get images by *google_search.py*
~~~
import google_search
gs = google_search.googleSearch("佐々木希")
gs.saveImages()
~~~

You get *google_data/佐々木希/\*.jpg*

## 2. Extract faces by *img_cut.py*
~~~
import img_cut
ic = img_cut.imgCut("佐々木希")
~~~
