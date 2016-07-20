#!/usr/bin/env python

import sys
import os
import glob

def getFileNames(folder):
  return glob.glob("%s/*.txt" % folder)

def getOffsetUpToWord(words, index):
  if(index == 0):
    return 0
  subList = words[0:index]
  length = 0
  for w in subList:
    length += len(w)
  return length + index + 1
        
def getWords(content, filename, wordIndexDict):

  STRIP_CHARS = ",.\t\n |"
  currentOffset = 0

  for line in content:
    line = line.strip(STRIP_CHARS)
    localWords = line.split()
    for (idx, word) in enumerate(localWords):
      word = word.strip(STRIP_CHARS)
      if wordIndexDict.get(word) == None:
        wordIndexDict[word] = []

      line_offset = getOffsetUpToWord(localWords, idx) 
      index = (line_offset) + currentOffset
      currentOffset = index 
      wordIndexDict[word].append([filename, index])

  return wordIndexDict

def readFileContent(filepath):
    f = open(filepath, 'r')
    return f.read().split( ' ' )

def list2dict(list):
  res = {}
  for item in list:
    if(res.get(item[0]) == None):
      res[item[0]] = []
    res[item[0]].append(item[1])
  return res

def saveIndex(index):
  lines = []
  for word in index:
    indexLine = ""
    glue = ""
    for filename in index[word]:
      indexLine += "%s(%s, %s)" % (glue, filename, ','.join(map(str, index[word][filename])))
      glue = ","
    lines.append("%s, %s" % (word, indexLine))

  f = open("index-file.txt", "w")
  f.write("\n".join(lines))
  f.close()

def __start__():
  files = getFileNames('./files')
  words = {}
  for f in files:
    content = readFileContent(f)
    words = getWords(content, f, words)
  for word in (words):
    words[word] = list2dict(words[word])
  saveIndex(words)

__start__()
