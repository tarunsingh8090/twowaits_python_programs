runplayer1=int(input("enter the runs scored by player 1 in 60 balls:"))
runplayer2=int(input("enter the runs scored by player 2 in 60 balls:"))
runplayer3=int(input("enter the runs scored by player 3 in 60 balls:"))
strikerate1=runplayer1*100/60
strikerate2=runplayer2*100/60
strikerate3=runplayer3*100/60
print("strike rate of player 1 is:",strikerate1)
print("strike rate of player 2 is:",strikerate2)
print("strike rate of player 3 is:",strikerate3)
print("run scored by player 1 if he played 60 balls more:",runplayer1*2)
print("run scored by player 2 if he played 60 balls more:",runplayer2*2)
print("run scored by player 3 if he played 60 balls more:",runplayer3*2)
print("maximum number of sixes player 1 could hit:",runplayer1//6)
print("maximum number of sixes player 2 could hit:",runplayer2//6)
print("maximum number of sixes player 3 could hit:",runplayer3//6)
