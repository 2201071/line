#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
import time
from xml.dom.minidom import parse
import sys
if len(sys.argv) < 4:
    print("USE: "+sys.argv[0]+" <openfile>.svg <addX> <addY>")
    quit()
x: float = float(sys.argv[2])
y: float = float(sys.argv[3])
domTree = parse(sys.argv[1])
rootNode = domTree.documentElement
tagArr: list[str] = ["line", "text", "image", "circle", "tspan"]
attrArr: list[str] = ["x", "x1", "x2", "cx", "y", "y1", "y2", "cy"]
for tag in tagArr:
    eles = rootNode.getElementsByTagName(tag)
    for ele in eles:
        for attr in attrArr:
            valStr: str = ele.getAttribute(attr)
            if len(valStr) > 0:
                valNum: float = float(valStr)
                if attr[0] == "x" or attr[-1] == "x":
                    valNum += x
                else:
                    valNum += y
                valStrNew: str = str(valNum)
                if int(valStrNew.split(".")[1]) == 0:
                    valStrNew = str(int(valNum))
                print("["+sys.argv[0]+" "+time.ctime()+"] tag: "+tag+" , att: "+attr +
                      " , "+valStr+" -> "+valStrNew)
                ele.setAttribute(attr, valStrNew)
fnameArr: list[str] = sys.argv[1].split(".")
newFName: str = fnameArr[0]+"_mv."+fnameArr[1]
with open(newFName, "w") as f:
    domTree.writexml(f, addindent="  ", encoding="utf-8")
