from  django.shortcuts import render
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
import time
def onoff_interface(request):
    return render(request,'x.html',{'msg':''})
def on_off(request):
    pc=PNConfiguration()
    pc.subscribe_key="sub-c-1f509f62-6589-11e9-b976-eed4deb7d812"
    pc.publish_key="pub-c-52c0efa1-892c-4002-8c0b-e202541d8978"
    pc.ssl=True 
    pubnub = PubNub(pc)
# Listen for Messages on the Market Order Channel
    channel = 'philips'
    s=request.GET['btn']
    pubnub.publish().channel(channel).message(s).pn_async(show)
    time.sleep(2)
    return render(request,'x.html',{'msg':''})

def show(msg,stat):
    if(msg and stat):print(msg.timetoken,stat.status_code)
    else:
        print("Error",stat and stat.status_code)
        
