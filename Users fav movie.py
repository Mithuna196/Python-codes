# 𝐆𝐞𝐭 𝐭𝐡𝐞 𝐮𝐬𝐞𝐫'𝐬 𝐟𝐚𝐯𝐨𝐫𝐢𝐭𝐞 𝐦𝐨𝐯𝐢𝐞 𝐮𝐬𝐢𝐧𝐠 𝐧𝐞𝐬𝐭𝐢𝐧𝐠 𝐢𝐧 𝐩𝐲𝐭𝐡𝐨𝐧

movie = input("What's your favorite movie? Bhahubali, RRR, or KGF: ")

if movie == "Bhahubali":
    print("Great Choice!")
    actor = input("Who's your favorite actor? Prabhas or Rana: ")
    if actor == "Prabhas":
        print("You are a loyal fan.")
    else:
        print("He slayed in the character in the movie.")

elif movie == "RRR":
    print("Great Choice!")
    actor = input("Who's your favorite actor? Ramcharan or NTR: ")
    if actor == "Ramcharan":
        print("You are a loyal fan.")
    else:
        print("He slayed in the character in the movie.")

elif movie == "KGF":
    print("Great Taste!")
    hero = input("Who's your favorite actor? Yash or Prakash Raj: ")
    if hero == "Yash":
        print("You are a loyal fan.")
    else:
        print("He slayed in the character in the movie.")

else:
    print("You must be an Allu Arjun fan!")
