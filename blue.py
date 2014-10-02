def blue():
  P = makeEmptyPicture(200,200,blue)  
  show(P)
  for row in range(200):
    for col in range(200):
      p=getPixel(P,col,row)
    