import hashlib

target_hash = "f5cdd96dd845b86e36efe3c3791faeee"
lyrics = """
I'm sitting here in the boring room
It's just another rainy Sunday afternoon
I'm wasting my time, I got nothing to do
I'm hanging around, I'm waiting for you
But nothing ever happens and I wonder

I'm driving around in my car
I'm driving too fast, I'm driving too far
I'd like to change my point of view
I feel so lonely, I'm waiting for you
But nothing ever happens and I wonder

I wonder how, I wonder why
Yesterday you told me 'bout the blue blue sky
And all that I can see is just a yellow lemon tree
I'm turning my head up and down
I'm turning, turning, turning, turing, turning around
And all that I can see is just another lemon tree

Sing
Da Da-la-da-la-de-la-da
Da-la-la-la-de-la-da
Da-de-le-la

I'm sitting here, I miss the power
I'd like to go out, taking a shower
But there is a heavy cloud inside my head
I feel so tired, put myself into bed
Where nothing ever happens and I wonder

Isolation is not good for me
Isolation I don't want to sit on the lemon tree
I'm stepping around in a desert of joy
Baby, anyhow I'll get another toy
And everything will happen and you wonder

I wonder how, I wonder why
Yesterday you told me 'bout the blue blue sky
And all that I can see is just another lemon tree
I'm turning my head up and down
I'm turning turning turning turning turning around
And all that I can see is just a yellow lemon tree
And I wonder, wonder

I wonder how, I wonder why
Yesterday you told me 'bout the blue blue sky
And all that I can see, and all that I can see, and all that I can see
Is just a yellow lemon tree
"""
phrases = [line.strip() for line in lyrics.split('\n') if line.strip()]
words = set(word.strip() for line in phrases for word in line.split())  # Use a set for unique words

password_candidates = phrases + list(words)

for password in password_candidates:
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    
    if hashed_password == target_hash:
        print(f"Password found: {password}")
        break
else:
    print("No matching password found.")
