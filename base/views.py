from django.shortcuts import render
from django.http import JsonResponse

import paho.mqtt.client as mqtt
from .models import *
from django.core.serializers import serialize

from sklearn.linear_model import LinearRegression 
import numpy as np
import pandas as pd


ml1_x = np.array([[-50,100,20],[-21,20,10],[0,120,10],[-10,50,20],[-50,80,23],[-20,102,60]])
ml1_y = np.array([0.6,0.5,0.6,0.2,0.8,0.3])
model1 = LinearRegression().fit(ml1_x,ml1_y)
ml2_x = np.array([[-50,100,20],[-21,20,10],[0,120,10],[-10,50,20],[-50,80,23],[-20,102,60]])
ml2_y = np.array([0.6,0.5,0.6,0.2,0.8,0.3])
model2 = LinearRegression().fit(ml2_x,ml2_y)
ml3_x = np.array([[-50,100,20],[-21,20,10],[0,120,10],[-10,50,20],[-50,80,23],[-20,102,60]])
ml3_y = np.array([0.6,0.5,0.6,0.2,0.8,0.3])
model3 = LinearRegression().fit(ml3_x,ml3_y)

def home(req):
    return render(req, "base/index.html")

def api(req):
    ml_data1, ml_data2, ml_data3 = get_ml_data()
    data = {
        "system1_temperature": serialize("json", list(reversed(System1_Temperature.objects.all()))),
        "system1_humidity": serialize("json", list(reversed(System1_Humidity.objects.all()))),
        "system1_occupancy": serialize("json", list(reversed(System1_Occupancy.objects.all()))),
        "system2_ph": serialize("json", list(reversed(System2_Ph.objects.all()))),
        "system2_turbiditas": serialize("json", list(reversed(System2_Turbidity.objects.all()))),
        "system2_konduktivitas": serialize("json", list(reversed(System2_Conductivity.objects.all()))),
        "system3_waterlevel": serialize("json", list(reversed(System3_Water_Level.objects.all()))),
        "system3_pressure": serialize("json", list(reversed(System3_Pressure.objects.all()))),
        "system3_temperature": serialize("json", list(reversed(System3_Temperature.objects.all()))),
        "system1_hvac": ml_data1,
        "system2_chemical_pump": ml_data2,
        "system3_water_valve": ml_data3
    }
    return JsonResponse(data)

def get_ml_data():
    l11 = np.array(list(map(lambda x:x['value'], System1_Temperature.objects.all().values())))
    l12 = np.array(list(map(lambda x:x['value'], System1_Humidity.objects.all().values())))
    l13 = np.array(list(map(lambda x:x['value'], System1_Occupancy.objects.all().values())))
    l21 = np.array(list(map(lambda x:x['value'], System2_Ph.objects.all().values())))
    l22 = np.array(list(map(lambda x:x['value'], System2_Turbidity.objects.all().values())))
    l23 = np.array(list(map(lambda x:x['value'], System2_Conductivity.objects.all().values())))
    l31 = np.array(list(map(lambda x:x['value'], System3_Water_Level.objects.all().values())))
    l32 = np.array(list(map(lambda x:x['value'], System3_Pressure.objects.all().values())))
    l33 = np.array(list(map(lambda x:x['value'], System3_Temperature.objects.all().values())))
    l1_size = min(l11.size, l12.size, l13.size)
    l2_size = min(l21.size, l22.size, l23.size)
    l3_size = min(l31.size, l32.size, l33.size)
    new_l1 = np.vstack((l11[:l1_size],l12[:l1_size],l13[:l1_size])).T
    new_l2 = np.vstack((l21[:l2_size],l22[:l1_size],l23[:l2_size])).T
    new_l3 = np.vstack((l31[:l3_size],l32[:l1_size],l33[:l3_size])).T
    pred1 = model1.predict(new_l1)
    pred2 = model2.predict(new_l2)
    pred3 = model3.predict(new_l3)
    ml_data1 = bool(pred1[0] > 0.5)
    ml_data2 = bool(pred2[0] > 0.5)
    ml_data3 = bool(pred3[0] > 0.5)
    return ml_data1, ml_data2, ml_data3

def on_message_s1temperatur(client, userdata, msg):
    System1_Temperature.objects.create(value=msg.payload.decode("utf-8"))
    if System1_Temperature.objects.count() > 200:
        System1_Temperature.objects.all().first().delete()

def on_message_s1kelembapan(client, userdata, msg):
    System1_Humidity.objects.create(value=msg.payload.decode("utf-8"))
    if System1_Humidity.objects.count() > 200:
        System1_Humidity.objects.all().first().delete()

def on_message_s1okupansi(client, userdata, msg):
    System1_Occupancy.objects.create(value=msg.payload.decode("utf-8"))
    if System1_Occupancy.objects.count() > 200:
        System1_Occupancy.objects.all().first().delete()

def on_message_s2ph(client, userdata, msg):
    System2_Ph.objects.create(value=msg.payload.decode("utf-8"))
    if System2_Ph.objects.count() > 200:
        System2_Ph.objects.all().first().delete()

def on_message_s2turbiditas(client, userdata, msg):
    System2_Turbidity.objects.create(value=msg.payload.decode("utf-8"))
    if System2_Turbidity.objects.count() > 200:
        System2_Turbidity.objects.all().first().delete()

def on_message_s2konduktivitas(client, userdata, msg):
    System2_Conductivity.objects.create(value=msg.payload.decode("utf-8"))
    if System2_Conductivity.objects.count() > 200:
        System2_Conductivity.objects.all().first().delete()

def on_message_s3waterlevel(client, userdata, msg):
    System3_Water_Level.objects.create(value=msg.payload.decode("utf-8"))
    if System3_Water_Level.objects.count() > 200:
        System3_Water_Level.objects.all().first().delete()

def on_message_s3tekanan(client, userdata, msg):
    System3_Pressure.objects.create(value=msg.payload.decode("utf-8"))
    if System3_Pressure.objects.count() > 200:
        System3_Pressure.objects.all().first().delete()

def on_message_s3temperatur(client, userdata, msg):
    System3_Temperature.objects.create(value=msg.payload.decode("utf-8"))
    if System3_Temperature.objects.count() > 200:
        System3_Temperature.objects.all().first().delete()


client = mqtt.Client("danielw12345")
client.message_callback_add("tugas11/sistem1/temperatur", on_message_s1temperatur)
client.message_callback_add("tugas11/sistem1/kelembapan", on_message_s1kelembapan)
client.message_callback_add("tugas11/sistem1/okupansi", on_message_s1okupansi)
client.message_callback_add("tugas11/sistem2/ph", on_message_s2ph)
client.message_callback_add("tugas11/sistem2/turbiditas", on_message_s2turbiditas)
client.message_callback_add("tugas11/sistem2/konduktivitas", on_message_s2konduktivitas)
client.message_callback_add("tugas11/sistem3/waterlevel", on_message_s3waterlevel)
client.message_callback_add("tugas11/sistem3/tekanan", on_message_s3tekanan)
client.message_callback_add("tugas11/sistem3/temperatur", on_message_s3temperatur)

client.connect("localhost", 1883)
client.subscribe("tugas11/#")
client.loop_start()
