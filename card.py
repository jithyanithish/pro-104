import cv2
img = cv2.imread("solar-system.jpg")
cv2.putText(img, "Sun",(90,99),cv2.FONT_HERSHEY_COMPLEX,0.9,(255,255,255))
cv2.putText(img, "Mercury",(100,180),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img, "Venus",(195,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img, "Earth",(280,176),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img, "Mars",(390,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img, "Jupiter",(500,50),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img, "Saturn",(690,99),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img, "Uranus",(950,130),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img, "Neptune",(1099,139),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.imshow("display",img)
cv2.waitKey(0)







