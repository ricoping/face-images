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

![g1](https://user-images.githubusercontent.com/47266653/54268646-0109cb80-45bf-11e9-9c6f-6fcad38d672c.png)

## 2. Extract faces by *img_cut.py*
~~~
import img_cut
ic = img_cut.imgCut("佐々木希")
~~~

![g2](https://user-images.githubusercontent.com/47266653/54268703-2a2a5c00-45bf-11e9-9025-2918b4bcca00.png)
