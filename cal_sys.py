import random
from fractions import Fraction

op_standrad = ['+','-','×','÷']

def mdfk():
	op_amount = random.randint(1,3)
	op = []
	num = 0
	swap = 0
	danger = 0
	que = get_num()
	question = [que]
	for i in range(op_amount):
		op.append(random.choice(op_standrad))
	
	for op_sign in op:
		if op_sign == '+':
			que += get_num()
			danger += 1
		
		if op_sign == '-':
			num = get_num()
			if que > num : 
				que -= num
			elif que < num :
				swap = 1
				que = num - que
			else:
				while 1:
					num = get_num()
					if que>= num:
						que = que - num
						break
			danger += 1

		if op_sign == '×':
			que *= get_num()
		
		if op_sign == '÷':
			#if num == 0 : num = get_num()
			#if num > que : que =
			print("mismatch")
			break
		
		if op_sign == '×' or op_sign == '÷':
			if danger >= 1:
				question = ['('] + question + [')']

		if swap == 1 :
			question = [num] + [op_sign] + question
			swap = 0
		else:
			question = question + [op_sign] + [num]
	question = ' '.join('%s' %id for id in question)
	print (question)

def get_num():
	i = 0
	i = random.randint(0,9)
	return i

if __name__ == "__main__":
	mdfk()
def get_num():
	i = 0
	i = random.randint(0,9)
	return i

if __name__ == "__main__":
	mdfk()
