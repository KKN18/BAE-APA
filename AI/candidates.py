#!/usr/bin/env python3

import csv
import sys
import torchvision
import torchvision.models as models
import torch.nn as nn
import torch
from torch import optim
import os
from torchvision.transforms import transforms
from PIL import Image

checkpoint_path = sys.argv[1]
image_path = sys.argv[2]

labels = ['오렌지 주스',
              '우유',
              '샐러드',
              '계란',
              '고구마맛탕',
              '김치',
              '쌀밥',
              '콩나물',
              '치킨',
              '비빔밥',
              '돈가스']

def load_model(checkpoint_path, labels):
    num_classes = len(labels)
    model = models.resnet50()
    num_features = model.fc.in_features
    model.fc = nn.Linear(num_features, 101)
    classifier = nn.Linear(model.fc.out_features, num_classes)
    model = nn.Sequential(model,
                          classifier)
    checkpoint = torch.load(checkpoint_path, map_location='cpu')
    model.load_state_dict(checkpoint['model_state_dict'])
    model.eval()
    
    return model
def predict_food(model, image_path, labels):    
    image = Image.open(image_path).convert('RGB')
    num_classes = len(labels)
    transform = transforms.Compose([transforms.Resize(224),
                                    transforms.ToTensor(),
                                    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                        std=[0.229, 0.224, 0.225])])
    image = transform(image)

    # Make a prediction with the model
    with torch.no_grad():
        output = model(image.unsqueeze(0))

    # Extract the predicted label
    _, predicted_idx = torch.max(output, 1)
    predicted_label = predicted_idx.item()
    predicted = labels[predicted_label]

    return predicted

def make_plt():
    import matplotlib.pyplot as plt
    import math
    # data = result
    x_values = []
    y_values = []
    for a in sorted_lst:
        x,y = sugar_fat(a,sorted_lst,elements_dic,recipe_dic,dif_D)
        x_values.append(x)
        y_values.append(y)
        

    # Convert the data points from strings to floating-point numbers
    # for point in data:
    #     try:
    #         a = abs(float(point[0]))
    #         b = abs(float(point[1]))

    #         x_values.append(a)
    #         y_values.append(b)
    #     except ValueError:
    #         print(f"Skipping data point: {point}")

    # sugar_avg = sum(x_values)/len(x_values)
    # fat_avg = sum(y_values)/len(y_values)
    # print("당류 평균 :",sum(x_values)/len(x_values))
    # print("지방 평균 :",sum(y_values)/len(y_values))
    # for i in range(len(x_values)):
    #   x_values[i] = x_values[i]/sugar_avg
    #   y_values[i] = y_values[i]/fat_avg

    # Plot the scatter plot
    plt.scatter(x_values, y_values, s=5)

    # Add labels and title to the plot
    plt.xlabel('sugar')
    plt.ylabel('fat')
    plt.title('sugar,fat ratio')

    # Display the plot
    # plt.show()
    plt.savefig("plt.jpg")

def spicy(n_l,rec_dic):






        spicy_dic = {}
        temp = 0
        for a in n_l:#key
            for b in rec_dic[a].keys():
                if "청양고추" in b:
                    temp += float(rec_dic[a][b])*1.5

                elif "고추" in b:
                    temp += float(rec_dic[a][b])
                    
                elif "마늘" in b:
                    temp += float(rec_dic[a][b])*0.3
            spicy_dic[a] = temp
            temp = 0
        
        return spicy_dic

def chronic(n_l,rec_dic): #매운맛 for 위염
    chronic_red_lst = []
    chronic_yellow_lst = []
    
    for a in n_l:#key
        for b in rec_dic[a].keys():
            if "밀가루" in b or "청양고추" in b:
                chronic_red_lst.append(a)
            elif "고추" in b  or "양파" in b  or "마늘" in b or "양배추" in b:
                chronic_yellow_lst.append(a)
    crl = set(chronic_red_lst)
    cyl = set(chronic_yellow_lst)
    return crl, cyl
            
        
    
    return spicy_dic

def sugar_fat(food_name,n_l, ele_dic, rec_dic, dif_dic):#이름 , sorted lst, eledic, recdic
    if food_name in n_l: #high level
        s_num = 0
        f_num = 0
        for a in rec_dic[food_name].keys():
            weight = float(rec_dic[food_name][a])
            if a in ele_dic.keys():
                s, f = ele_dic[a]
                s_num += float(s)*weight
                f_num += float(f)*weight
            else:#이름 match X, 전처리 필요
                s, f = dif_dic[a]
                s_num += float(s)*weight
                f_num += float(f)*weight

        return s_num/weight_dic[food_name], f_num/weight_dic[food_name]
    else:
        s,f = ele_dic[food_name]
        return s/weight_dic[food_name],f/weight_dic[food_name]
    


#food_recipe에서 검색해서 고추, 캡사이신의 함량 총합, 
elements_dic = {}
recipe_dic = {}

filename = "food_elements.csv"  # CSV 파일 이름
r_filename = "food_recipe.csv"

#ele,rec 파일을 읽어와서 dic 구축
n_lst = []
nn_lst = []
nnn_lst = []
nnnn_lst = []
with open(r_filename, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
                    for key, value in row.items():
                        
                        if "음식명" in key:
                            n_lst.append(value)
                        if "음식총" in key:
                            nnnn_lst.append(value)
                        if "식품명" in key:
                            nn_lst.append(value)
                        if "재료" in key:
                            nnn_lst.append(value)
sorted_lst = sorted(set(n_lst))
weight_dic = {}
for i in sorted_lst:
    D = {}
    for j in range(len(n_lst)):
        weight_dic[n_lst[j]] = float(nnnn_lst[j])
        if i==n_lst[j]:
            D[nn_lst[j]] = nnn_lst[j]
    recipe_dic[i] = D



i = 0
sugar = 0
fat = 0
name = ''


#element_dic 구축
with open(filename, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

                    for key, value in row.items():
                        
                        if "식품명" in key:
                            
                            name = value
            
                        if "지방" in key.split():
                            if value == '-' or value == 'Tr':
                                continue
                            fat = float(value)

                        if "당류" in key.split():
                            if value == '-' or value == 'Tr':
                                continue
                            sugar = float(value)
                        i+=1
                        elements_dic[name] = (sugar,fat) #당류,지방
# print(elements_dic)
#-----------------------------------------------
chronic_red_lst, chronic_yellow_lst = chronic(sorted_lst,recipe_dic)
chronic_red_lst=chronic_red_lst.union(["밀가루", "청양고추"])
chronic_yellow_lst=chronic_yellow_lst.union(["고추", "양파", "마늘", "양배추"])
spicy_dic = spicy(sorted_lst,recipe_dic)
k=0
L = elements_dic.keys()

LL = []
for a in sorted_lst:
    LL.extend(recipe_dic[a].keys())

LL = set(LL)
dif = []
for a in LL:
    if a not in L:
        dif.append(a)
dif_D = {}
for a in dif:
    dif_D[a] = (0.0,0.0)
for a in dif:
    for b in a.split(","):
        for c in elements_dic.keys():
            if b in c.split(",")[0]:
                s,f = elements_dic[c]
                dif_D[a] = (dif_D[a][0]+s, dif_D[a][1]+f)

# dif - recipe에 있는데 element에 없는 경우
# sys.exit()

model = load_model(checkpoint_path,labels)
food_name = predict_food(model,image_path,labels)

s,v = sugar_fat(food_name,sorted_lst,elements_dic,recipe_dic,dif_D)
sv = ""
chrr = ""
spi = ""

for a in chronic_yellow_lst:
    if food_name in a:
        chrr = "2"
for a in chronic_red_lst:
    if food_name in a:
        chrr = "3"
for a in spicy_dic.keys():
    if food_name in a:
        if spicy_dic[a] > 20:
            spi = "3"
        elif spicy_dic[a] > 10:
            spi = "2"
        else:
            spi = "1"
if v>20:
    spi = "2"
if v>30:
    spi = "2"


if s>30 or v>30:
    sv = "3"
elif s>15 or v>15:
    sv = "2"
else:
    sv = "1"
print(sv+chrr+spi,"위험, 위험, 주의")
print(food_name)
# if v > 20:
#     print("332")
# else:
#     print("123")
