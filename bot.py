import tweepy
import random
import time

auth = tweepy.OAuthHandler(#, #)
auth.set_access_token(#, #)

api = tweepy.API(auth)



fun_facts = ["McDonald’s once made bubblegum-flavored broccoli",
             "Some fungi create zombies, then control their minds",
             "The first oranges weren’t orange",
             "There’s only one letter that doesn’t appear in any U.S. state name",
             "A cow-bison hybrid is called a “beefalo”",
             "Johnny Appleseed’s fruits weren’t for eating",
             "Scotland has 421 words for “snow”",
             "Samsung tests phone durability with a butt-shaped robot",
             "The “Windy City” name has nothing to do with Chicago weather",
             "Peanuts aren’t technically nuts",
             "Armadillo shells are bulletproof",
             "Firefighters use wetting agents to make water wetter",
             "The longest English word is 189,819 letters long",
             "Octopuses lay 56,000 eggs at a time",
             "Cats have fewer toes on their back paws",
             "Kleenex tissues were originally intended for gas masks",
             "Blue whales eat half a million calories in one mouthful",
             "That tiny pocket in jeans was designed to store pocket watches",
             "Turkeys can blush",
             "Most Disney characters wear gloves to keep animation simple",
             "The man with the world’s deepest voice can make sounds humans can’t hear",
             "Bats are the only mammal that can actually fly",
             "The wedding of Princess Diana and Prince Charles was watched by 750 million people worldwide in 1981",
             "It’s impossible to hum while holding your nose",
             "Hawaiian pizza was created in Ontario, Canada, by Greek immigrant Sam Panopoulos in 1962",
             "The first footprints on the moon will remain there for a million years",
             "Buckingham Palace in London, England, has 775 rooms, including 78 bathrooms",
             "Michelin stars are highly coveted by elite and upscale restaurants the world over—but they’re actually given out by the Michelin tire company",
             "Sweden has 267,570 islands, the most of any country in the world",
             "If you sneeze too hard, you could fracture a rib",
             "Like fingerprints, everyone's tongue print is different",
             "An ostrich's eye is bigger than its brain",
             "Some lipsticks contain fish scales",
             "In the course of an average lifetime, while sleeping you might eat around 70 assorted insects and 10 spiders, or more",
             "A shrimp's heart is in its head",
             "A crocodile cannot stick its tongue out",
             "The moon has moonquakes",
             "Humans are the only animals that blush",
             "The feeling of getting lost inside a mall is known as the Gruen transfer",
             "You lose up to 30 percent of your taste buds during flight",
             "The longest wedding veil was the same length as 63.5 football fields",
             "The unicorn is the national animal of Scotland",
             "Dolphins have been trained to be used in wars",
             "Water makes different pouring sounds depending on its temperature",
             "Saturn and Jupiter produce diamond rain",
             "Setenil de Las Bodegas in Spain is a town that is under a huge a rock",
             "Your liver can regrow itself in three weeks due to its regenerative properties",
             "You only have two body parts that never stop growing - ears and noses",
             "No number before 1,000 contains the letter A",
             "Bees can fly higher than Mount Everest",
             "Neil Armstrong’s hair was sold in 2004 for $3,000"]




def readfile(file_name):
    thefile = open(file_name,'r')
    last_seen_id = int(thefile.read().strip())
    thefile.close()
    return last_seen_id

def writefile(file_name,last_seen):
    thefile = open(file_name,'w')
    thefile.write(str(last_seen))
    thefile.close()
    return None

def reply():
    tweets = api.mentions_timeline(readfile('last_seen.txt'), tweet_mode ='extended')
    number = random.randint(0,len(fun_facts))
    for tweet in reversed(tweets):
        if "#funfact" in tweet.full_text.lower():
            print(str(tweet.id) + '-' +tweet.full_text)
            api.update_status(f"@{tweet.user.screen_name} Fact: {fun_facts[number]}!",tweet.id)
            api.create_favorite(tweet.id)
            writefile('last_seen.txt',tweet.id)

while True:
    reply()
    time.sleep(15)



