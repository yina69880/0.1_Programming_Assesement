import random
many_words = {'addictive', 'ambitious', 'amusing', 'appealing', 'artistic', 'astonishing', 'award-winning', 'awe-inspiring'}
short_list = []

while len(short_list)<5:
    word = random.choice(many_words)

    if word not in short_list:
        short_list.append(word)

print(short_list)