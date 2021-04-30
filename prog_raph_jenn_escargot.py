from random import * #on importe le module random
t=0                                                             
j=0                                                            
trajet=[j] #le premier terme de la liste trajet est la variable j                                                     
j=randint(1,3) #j prend la valeur d'un entier aléatoire entre 1 et 3 (inclus)                                                 
while j!=0 and t<24: #tantque j est différent de 0 et t inférieur à 24 on fait tourner le programme                                           
    j=randint(0,3) #j prend la valeur d'un entier aléatoire entre 0 et 3 (inclus)
    while j==trajet[-1]: #tantque j est égal au dernier terme de la liste faire :                                           
        j=randint(0,3) #j prend la valeur d'un entier aléatoire entre 0 et 3 (inclus)                                           
    trajet.append(j)#ajouter j à la liste trajet (seulement si celui-ci n'est pas égal au terme juste avant)                                            
    t+=1 #ajouter 1 à t                                                                                                                                                                         
    print("trajet parcouru :",trajet)
    if j==0 :                                                      
        print("l'escragot reviens en A en 24h, il a mis :",t,"heures")
    if t==24:
        print("l'escargot ne reviens pas en 24h")
                                                                     

    
