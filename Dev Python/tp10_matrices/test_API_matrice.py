""" tests pour les API matrices 
    Remarques : tous les tests de ce fichier doivent passer quelle que soit l'API utilisée
    """
import API_matrice2 as API


def matrice1():
    m1 = API.construire_matrice(3, 4, None)
    API.set_val(m1, 0, 0, 10)
    API.set_val(m1, 0, 1, 11)    
    API.set_val(m1, 0, 2, 12)
    API.set_val(m1, 0, 3, 13)
    API.set_val(m1, 1, 0, 14)
    API.set_val(m1, 1, 1, 15)
    API.set_val(m1, 1, 2, 16)
    API.set_val(m1, 1, 3, 17)
    API.set_val(m1, 2, 0, 18)
    API.set_val(m1, 2, 1, 19)
    API.set_val(m1, 2, 2, 20)
    API.set_val(m1, 2, 3, 21)
    return m1

def matrice1b():
    m1b = API.construire_matrice(4, 4, None)
    API.set_val(m1b, 0, 0, 10)
    API.set_val(m1b, 0, 1, 11)    
    API.set_val(m1b, 0, 2, 12)
    API.set_val(m1b, 0, 3, 13)
    API.set_val(m1b, 1, 0, 14)
    API.set_val(m1b, 1, 1, 15)
    API.set_val(m1b, 1, 2, 16)
    API.set_val(m1b, 1, 3, 17)
    API.set_val(m1b, 2, 0, 18)
    API.set_val(m1b, 2, 1, 19)
    API.set_val(m1b, 2, 2, 20)
    API.set_val(m1b, 2, 3, 21)
    API.set_val(m1b, 3, 0, 22)
    API.set_val(m1b, 3, 1, 23)
    API.set_val(m1b, 3, 2, 24)
    API.set_val(m1b, 3, 3, 25)
    return m1b

def tra_m1():
    tram1 = API.construire_matrice(4, 3, None)
    API.set_val(tram1, 0, 0, 10)
    API.set_val(tram1, 1, 0, 11)    
    API.set_val(tram1, 2, 0, 12)
    API.set_val(tram1, 3, 0, 13)
    API.set_val(tram1, 0, 1, 14)
    API.set_val(tram1, 1, 1, 15)
    API.set_val(tram1, 2, 1, 16)
    API.set_val(tram1, 3, 1, 17)
    API.set_val(tram1, 0, 2, 18)
    API.set_val(tram1, 1, 2, 19)
    API.set_val(tram1, 2, 2, 20)
    API.set_val(tram1, 3, 2, 21)
    return tram1

def tri_m1():
    trim1 = API.construire_matrice(4, 4, None)
    API.set_val(trim1, 0, 0, 10)
    API.set_val(trim1, 0, 1, 0)    
    API.set_val(trim1, 0, 2, 0)
    API.set_val(trim1, 0, 3, 0)
    API.set_val(trim1, 1, 0, 14)
    API.set_val(trim1, 1, 1, 15)
    API.set_val(trim1, 1, 2, 0)
    API.set_val(trim1, 1, 3, 0)
    API.set_val(trim1, 2, 0, 18)
    API.set_val(trim1, 2, 1, 19)
    API.set_val(trim1, 2, 2, 20)
    API.set_val(trim1, 2, 3, 0)
    API.set_val(trim1, 3, 0, 22)
    API.set_val(trim1, 3, 1, 23)
    API.set_val(trim1, 3, 2, 24)
    API.set_val(trim1, 3, 3, 25)
    return trim1

def tris_m1():
    trism1 = API.construire_matrice(4, 4, None)
    API.set_val(trism1, 0, 0, 10)
    API.set_val(trism1, 0, 1, 11)    
    API.set_val(trism1, 0, 2, 12)
    API.set_val(trism1, 0, 3, 13)
    API.set_val(trism1, 1, 0, 0)
    API.set_val(trism1, 1, 1, 15)
    API.set_val(trism1, 1, 2, 16)
    API.set_val(trism1, 1, 3, 17)
    API.set_val(trism1, 2, 0, 0)
    API.set_val(trism1, 2, 1, 0)
    API.set_val(trism1, 2, 2, 20)
    API.set_val(trism1, 2, 3, 21)
    API.set_val(trism1, 3, 0, 0)
    API.set_val(trism1, 3, 1, 0)
    API.set_val(trism1, 3, 2, 0)
    API.set_val(trism1, 3, 3, 25)
    return trism1

def bloc_m1():
    bm1 = API.construire_matrice(2, 2, None)
    API.set_val(bm1, 0, 0, 15)
    API.set_val(bm1, 0, 1, 16)
    API.set_val(bm1, 1, 0, 19)
    API.set_val(bm1, 1, 1, 20)
    return bm1

def matrice2():
    m2 = API.construire_matrice(2, 3, None)
    API.set_val(m2, 0, 0, 'A')
    API.set_val(m2, 0, 1, 'B')    
    API.set_val(m2, 0, 2, 'C')
    API.set_val(m2, 1, 0, 'D')
    API.set_val(m2, 1, 1, 'E')
    API.set_val(m2, 1, 2, 'F')
    return m2

def matrice2b():
    m2b = API.construire_matrice(3, 3, None)
    API.set_val(m2b, 0, 0, 'A')
    API.set_val(m2b, 0, 1, 'B')    
    API.set_val(m2b, 0, 2, 'C')
    API.set_val(m2b, 1, 0, 'D')
    API.set_val(m2b, 1, 1, 'E')
    API.set_val(m2b, 1, 2, 'F')
    API.set_val(m2b, 2, 0, 'G')
    API.set_val(m2b, 2, 1, 'H')
    API.set_val(m2b, 2, 2, 'I')
    return m2b

def tra_m2():
    tram2 = API.construire_matrice(3, 2, None)
    API.set_val(tram2, 0, 0, 'A')
    API.set_val(tram2, 0, 1, 'D')    
    API.set_val(tram2, 1, 0, 'B')
    API.set_val(tram2, 1, 1, 'E')
    API.set_val(tram2, 2, 0, 'C')
    API.set_val(tram2, 2, 1, 'F')
    return tram2

def tri_m2():
    trim2 = API.construire_matrice(3, 3, None)
    API.set_val(trim2, 0, 0, 'A')
    API.set_val(trim2, 0, 1, 0)    
    API.set_val(trim2, 0, 2, 0)
    API.set_val(trim2, 1, 0, 'D')
    API.set_val(trim2, 1, 1, 'E')
    API.set_val(trim2, 1, 2, 0)
    API.set_val(trim2, 2, 0, 'G')
    API.set_val(trim2, 2, 1, 'H')
    API.set_val(trim2, 2, 2, 'I')
    return trim2

def tris_m2():
    tris2 = API.construire_matrice(3, 3, None)
    API.set_val(tris2, 0, 0, 'A')
    API.set_val(tris2, 0, 1, 'B')    
    API.set_val(tris2, 0, 2, 'C')
    API.set_val(tris2, 1, 0, 0)
    API.set_val(tris2, 1, 1, 'E')
    API.set_val(tris2, 1, 2, 'F')
    API.set_val(tris2, 2, 0, 0)
    API.set_val(tris2, 2, 1, 0)
    API.set_val(tris2, 2, 2, 'I')
    return tris2

def bloc_m2():
    bm2 = API.construire_matrice(1, 3, None)
    API.set_val(bm2, 0, 0, 'A')
    API.set_val(bm2, 0, 1, 'B')    
    API.set_val(bm2, 0, 2, 'C')
    return bm2

def matrice3():
    m3 = API.construire_matrice(3, 3, None)
    API.set_val(m3, 0, 0, 2)
    API.set_val(m3, 0, 1, 7)    
    API.set_val(m3, 0, 2, 6)
    API.set_val(m3, 1, 0, 9)
    API.set_val(m3, 1, 1, 5)
    API.set_val(m3, 1, 2, 1)
    API.set_val(m3, 2, 0, 4)
    API.set_val(m3, 2, 1, 3)
    API.set_val(m3, 2, 2, 8)
    return m3

def tra_m3():
    tram3 = API.construire_matrice(3, 3, None)
    API.set_val(tram3, 0, 0, 2)
    API.set_val(tram3, 1, 0, 7)    
    API.set_val(tram3, 2, 0, 6)
    API.set_val(tram3, 0, 1, 9)
    API.set_val(tram3, 1, 1, 5)
    API.set_val(tram3, 2, 1, 1)
    API.set_val(tram3, 0, 2, 4)
    API.set_val(tram3, 1, 2, 3)
    API.set_val(tram3, 2, 2, 8)
    return tram3

def tri_m3():
    trim3 = API.construire_matrice(3, 3, None)
    API.set_val(trim3, 0, 0, 2)
    API.set_val(trim3, 0, 1, 0)    
    API.set_val(trim3, 0, 2, 0)
    API.set_val(trim3, 1, 0, 9)
    API.set_val(trim3, 1, 1, 5)
    API.set_val(trim3, 1, 2, 0)
    API.set_val(trim3, 2, 0, 4)
    API.set_val(trim3, 2, 1, 3)
    API.set_val(trim3, 2, 2, 8)
    return trim3

def tris_m3():
    tris3 = API.construire_matrice(3, 3, None)
    API.set_val(tris3, 0, 0, 2)
    API.set_val(tris3, 0, 1, 7)    
    API.set_val(tris3, 0, 2, 6)
    API.set_val(tris3, 1, 0, 0)
    API.set_val(tris3, 1, 1, 5)
    API.set_val(tris3, 1, 2, 1)
    API.set_val(tris3, 2, 0, 0)
    API.set_val(tris3, 2, 1, 0)
    API.set_val(tris3, 2, 2, 8)
    return tris3

def bloc_m3():
    bm3 = API.construire_matrice(2, 3, None)
    API.set_val(bm3, 0, 0, 9)
    API.set_val(bm3, 0, 1, 5)
    API.set_val(bm3, 0, 2, 1)
    API.set_val(bm3, 1, 0, 4)
    API.set_val(bm3, 1, 1, 3)
    API.set_val(bm3, 1, 2, 8)
    return bm3

def test_get_nb_lignes():
    m1 = matrice1()
    m2 = matrice2()
    m3 = matrice3()
    assert API.get_nb_lignes(m1) == 3
    assert API.get_nb_lignes(m2) == 2
    assert API.get_nb_lignes(m3) == 3
        
def test_get_nb_colonnes():
    m1 = matrice1()
    m2 = matrice2()
    m3 = matrice3()
    assert API.get_nb_colonnes(m1) == 4
    assert API.get_nb_colonnes(m2) == 3
    assert API.get_nb_colonnes(m3) == 3

def test_get_val():
    m1 = matrice1()
    m2 = matrice2()
    m3 = matrice3()
    assert API.get_val(m1, 0, 1) == 11
    assert API.get_val(m1, 2, 1) == 19
    assert API.get_val(m2, 1, 1) == 'E'
    assert API.get_val(m2, 0, 2) == 'C'
    assert API.get_val(m3, 2, 0) == 4
    assert API.get_val(m3, 1, 0) == 9

def test_sauve_charge_matrice():
    matrice = matrice2()
    API.sauve_matrice(matrice, "matrice.csv")
    matrice_bis = API.charge_matrice_str("matrice.csv")
    assert matrice == matrice_bis

def test_get_ligne():
    m1 = matrice1()
    m2 = matrice2()
    m3 = matrice3()
    assert API.get_ligne(m1,0) == [10, 11, 12, 13]
    assert API.get_ligne(m2,0) == ['A', 'B', 'C']
    assert API.get_ligne(m3,0) == [2, 7, 6]

def test_get_colonne():
    m1 = matrice1()
    m2 = matrice2()
    m3 = matrice3()
    assert API.get_colonne(m1,1) == [11, 15, 19]
    assert API.get_colonne(m2,2) == ['C', 'F']
    assert API.get_colonne(m3,0) == [2, 9, 4]

def test_diago_princ():
    m1 = matrice1b()#on prend les matrice carees 1 et 2
    m2 = matrice2b()
    m3 = matrice3()
    assert API.get_diagonale_principale(m1) == [10, 15, 20, 25]
    assert API.get_diagonale_principale(m2) == ['A', 'E', 'I']
    assert API.get_diagonale_principale(m3) == [2, 5, 8]

def test_diago_sec():
    m1 = matrice1b()#on prend les matrice carees 1 et 2
    m2 = matrice2b()
    m3 = matrice3()
    assert API.get_diagonale_secondaire(m1) == [13, 16, 19, 22]
    assert API.get_diagonale_secondaire(m2) == ['C', 'E', 'G']
    assert API.get_diagonale_secondaire(m3) == [6, 5, 4]

def test_transpose():
    m1 = matrice1()
    tram1 = tra_m1()
    m2 = matrice2()
    tram2 = tra_m2()
    m3 = matrice3()
    tram3 = tra_m3()
    assert API.transpose(m1) == tram1
    assert API.transpose(m2) == tram2
    assert API.transpose(m3) == tram3

def test_triangulaire_inf():
    m1 = matrice1b()
    trim1 = tri_m1()
    m2 = matrice2b()
    trim2 = tri_m2()
    m3 = matrice3()
    trim3 = tri_m3()
    assert not API.is_triangulaire_inf(m1)
    assert API.is_triangulaire_inf(trim1)
    assert not API.is_triangulaire_inf(m2)
    assert API.is_triangulaire_inf(trim2)
    assert not API.is_triangulaire_inf(m3)
    assert API.is_triangulaire_inf(trim3) 

def test_ts():
    m1 = matrice1b()
    trism1 = tris_m1()
    m2 = matrice2b()
    tris2 = tris_m2()
    m3 = matrice3()
    tris3 = tris_m3()
    assert not API.is_triangulaire_sup(m1)
    assert API.is_triangulaire_sup(trism1)
    assert not API.is_triangulaire_sup(m2)
    assert API.is_triangulaire_sup(tris2)
    assert not API.is_triangulaire_sup(m3)
    assert API.is_triangulaire_sup(tris3)

def test_bloc():
    m1 = matrice1()
    bm1 = bloc_m1()
    m2 = matrice2()
    bm2 = bloc_m2()
    m3 = matrice3()
    bm3 = bloc_m3()
    assert API.bloc(m1, 1, 1, 2, 2) == bm1
    assert API.bloc(m2, 0, 0, 1, 3) == bm2
    assert API.bloc(m3, 1, 0, 2, 3) == bm3

def somme_m1btrim1():
    sm1 = API.construire_matrice(4, 4)
    API.set_val(sm1, 0, 0, 20)
    API.set_val(sm1, 0, 1, 11)
    API.set_val(sm1, 0, 2, 12)
    API.set_val(sm1, 0, 3, 13)
    API.set_val(sm1, 1, 0, 28)
    API.set_val(sm1, 1, 1, 30)
    API.set_val(sm1, 1, 2, 16)
    API.set_val(sm1, 1, 3, 17)
    API.set_val(sm1, 2, 0, 36)
    API.set_val(sm1, 2, 1, 38)
    API.set_val(sm1, 2, 2, 40)
    API.set_val(sm1, 2, 3, 21)
    API.set_val(sm1, 3, 0, 44)
    API.set_val(sm1, 3, 1, 46)
    API.set_val(sm1, 3, 2, 48)
    API.set_val(sm1, 3, 3, 50)
    return sm1
def test_som():
    mvide = API.construire_matrice(4, 4)
    m1 = matrice1b()
    m1b = tri_m1()
    som = somme_m1btrim1()
    assert API.somme(mvide, m1) == m1
    assert API.somme(m1, m1b) == som
def mpro1():
    mp1 = API.construire_matrice(3, 4)
    API.set_val(mp1, 0, 0, 1)
    API.set_val(mp1, 0, 1, 2)    
    API.set_val(mp1, 0, 2, 3)
    API.set_val(mp1, 0, 3, 4)
    API.set_val(mp1, 1, 0, 4)
    API.set_val(mp1, 1, 1, 3)
    API.set_val(mp1, 1, 2, 2)
    API.set_val(mp1, 1, 3, 1)
    API.set_val(mp1, 2, 0, 1)
    API.set_val(mp1, 2, 1, 2)
    API.set_val(mp1, 2, 2, 3)
    API.set_val(mp1, 2, 3, 4)
    return mp1
def mpro2():
    mp2 = API.construire_matrice(4, 3)
    API.set_val(mp2, 0, 0, 1)
    API.set_val(mp2, 0, 1, 4)    
    API.set_val(mp2, 0, 2, 1)
    API.set_val(mp2, 1, 0, 2)
    API.set_val(mp2, 1, 1, 3)
    API.set_val(mp2, 1, 2, 2)
    API.set_val(mp2, 2, 0, 3)
    API.set_val(mp2, 2, 1, 2)
    API.set_val(mp2, 2, 2, 3)
    API.set_val(mp2, 3, 0, 4)
    API.set_val(mp2, 3, 1, 1)
    API.set_val(mp2, 3, 2, 4)
    return mp2
def mpro():
    mp = API.construire_matrice(3, 3)
    API.set_val(mp, 0, 0, 30)
    API.set_val(mp, 0, 1, 20)    
    API.set_val(mp, 0, 2, 30)
    API.set_val(mp, 1, 0, 20)
    API.set_val(mp, 1, 1, 30)
    API.set_val(mp, 1, 2, 20)
    API.set_val(mp, 2, 0, 30)
    API.set_val(mp, 2, 1, 20)
    API.set_val(mp, 2, 2, 30)
    return mp
def test_pro():
    mp1 = mpro1()
    mp2 = mpro2()
    pro = mpro()
    assert API.produit(mp1 , mp2) == pro