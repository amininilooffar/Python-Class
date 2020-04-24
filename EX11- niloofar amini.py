>>> class time:
	hour=0
	minute=0
	second=0
	def __init__ (obj, h,m,s):
		obj.hour= h
		obj.minute= m
		obj.second= s
	def show (obj):
		return obj.hour*3600+obj.minute*60+obj.second
	def ezafe_kardan (obj,hh,mm,ss):
		obj.hour+=hh
		obj.minute+=mm
		obj.second+=ss
		return obj
	def sub (obj, obj2):
		obj.hour-=obj2.hour
		obj.minute-=obj2.minute
		obj.second-=obj2.second
		return obj
	def kam_kardan (obj, hh, mm, ss):
		obj.hour-=hh
		obj.minute-=mm
		obj.second-=ss
		return obj
	def __add__(obj1,obj2):
		obj1.hour +=obj2.hour
		obj1.minute+=obj2.minute
		obj1.second+=obj2.second
		if obj1.second>60:
			obj1.second-=60
			obj1.minute+=1
		if obj1.minute>60:
			obj1.minute-=60
			obj1.hour+=1
		return obj1
	def __repr__(obj):
		return str (obj.hour)+':'+ str (obj.minute)+':'+ str (obj.second)
	def __gt__ (obj1,obj2):
		if obj1.hour*3600+obj1.minute*60+obj1.second> obj2.hour*3600+obj2.minute*60+obj2.second:
			return True
		return False
	def __repr__(obj):
		return str (obj.hour)+':'+ str (obj.minute)+':'+ str (obj.second)
