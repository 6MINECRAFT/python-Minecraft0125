from mcpi.minecraft import Minecraft
DD=Minecraft.create()

DD.postToChat("I am watching you")

while True:
    x,y,z=DD.player.getTilePos()
    DD.postToChat("x"+str(x)+"y"+str(y)+"z"+str(z))