from django.shortcuts import render
from .models import Destination      # we make a change 

# Create your views here.
#def index(request):   # for fix domain 
    

   # dest1=Destination()
    #dest1.name="AMMAN"
   # dest1.desc="this photo is for wadi alseer"
  #  dest1.img="destination_1.jpg"
  # dest1.price=800
  #  dest1.offer=False     # the offer will not appear 

   # dest2=Destination()
  #  dest2.name="ABBAD"
  #  dest2.desc="this photo is for addadi land"
  #  dest2.img="destination_2.jpg"
   # dest2.price=700
  #  dest2.offer=True

   # dest3=Destination()
   # dest3.name="IRAQ ALAMEER"
   # dest3.desc="this photo is for our house"
   # dest3.img="destination_3.jpg"
   # dest3.price=900
   # dest3.offer=False///

    


   # dests=[dest1,dest2,dest3]
   # return render(request,'index.htm',{"dests":dests})
def index(request):                               # this for database 
    dests=Destination.objects.all()
    return render(request,'index.htm',{"dests":dests})