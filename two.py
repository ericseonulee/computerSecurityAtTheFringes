#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys
from hashlib import sha256
blob = """
                      Hd��TX��,e:��V�4�k��� ?�x!��	8ӯ�.c��2,j�)���wD?�b��[J�UΤ;�d�*��@�����L==]a��͍���ŏ����h*��)?�|L+��3*]��l?��
"""

if sha256(blob.encode('utf-8')).hexdigest() == "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b":
    print("Hashing is not encryption")
elif sha256(blob.encode('utf-8')).hexdigest() == "e647ab380e7c7a2e62a6da22fad0e63317ea4bee384e3a80b8c5fb548d1df44e":
    print("Security through obscurity!")

print(sha256(blob.encode('utf-8')).hexdigest())