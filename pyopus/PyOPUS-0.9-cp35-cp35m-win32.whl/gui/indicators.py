from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import math

__all__ = [ 'QPRelativePosition', 'QPPerformanceConstraint', 'QPPerformanceRange' ]

class QPBarIndicator(QWidget):
	def __init__(self, hborder=4, vborder=6, h=None, x1=0.0, x2=1.0, parent=None, *args):
		QWidget.__init__(self, parent, *args)
		
		self.x1=x1
		self.x2=x2
		self.hborder=hborder
		self.vborder=vborder
		if h is not None:
			self.h=h
		else:
			fm=QFontMetrics(QFont())
			self.h=fm.height()
		
		self.setMaximumHeight(self.h+2*self.vborder)
			
	def minimumSizeHint(self):
		return QSize(50+2*self.hborder, self.h+2*self.vborder);
	
	def paintBackground(self, color, painter):
		w=self.width()
		h=self.height()
		
		we=w-2*self.hborder
		he=h-2*self.vborder
		
		painter.save()
		painter.setRenderHint(QPainter.Antialiasing, False)
		painter.setBrush(QBrush(color))
		pen=QPen(Qt.black)
		pen.setWidth(0)
		painter.setPen(pen)
		
		painter.drawRect(self.hborder, self.vborder, we, he)
		
		painter.restore()
	
	def bound(self, x):
		if x<self.x1:
			return self.x1
		elif x>self.x2:
			return self.x2
		else:
			return x
		
	def paintBar(self, xfrom, xto, color, painter):
		w=self.width()
		h=self.height()
		
		we=w-2*self.hborder
		he=h-2*self.vborder
		
		xpf=round(we/(self.x2-self.x1)*(self.bound(xfrom)-self.x1))
		xpt=round(we/(self.x2-self.x1)*(self.bound(xto)-self.x1))
		
		painter.save()
		painter.setBrush(QBrush(color))
		pen=QPen(Qt.black)
		pen.setWidth(0)
		painter.setPen(pen)
		
		if xpt>=xpf:
			painter.drawRect(self.hborder+xpf, self.vborder, xpt-xpf, he)
		else:
			painter.drawRect(self.hborder+xpt, self.vborder, xpf-xpt, he)
			
		painter.restore()
	
	def paintAnchors(self, posList, painter, extend=2):
		w=self.width()
		h=self.height()
		
		we=w-2*self.hborder
		he=h-2*self.vborder
		
		xpl=[ round(we/(self.x2-self.x1)*(self.bound(x)-self.x1)) for x in posList ]
		
		painter.save()
		pen=QPen(Qt.black)
		pen.setWidth(0)
		painter.setPen(pen)
			
		for xp in xpl:
			painter.drawLine(self.hborder+xp, self.vborder-extend, self.hborder+xp, self.vborder+he+extend)
		
		painter.restore()
	
	def paintTicks(self, posList, painter, relExtend=0.25, absExtend=2):
		w=self.width()
		h=self.height()
		
		we=w-2*self.hborder
		he=h-2*self.vborder
		
		xpl=[ round(we/(self.x2-self.x1)*(self.bound(x)-self.x1)) for x in posList ]
		
		dyp=math.floor(relExtend*he)
		dyp=dyp if dyp>absExtend else absExtend
		
		painter.save()
		pen=QPen(Qt.black)
		pen.setWidth(0)
		painter.setPen(pen)
		
		for xp in xpl:
			painter.drawLine(self.hborder+xp, h-self.vborder-1, self.hborder+xp, h-self.vborder-dyp-1)
		
		painter.restore()
		
		
class QPRelativePosition(QPBarIndicator):
	def __init__(self, pos, parent=None, *args):
		QPBarIndicator.__init__(self, parent=parent, *args)
		self.pos=pos 
		
	def setPos(self, pos):
		self.pos=pos 
		self.update()
		
	def paintEvent(self, ev):
		p=QPainter(self)
		
		self.paintBackground(QColor(Qt.lightGray), p)
		self.paintBar(0.0, self.pos, QColor(Qt.green), p)
	

class QPPerformanceConstraint(QPBarIndicator):
	def __init__(self, pos, constraint='above', lo=-10.0, hi=10.0, tick=1.0, parent=None, *args):
		QPBarIndicator.__init__(self, x1=lo, x2=hi, parent=parent, *args)
		self.constraint=constraint
		self.tick=tick
		self.failed=False
		self.setPos(pos, repaint=False)
		
	def setPos(self, pos, repaint=True):
		self.pos=pos 
		
		if self.pos is None:
			self.failed=True
		elif (
			(self.constraint=='above' and self.pos<0) or
			(self.constraint=='below' and self.pos>0)
		):
			self.failed=True
		else:
			self.failed=False
		
		if repaint:
			self.update()
	
	def paintEvent(self, ev):
		p=QPainter(self)
		
		baseColor=QColor(Qt.green) if not self.failed else QColor(Qt.red)
		
		if self.pos is None:
			self.paintBackground(baseColor, p)
		else:
			self.paintBackground(baseColor.lighter(180), p)
			self.paintBar(0.0, self.pos, baseColor, p)
			
		self.paintAnchors([0.0], p)
		
		# Count ticks, paint them if there are at least 2 pixels/tick
		nTicks=self.x2-self.x1
		w=self.width()
		if self.width()*1.0/nTicks>=2:
			self.paintTicks(range(math.floor(self.x1)-1, math.ceil(self.x2)+1), p)
		
		
class QPPerformanceRange(QPBarIndicator):
	def __init__(self, pos, lo, hi, norm, constraint='inside', span=3.0, parent=None, *args):
		self.center=(hi+lo)/2
		self.delta=(hi-lo)
		if self.delta==0:
			self.delta=norm*20
		QPBarIndicator.__init__(self, x1=lo-self.delta*(span-1)/2, x2=hi+self.delta*(span-1)/2, parent=parent, *args)
		self.lo=lo
		self.hi=hi
		self.norm=norm
		self.constraint=constraint
		self.span=span
		self.failed=False
		self.setPos(pos, repaint=False)
		
	def setPos(self, pos, repaint=True):
		self.pos=pos 
		
		if self.pos is None:
			self.failed=True
		elif (
			(self.constraint=='inside' and (self.pos<self.lo or self.pos>self.hi)) or
			(self.constraint=='outside' and (self.pos>self.lo and self.pos<self.hi))
		):
			self.failed=True 
		else:
			self.failed=False
		
		if repaint:
			self.update()
		
	def paintEvent(self, ev):
		p=QPainter(self)
		
		baseColor=QColor(Qt.green) if not self.failed else QColor(Qt.red)
		
		if self.pos is None:
			self.paintBackground(baseColor, p)
		else:
			self.paintBackground(baseColor.lighter(180), p)
			if self.pos<self.lo:
				self.paintBar(self.lo, self.pos, baseColor, p)
			elif self.pos>self.hi:
				self.paintBar(self.hi, self.pos, baseColor, p)
			else:
				self.paintBar(self.lo, self.hi, baseColor, p)
				self.paintAnchors([self.pos], p, extend=0)
		
		# Count ticks, paint them if there are at least 2 pixels/tick
		nTicks=(self.x2-self.x1)/self.norm
		w=self.width()
		if self.width()*1.0/nTicks>=2:
			xtl1=[ x*self.norm+self.center for x in range(0, math.ceil((self.x2-self.center)/self.norm)+1) ]
			xtl2=[ x*self.norm+self.center for x in range(math.floor((self.x1-self.center)/self.norm)-1, 0) ]
			self.paintTicks(xtl1+xtl2, p)
			
		self.paintAnchors([self.lo, self.hi], p)
		
		return None
	
		
if __name__=='__main__':
	import sip, sys
	
	sip.setdestroyonexit(True)
	
	app = QApplication(sys.argv)
	
	ind = QPRelativePosition(0.5)
	ind.show()
	
	app.exec_()
	
	
