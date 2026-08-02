print("╭━━━═══⋅⊱○⊰⋅═══━━━╮")
print("║        WELCOME        ║")
print("╰━━━═══⋅⊱○⊰⋅═══━━━╯")
print("✦───────✦──────✦")
print("Let me give you my introduction")
print("✿ Name     : Mr Cal ")
print("✿ Version  : 1.4")
print("✿ Founder  : Mr FalconHp")
print("✿ Job      : Basis mathematics function")
print("✿ RAM      : 4KB")
print("✦───────✦──────✦")
#user name 
print("So can I know your name")

print("╭───────────────╮")
name = input("  Enter your name here:")
print("╰───────────────╯")

print("Nice name ",name)
print("So here are some funtions that i can do right now... Heheh Mr Falcon finally give me new update")
#variable intro
print("✦ Calculator            : Enter C to use")
print("✦Even/Odd checker       : Enter EO to use")
print("✦Range checker for E/O  : Enter REO to use")
print("✦Discount checker       : Enter DC to check")
print("✦Pesentage finder       : Enter P to check")
print("✦────────✦────────✦")

Tell = input("So which function you want to use :")
#calculator funtion

if Tell ==("C"):
	print("Ok",name,"Let me tell you how to use it")
	print("Enter the values to 2 number and then select the operation you want to perform")
	print("╭───────────────╮")
	#Number selection
	A = int(input("   Enter 1st number :"))
	B = int(input("   Enter 2nd number :"))
	print("╰───────────────╯")
	print("Now",name,"Can you tell me which opration you want to use")
	print("╭───────────────╮")
	print("☆ use + For Addtion")
	print("☆ use - For Subtraction")
	print("☆ use * For Multipication")
	print("☆ use / For Division")
	print("☆ use // For Floor Division")
	print("☆ use % For Modulus")
	print("☆ use ** For Exponent")
	print("╰───────────────╯")
	#opration seletion
	O = input("which operation you want to use :")
	if O ==("+"):
		print(A,"+",B,"=",A+B)
	elif O ==("-"):
		print(A,"-",B,"=",A-B)
	elif O ==("*"):
		print(A,"×",B,"=",A*B)
	elif O ==("/"):
		if B ==(0):
			print("Sorry but I can not process it my CPU will crash")
		else:
			print(A,"/",B,"=",A/B)
	elif O ==("//"):
		if B ==(0):
			print("Have some Mercy on my 4KB RAM I know I got 2KB more but it dose not mean I will process such things")
		else:
			print(A,"//",B,"=",A//B)
	elif O ==("%"):
		print("The remainder will be: ",A%B)
	elif O ==("**"):
		print(A,"**",B,"=",A**B)
#even odd funtion
if Tell == ("EO"):
		print(name,"Tell me a number and I will tell you if it's Even or Odd")
		print("╭───────────────╮")
		#N is for number
		N = int(input("   Enter the Number:"))
		print("╰───────────────╯")
		if N % 2==(0):
			print("My CPU worked really Hard to Find out ",N,"is ○EVEN○")
		else:
			print("My CPU worked really Hard to Find out",N,"is ◇ODD◇")

#even odd Range funtion
if Tell == ("REO"):
		print("So you want to check a range of number and find out how many are Even and how Many are Odd")
		print("╭───────────────╮")
		#RS is for starting point of Range
		RS = int(input("  Enter Start of Range:"))
		#RE is for End of Range
		RE = int(input("  Enter End of Range:"))
		print("╰───────────────╯")
		#TE is for Tottal Even number
		TE =(0)
		#TO is for Tottal Odd number
		TO =(0)
		while RS < RE:
			RS += (1)
			if RS % 2 ==(0):
				print(RS," ○ is EVEN")
				TE +=(1)
			else:
				print(RS,"◇ is ODD")
				TO +=(1)
		print("╭───────────────╮")
		print("『Tottal Even Number :",TE,"』")
		print("『Tottal Odd Number :",TO,"』")
		print("╰───────────────╯")

#Discount checker
if Tell ==("DC"):
	print("••◇ Let me calulate the final Prise for you just tell me original prise and how much discount you are getting◇••")
	print("╭───────────────╮")
	#OP is for Original price
	OP = int(input("  Enter Price :"))
	#DG is for Discount obtained
	DG = int(input("  Enter Discount:"))
	
	#DC is to calulate discount
	DC = OP -((DG/100)*OP)
	#SM is for saved money
	SM =((DG/100)*OP)
	print("╰───────────────╯")
	
	print("⋆｡˚☁︎━━━○━○━━━☁︎˚｡⋆")
	print(" • Original Price :",OP)
	print(" • Discount  :",DG,"%")
	print(" • Final Price :" ,DC)
	print(" • Saved Money :",SM)
	print("⋆｡˚☁︎━━━○━○━━━☁︎˚｡⋆")
#persentage checker	
if Tell ==("P"):
	print("Ok let's check the persentage together")
	print("╭───────────────╮")
	#SN is for student name 
	SN = input("Enter Student Name:")
	#TM is For Tottal Marks
	TM = int(input("Enter Tottal Marks:"))
	#OM is for obtained Marks
	OM = int(input("Enter Obtain Marks:"))
	print("╰───────────────╯")
	
	print("Here select the Persentage rules so i can store it in My 4KB RAM")
	#GP is for good persentage
	#PP is for passing persentage
	print("⋆｡˚☁︎━━━○━○━━━☁︎˚｡⋆")
	GP =int(input("  Enter good % :"))
	PP =int(input("  Enter passing % :"))
	print("⋆｡˚☁︎━━━○━○━━━☁︎˚｡⋆")
	
	#P is for persentage
	if TM == (0):
		print("I think you made a mistake")
	else:
		P= ((OM/TM)*100)
	print("⋆｡˚☁︎━━━○━○━━━☁︎˚｡⋆")
		
	print("  Studen Name :",SN)
	print("  Tottal Marks :",TM)
	print("  Obtained Marks :",OM)
	if TM == (0):
	  print("persentage: Error")
	else:
		  print("Persentage :",P,"%")
	if P >= (GP):
		print("Status : Execllent Marks")
		print("Give this student a Candy")
	elif P >= (PP):
		print("Status : Passed")
		print("Tell this student to watch less Anime")
	elif P < (PP):
		print("Status : Fail")
		print("Better start study or you will be wipping floors")
	print("⋆｡˚☁︎━━━○━○━━━☁︎˚｡⋆")


print("╭━━━═══⋅⊱○⊰⋅═══━━━╮")
print("Mr Falcon Modife V1.4 new tools will be add soon and I hope i get an other RAM upgrate")
print("╰━━━═══⋅⊱○⊰⋅═══━━━╯")
