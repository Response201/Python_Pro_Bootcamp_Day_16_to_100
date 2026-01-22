

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
new_list = sentence.split(" ")
result = {word: len(word) for word  in new_list}
print(result)
