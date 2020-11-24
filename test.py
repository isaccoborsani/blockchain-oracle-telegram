import base64
import codecs

x = base64.b64decode('DdYECFkzrKt31N2T41Fp+hk12zNbG3SUf7aZveF3Lgs==')
b_string = codecs.encode(x, 'hex')

print(b_string.decode('utf-8'))

#0dd604085933acab77d4dd93e35169fa1935db335b1b74947fb699bde1772e0b
#0dd604085933acab77d4dd93e35169fa1935db335b1b74947fb699bde1772e0b