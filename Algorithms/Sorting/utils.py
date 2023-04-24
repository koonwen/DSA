from random import randint

def list_generator(size = 10):
	return [randint(0,size) for x in range(size)]

if __name__ == "__main__":
	result = list_generator()
	print(result)