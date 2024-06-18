import math as m

vektor_sayisi =int(input("Kaç nokta gireceksiniz?"))

points = []
for i in range(vektor_sayisi):
    x = int(input(f"x{i+1} değerini giriniz: "))
    y = int(input(f"y{i+1} değerini giriniz: "))
    points.append((x,y))


def euclideanDistance(point1, point2):
    d=m.sqrt((point2[0]-point1[0])**2+(point2[1]-point1[1])**2)
    return d 

distances =[]
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

min_distance = min(distances)

print(f"Distances: {distances}")
print(f"Minimum distance: {min_distance:.2f}")