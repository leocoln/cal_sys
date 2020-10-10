import random
from fractions import Fraction

op_standrad = ['+','-','×','÷']

def mdfk():
	op_amount = random.randint(1,3)
	op = []
	num = 0
	swap = 0
	danger = 0
	time = 0
	que = get_num()
	last_question = []
	question = [change_Fraction(que)]
	for i in range(op_amount):
		op.append(random.choice(op_standrad))
	
	for op_sign in op:
		time += 1
		if time == 1:
			last_question = question
		else:
			last_question = [change_Fraction(que)]

		if op_sign == '+':
			num = get_num()
			que += num
			danger += 1
		
		if op_sign == '-':
			num = get_num()
			danger += 4
			if que > num : 
				que -= num
			elif que < num :
				swap = 1
				if danger >= 5:
					question = ['('] + question + [')']
					danger = 1
				que = num - que
			else:
				while 1:
					num = get_num()
					if que>= num:
						que = que - num
						break

		if op_sign == '×':
			num = get_num()
			que *= num
		
		if op_sign == '÷':
			num = 0
			while num == 0 : 
				num = get_num()
				if num != 0:
					break
			if time == 1 :
				que = Fraction(num,que)
			else:
				que = que/num

		num = change_Fraction(num)

		if op_sign == '×' or op_sign == '÷':
			if danger >= 1:
				question = ['('] + question + [')']
				last_question = ['('] + last_question + [')']
				danger = 0

		if swap == 1 :
			question = [num] + [op_sign] + question
			last_question = [num] + [op_sign] + last_question
			swap = 0
		else:
			question = question + [op_sign] + [num]
			last_question = last_question + [op_sign] + [num]
		print (question)
	question = ' '.join('%s' %id for id in question)
	last_quesetion = ' '.join('%s' %id for id in last_question)
	print ("the whole expression is:",question)
	print ("the last step is:",last_question)

def get_num():
	weight = random.randint(1,10)
	
	if weight >= 4:
		return random.randint(0,9)
		
	if weight <= 2:
		down_num = random.randint(2,min(9,9))
		up_num = random.randint(1,down_num - 1)
		return Fraction(up_num,down_num)
		
	else:
		down_num = random.randint(2,min(9,9))
		up_num = random.randint(down_num,9*down_num-1)
		return Fraction(up_num,down_num)

def change_Fraction(num):
	if isinstance(num,int):
		return (str(num))
	x = num.numerator
	y = num.denominator
	z = int(num)
	if y == 1 or z == 0:
		return (str(num))
	else:
		num -= z
		return (str(z)+"’"+str(num))

if __name__ == "__main__":
	mdfk()
