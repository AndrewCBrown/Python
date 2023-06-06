#Vertical calculation based on time in air
#Note that acceleration due to gravity in Olathe, KS is 32.15065617 feet/sec/sec
#For the purpose of this program we will use 32.15

time=float(input("Please input the time you spent in the air in seconds to the most decimal places you are sure of."))


    #If block for frames of air and fps of video
if (time==0):
    frames=float(input("Enter the number of frames you were in the air: "))
    fps=float(input("Enter the frames per second the video had: "))
    time=frames/fps
    print("Then your air time was",time,"seconds, we will use that to calculate your vertical.")


#The goal is to find h(t) at t=time/2
G=32.15
h_0=0

#We know at t=time that v_0=G*t-v_0
#2*v_0=G*time
#v_0=(G*time)/2
v_0=(G*time)/2

#velocity=v_0-(G*t)
#height=h_0+(v_0*t)-(G*t*t)/2
height_ft=h_0+(v_0*(time/2))-(G*(time/2)*(time/2))/2
height_in=height_ft*12

print("Your vertical is",height_in,"inches!")
