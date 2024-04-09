"""A python module to automaticaly fish in Minecraft"""
import sys
import time
import base64

import keyboard
import pyautogui
import requests

from base64 import b64decode
from io import BytesIO
from PIL import Image
pyautogui.useImageNotFoundException()

#embed original PNG file instead of attempting to fetch from web
myb64image = "iVBORw0KGgoAAAANSUhEUgAAAPsAAAAVCAYAAACAPJhUAAAE6UlEQVR4nO3a3VKrMBAAYO+r/Nop1rY6o77/A/kwnAsbCNvsfwLVORc7cyo5KQn7kQ304akZxnS8iKLujmPdHcXtb2MYn7qTPJDzrdoXMsJ5UhHOieuLCsmYd/VAhn0u56j6i2jM3sg1lqo7k/HYnhxxHpvnt7F5fhvbwycazf4jW+Cu+Fyl80vmNHUtHpruSJ5YjsTLip481zzoPRdDgp4Dkgt9279ujj0neg/2EBT6nNgp9Hnyi3aKYm+64/j9/S2K0Bn83PavqkSE/59DP7ensedAL5lsbp4o9BIcoR8plNR8tv3rFFtjXxt9mA+InUKfA3f4Xgp9Duwc+uLYQ/iwp8FrsUsn1bqqS7Gn0GuxS6Bw2Euh12JfC/0Sexo8RF8Se4w+J3YKPYs9fNaW9qnEsmNH0CugW1d5LXbNcS92CooUe270Vuyl0UuxQ/SlsTf7j7E9fBYBD9HvqoMMOw9+ECeWHTtAb8SuQV8Sewgv9hQSLfac6L3gS6DXYg9RdZex6i7FsYcohb5qX36wh5CU8Rj6OLni5LFuA7B2t+2X349/Txq8tvzmMGv7wdpz2LH20vnEsGPnA0HDv6faw5VEc1Pz5gtEz2HHvq/bv4/d/v0GPXeeGHasXcBe96ex7k9ov578W6zw1UGGPbXSx6ia7rga9l11+I+daL8l9mk12Rh71c2Yrdgh+t+MPQRZxqcCw84lFZdkXFmKJT+HGvsMS3srdulxaXstbqw9VnFhn2FpL8GduhksSkjHNgWrXLh8gdjn8l5WxkP0cz+y8h7DDY8H7NN8XtGHsOYRDBd22B5iD8fXwh5Weit2eHxz7FckW2KPj1uxc+il2KnxSbH/xMWFHSvvS2GHK/5dYee2A1gySR/godinFeBvYMdWeil2uCpy2LnAVnrt7xM49NKbG/bgDsuXGHsIqoyHuCF6KWbuZtAPXwvsXEjL+KLYm+tF9mBPPbXXYt/Vw2KVt2IP4/gr2AN4D/bUSm/9MRJEvwV2yR5cih17kCfB3g9f4uuAlfc67NcX/VbscceS9pIy0ow9Qo/h5iY1Pud7wD4hcWCP509axlM3Zw92bqWXblNgUPhj7BApLO8x7FjA/qzY2+czWsqnQppHN9gXdyQHdgq9Ntlc2IkHeBrsFPq1sUP0VuzYSq/Bjr2j12Dn0OfEPr+jT2NPlfda7PCz5D08xB7Cgz6VNyh2uAeXYtciWgt7aj8vKeM59Nx4OdRce65/6d4XwwDRY8HdnK3YreOT/vhGih4LrnzHbgrwZsJh74evsX3mnyFwr+iovMNX9ug3vPeAHX62YIf7eSv2GP3W2GFpb8GeeqWlxR6j/y3YJeOuuosLO/fjnDWxB/APWLkhRS+9uFQf0lKS2uNxwWOQVTTacWN3Wfie3xOp8WpRwFd1lvDMC1feW7FLIlXSxyEt6alIrfQxdkl49/Qsdgq85SJuhT43duscYJVFbvSe5Pdg994MsTGVxC5BnwM8RK/F7kUvwo6ht15ADtAaK/2MYg4Ldu1cUFuJnEC8ie/FnhN9WOVLQt8Cfbd/N4PXoq/7kw47RO+9iHeD/rqf92CXJrfkYWEOID99+RPfiz0n+lxjuhf0j+15+rcFuxa9CXsAn2slugvwtX91lyS2BHsO9Mu+1kFf8lnHtMJPD1r/Bvrwft+DXYr+H4YjIYe4TEMcAAAAAElFTkSuQmCC"
mybinimage = b64decode(myb64image)

def main():
    with Image.open(BytesIO(mybinimage)) as image:
        print("Press F12 to quit the program")
        try:
            while not keyboard.is_pressed("F12"):
                try: 
                    loc = pyautogui.locateOnScreen(image, grayscale=True, confidence=0.9)
                except pyautogui.ImageNotFoundException:
                    loc = None
                if loc:
                    print("Fishing Bobber splashed!")
                    pyautogui.doubleClick(button='right', interval=0.5)
                    time.sleep(5)  # Prevent from clicking again before gone
        except KeyboardInterrupt:
            sys.exit()



if __name__ == "__main__":
    main()
