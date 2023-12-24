import insightface
from insightface.app import FaceAnalysis

app = FaceAnalysis()
app.prepare(ctx_id=0, det_size=(640, 640))

import cv2
img = cv2.imread('sample.jpg')

faces = app.get(img)

print(faces)