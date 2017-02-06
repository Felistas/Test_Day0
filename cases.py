def case(a):
	if type (a) is str:
		return True
	if type(a) is int:
		return True
	if type(a) is list:
		return True
	if type(a) is dict:
		return True
	if type(a) is float:
		return True
	if a%2==0:
		return True
	if a%2!=0:
		return True
	if a==0:
		return True
	if a>0:
		return True
	if a<0:
		return True