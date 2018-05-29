def click(obj, heihgt, width):
	'''
	func that simulates mouse clicks in areas as Bot
	works from BOT to TOP and LEFT to RIGHT!

	Put only from 1 to 10 indexes for easy placement!

	'''

	if heihgt > 10 or width > 10:
		raise ValueError('Put only from 1 to 10 indexes for easy placement!')
	else:
	    heihgt = 10 - heihgt #make height placemanet from botom to top
	    if width != 0:
		    width -= 1
	    else:
		    raise ValueError('Second index "<= 0"')

	    obj[width][heihgt].click()
