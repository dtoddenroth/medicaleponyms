#!/usr/bin/env python3

from tempfile import TemporaryDirectory
from lxml.etree import fromstring, tostring
from os.path import dirname, basename, splitext
from hashlib import md5
from shutil import copy

from pubmedcache import PubmedCache

def extractabstract(xmlfile):
	et = fromstring(open(xmlfile,"rb").read())
	try: 
		return " ".join(et.find(".//Abstract").itertext())
	except AttributeError:
		print("Error reading abstract from %s."%xmlfile)
		return ""

def extracttitle(xmlfile):
	et = fromstring(open(xmlfile,"rb").read())
	try: 
		return " ".join(et.find(".//ArticleTitle").itertext())
	except AttributeError:
		print("Error reading title from %s."%xmlfile)
		return ""

def converttotext(xmlfile):
	title = extracttitle(xmlfile)
	abstract = extractabstract(xmlfile)
	assert len(abstract)
	pmid = splitext(basename(xmlfile))[0]
	textfile = dirname(xmlfile)+ f"/{pmid}.txt"
	with open(textfile,"wb+") as f:
		_ = f.write(f"{title}\n\n{abstract}".encode("utf-8"))
	return textfile

filemd5 = lambda fn: md5(open(fn,encoding="utf-8").read().encode()).hexdigest()
hashdict = {row.split("  ")[1].strip(): row.split("  ")[0] 
	for row in open("checksums.md5").readlines()}
pmids = open("pmids.txt").read().strip().split("\n")

if __name__=="__main__":
	with TemporaryDirectory() as tempdir:
		print(f"Downloading abstracts to temporary folder {tempdir}...")
		xmlfiles = PubmedCache(tempdir).fetch(pmids)
		print(f"Converting .xml to .txt files...")
		textfiles = [converttotext(xmlfile) 
			for xmlfile in list(xmlfiles.values())]
		print(f"Copying unmodified .txt files to ../annotations/ ...")
		matchcounter = 0
		for textfile in textfiles:
			if filemd5(textfile)==hashdict.get(basename(textfile)):
				matchcounter += 1
				_ = copy(textfile,"../annotations/")
		print(f"Copied {matchcounter} unmodified .txt files "
			f"(of {len(pmids)}) from {tempdir} to ../annotations/.")

