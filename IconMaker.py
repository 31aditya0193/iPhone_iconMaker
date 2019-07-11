# Copyright (C) 2019 Aditya Mishra <31aditya0193@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limiting the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is furnished
# to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


#imports
from PIL import Image
import sys
import os

#Opening Source Image
iconSource = sys.argv[1]
imgSrc = Image.open(iconSource)

# Program Constants
sizes = [ 20, 29, 40, 58, 60, 76, 80, 87, 120, 152, 167, 180, 1024 ]
ext = ".png"

# use one of these filter options to resize the image
try:
    os.mkdir("iconPrints")
    os.chdir(os.getcwd()+"/iconPrints")
except FileExistsError:
    os.chdir(os.getcwd()+"/iconPrints")
for sz in sizes:
    res = imgSrc.resize((sz, sz))
    res.save( str(sz) + ext )
