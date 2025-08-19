# 7) მომხმარებელს შემოატანინე პაროლი. და ჰქონდეს სამი ცდა.
pasword = input ('შემოიყვანე პაროლი')
cvlaadi = 0
while pasword != 'cvladi' and cvlaadi != 3 :
  pasword = input ('შემოიყვანე პაროლი')
  cvlaadi += 1
print(cvlaadi)

