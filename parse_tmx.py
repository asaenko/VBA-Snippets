#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
 
#----------------------------------------------------------------------
def viewTMX(tmx_file):
    """
    Parse TMX with ElementTree
    """
    tree = ET.ElementTree(file=tmx_file)
    root = tree.getroot()

    # iterate over the entire tree
    print ("-" * 40)
    print ("Iterating using a tree iterator")
    print ("-" * 40)
    iter_ = tree.getiterator()
    for elem in iter_:
        if elem.tag == 'seg':
            print(elem.text)

    # lists TUs recursively, kind of manual way
    # for child in root:
    #     print(child.tag, child.attrib)
    #     if child.tag == "body":
    #         for step_child in child:
    #             for grandchild in step_child:
    #                 for greatgrandchild in grandchild:
    #                     if greatgrandchild.tag == 'seg':
    #                         print(greatgrandchild.text)
#----------------------------------------------------------------------
if __name__ == "__main__":
    viewTMX("EN_RU_TECH.tmx")