import requests


if __name__ == "__main__":
	r = requests.get('http://upe.42069.fun/7fznC')
	data = r.json()
	state = data['state']
	status = data['status']
	remaining_guesses = data['remaining_guesses']
	
	alreadyusedarray = []

	lettertype = 1 #1 if vowel was used last, 0 if consonant was


	vowels = "eiaou"
	consonants = "thnsrygbmldcufpwvkxjqz"
	init_guesses = remaining_guesses
	usedmarker = 0

	r = requests.post('http://upe.42069.fun/7fznC', data = {'guess' : vowels[0]})
	data = r.json()
	state = data['state']
	status = data['status']
	remaining_guesses = data['remaining_guesses']
	count = data['games']
	print("STATE: " + state)

	r = requests.post('http://upe.42069.fun/7fznC', data = {'guess' : vowels[1]})
	data = r.json()
	state = data['state']
	status = data['status']
	remaining_guesses = data['remaining_guesses']
	count = data['games']
	print("STATE: " + state)
	prevstate = state
	r = requests.post('http://upe.42069.fun/7fznC', data = {'guess' : vowels[2]})
	data = r.json()
	state = data['state']
	status = data['status']
	remaining_guesses = data['remaining_guesses']
	count = data['games']
	print("STATE: " + state)
	
	alreadyusedarray.append(vowels[0])
	alreadyusedarray.append(vowels[1])
	alreadyusedarray.append(vowels[2])
	
	vowelsused = 0

	
	while count < 4000:
		while status == "ALIVE":

			if state == prevstate:
				print("SAMESTATE")

				if lettertype == 0:
					lettertype = 1

					for i in range(0, len(vowels)):
						for j in range(0, len(alreadyusedarray)):
							if vowels[i] == alreadyusedarray[j]:
								usedmarker = 1
							
						
						if usedmarker  == 1:
							usedmarker = 0
						else:
							lettertosend = vowels[i]
							alreadyusedarray.append(lettertosend)
							break

						#if i == len(vowels) - 1:
							#vowelsused = 1

				else:
					lettertype = 0

					for i in range(0, len(consonants)):
						for j in range(0, len(alreadyusedarray)):
							if consonants[i] == alreadyusedarray[j]:
								usedmarker = 1
							
						
						if usedmarker  == 1:
							usedmarker = 0
						
						else:
							lettertosend = consonants[i]
							alreadyusedarray.append(lettertosend)
							break

				"""if vowelsused == 1:
					lettertype = 0

					for i in range(0, len(consonants)):
						for j in range(0, len(alreadyusedarray)):
							if consonants[i] == alreadyusedarray[j]:
								usedmarker = 1
							
						
						if usedmarker  == 1:
							usedmarker = 0
						
						else:
							lettertosend = consonants[i]
							alreadyusedarray.append(lettertosend)
							break"""
						
					
				
			
			else:
				if lettertype == 0:

					for i in range(0, len(consonants)):
						for j in range(0, len(alreadyusedarray)):
							if consonants[i] == alreadyusedarray[j]:
								usedmarker = 1
							
						
						if usedmarker  == 1:
							usedmarker = 0
						
						else:
							lettertosend = consonants[i]
							alreadyusedarray.append(lettertosend)
							break
						
					
				
				else:

					for i in range(0, len(vowels)):
						for j in range(0, len(alreadyusedarray)):
							if vowels[i] == alreadyusedarray[j]:
								usedmarker = 1
							
						
						if usedmarker  == 1:
							usedmarker = 0
						
						else:
							lettertosend = vowels[i]
							alreadyusedarray.append(lettertosend)
							break

						#if i == len(vowels) - 1:
						#	vowelsused = 1

				"""if vowelsused == 1:

					lettertype = 0

					for i in range(0, len(consonants)):
						for j in range(0, len(alreadyusedarray)):
							if consonants[i] == alreadyusedarray[j]:
								usedmarker = 1
							
						
						if usedmarker  == 1:
							usedmarker = 0
						
						else:
							lettertosend = consonants[i]
							alreadyusedarray.append(lettertosend)
							break						
					"""
				
			
			prevstate = state
			r = requests.post('http://upe.42069.fun/7fznC', data = {'guess' : lettertosend})
			data = r.json()
			state = data['state']
			status = data['status']
			remaining_guesses = data['remaining_guesses']
			count = data['games']
			print("STATE: " + state)
			print("STATUS: " + status)
			
		
		r = requests.get('http://upe.42069.fun/7fznC')
		data = r.json()
		state = data['state']
		status = data['status']
		remaining_guesses = data['remaining_guesses']
		print("STATE: " + state)
		alreadyusedarray = []
		lettertype = 1
		prevstate = ""
		vowelsused = 0
	