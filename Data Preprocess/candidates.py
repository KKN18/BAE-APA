import csv
import sys

def spicy(n_l,rec_dic): #매운맛 for 위염
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

def sugar_fat(food_name,n_l, ele_dic, rec_dic):#이름 , sorted lst, eledic, recdic
    if food_name in n_l: #high level
        s_num = 0
        f_num = 0
        for a in rec_dic[food_name].keys():
            s, f = ele_dic[a]
            s_num += float(s)
            f_num += float(f)
        return s_num, f_num
    else:
        s,f = ele_dic[food_name]
        return s,f
    


#food_recipe에서 검색해서 고추, 캡사이신의 함량 총합, 
elements_dic = {}
recipe_dic = {}

filename = "food_elements.csv"  # CSV 파일 이름
r_filename = "food_recipe.csv"

#ele,rec 파일을 읽어와서 dic 구축
n_lst = []
nn_lst = []
nnn_lst = []
with open(r_filename, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
                    for key, value in row.items():
                        
                        if "음식명" in key:
                            n_lst.append(value)
            
                        if "식품명" in key:
                            nn_lst.append(value)
                        if "재료" in key:
                            nnn_lst.append(value)
sorted_lst = sorted(set(n_lst))
for i in sorted_lst:
    D = {}
    for j in range(len(n_lst)):
        
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
                            if value == '-':
                                continue
                            fat = value

                        if "당류" in key.split():
                            if value == '-':
                                continue
                            sugar = value
                        i+=1
                        elements_dic[name] = (sugar,fat) #당류,지방
# print(elements_dic)
#----------------------------------
spicy_dic = spicy(sorted_lst,recipe_dic)
# sugar_fat("고구마맛탕",sorted_lst,elements_dic,recipe_dic)
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
print(dif)
# dif - recipe에 있는데 element에 없는 경우
sys.exit()
import matplotlib.pyplot as plt
import math
data = result

x_values = []
y_values = []

# Convert the data points from strings to floating-point numbers
for point in data:
    try:
        a = abs(float(point[0]))
        b = abs(float(point[1]))

        x_values.append(a)
        y_values.append(b)
    except ValueError:
        print(f"Skipping data point: {point}")

sugar_avg = sum(x_values)/len(x_values)
fat_avg = sum(y_values)/len(y_values)
print("당류 평균 :",sum(x_values)/len(x_values))
print("지방 평균 :",sum(y_values)/len(y_values))
for i in range(len(x_values)):
  x_values[i] = x_values[i]/sugar_avg
  y_values[i] = y_values[i]/fat_avg

# Plot the scatter plot
plt.scatter(x_values, y_values, s=5)

# Add labels and title to the plot
plt.xlabel('당류')
plt.ylabel('지방')
plt.title('Scatter Plot')

# Display the plot
plt.show()