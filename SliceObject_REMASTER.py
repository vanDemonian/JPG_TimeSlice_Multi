#!/usr/local/Cellar/python
# -*- coding: utf-8 -*-

class SliceObject:

	objectCount = 0

	def __init__(self, namePath):
		self.namePath = namePath

		SliceObject.objectCount += 1
		self.ObjectNumber = SliceObject.objectCount


	def displaySliceObjectCount(self):
		print "Total SliceObject Count %d" % SliceObject.objectCount


	
		return






