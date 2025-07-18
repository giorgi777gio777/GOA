# 4) მომხმარებელს შემოატანინე ორი სტრინგი და for loop-ის საშუალებით დაითვალე  ორივეში სიმბოლოების რაოდენობა. შემდეგ დაპრინტეთ არის თუ არა ერთმანეთის ტოლი სიმბოლოების რაოდენობა. 
string = input('შემოიტანე სტრინგი')
string2 = input('შემოიტანე სტრინგი')
romelime_cvladi = 0
romelime = 0
for i in string :
    remelime_cvladi = romelime_cvladi + 1
for i in string2 :
    romelime = romelime + 1
print(romelime_cvladi == romelime)