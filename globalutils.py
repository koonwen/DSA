import time

def timer(func):
	"""timer decorator to apply to functions"""
	def wrapper(*args, **kwargs):
		start = time.perf_counter()
		result = func(*args, **kwargs)
		end = time.perf_counter()
		print(f"[{func.__name__}] takes {end - start:.2f} seconds")
		return result
	return wrapper


@timer
def sleep(sec):
	"""Test function"""
	time.sleep(sec)


if __name__ == "__main__":
	sleep(2)
