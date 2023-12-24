import cv2
import insightface
from insightface.app import FaceAnalysis

app = FaceAnalysis(providers=['CPUExecutionProvider'])
app.prepare(ctx_id=-1, det_size=(640, 640))

img = cv2.imread('sample.jpg')

faces = app.get(img)
# print(faces)

rimg = app.draw_on(img, faces)
cv2.imwrite("./t1_output.jpg", rimg)