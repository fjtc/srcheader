#!/usr/bin/python
# -*- coding: utf-8 -*-
# BSD 3-Clause License
# 
# Copyright (c) 2018, Fabio Jun Takada Chino
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
import codecs

class SourceFile:
	def __init__(self, file_name, encoding='utf-8'):
		self._encoding = encoding
		self._contents = None
		self._file_name = file_name

	@property
	def encoding(self):
		return self._encoding

	@encoding.setter
	def set_encoding(self, encoding):
		self._encoding = encoding

	@property
	def contents(self):
		return self._contents

	@contents.setter
	def set_contents(self, contents):
		self._contents = contents

	def has_contents(self):
		return not (self.contents is None)

	@property
	def file_name(self):
		return self._file_name


	def load(self):
		with codecs.open(self.file_name, 'r', encoding=self.encoding) as inp:
			self.contents = inp.read()

	def save(self):
		if (not self.has_contents()):
			raise RuntimeError('Contents not set.') 
		with codecs.open(self.file_name, 'w', encoding=self.encoding) as outp:
			outp.write(self.contents)
			
class Source:
	def __init__(self):
		self.prefix = None
		self.header = None
		self.suffix = None
	
	@property
	def prefix(self):
		return self._prefix
	
	@prefix.setter
	def set_prefix(self, prefix):
		self._prefix = prefix
	
	@property
	def header(self):
		return self._header
	
	@header.setter
	def set_header(self, header):
		self._header = header

	@property
	def suffix(self):
		return self._suffix
	
	@suffix.setter
	def set_suffix(self, suffix):
		self._suffix = suffix

	def __str__(self):
		s = ''
		if not self.prefix is None:
			s = s + self.prefix
		if not self.header is None:
			s = s + self.header
		if not self.suffix is None:
			s = s + self.suffix
		return s
	
class StringStream:
	
	def __init__(self, text):
		self._text = text
		self._offset = 0
	
	def has_more(self):
		return self._offset < len(self._text)
	
	def getc(self):
		if self.has_more():
			c = self._text[self._offset]
			self._offset = self._offset + 1
			return c 
		else:
			return None
	
	def ungetc(self):
		if (self._offset > 0):
			self._offset = self._offset - 1

class SourceParser:
	
	def parse_source(self, src):
		return self.parse_text(src.contents)
	
	def parse_text(self, text):
		return None

class CSourceParser(SourceParser):
	
	def _extract_prefix(self, src):
		None
	
	def parse_text(self, text):
		None
