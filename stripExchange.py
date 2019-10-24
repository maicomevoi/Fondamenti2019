# Completare il codice per elaborare una immagine in strisce verticali che
# vengono scambiate tra loro (ogni striscia viene scambiata con quella adiacente
# alla sua destra);
# i ... indicano la mancanza di una o piu' parti di codice

def stripExchange(pict, colIndex, stripWidth):
# @param pict: Picture
# @param colIndex: int
# @param stripWidth: int

  for x in range(colIndex, colIndex + stripWidth):
    for y in range(0, getHeight(pict)) :
      pSx = getPixel(pict, x, y)
      pDx = getPixel(pict, x+stripWidth, y)
      colorSx = getColor(pSx)
      colorDx = getColor(pDx)
      setColor(pSx, colorDx)
      setColor(pDx, colorSx)


def verticalStrips(pict, stripWidth) :
# @param pict: Picture
# @param stripWidth: int; ampiezza di una striscia (da scambiare con quella adiacente)
  for c in range(0, getWidth(pict)-getWidth(pict)%(2*stripWidth), 2*stripWidth):  
    stripExchange(pict, c, stripWidth)
    
    
