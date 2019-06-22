def choice(choices):
	c = 0
	
	for i, choice in enumerate(choices):
		print(f"{i + 1}: {choice}")

	while True:
		try:
			c = int(input())

			if c < 1 or c > len(choices):
				raise ValueError
			
			break
		except ValueError:
			print("Please make a choice between 1 and", len(choices))

	return c - 1