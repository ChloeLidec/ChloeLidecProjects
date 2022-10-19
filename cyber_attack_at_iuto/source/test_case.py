"""
              Projet CyberAttack@IUT'O
        SAÉ1.01 département Informatique IUT d'Orléans 2021-2022

    Module case.py
    ce module teste les cases du plateau
"""
# pylint: disable=missing-function-docstring
import trojan
import protection
import equipement
import case

def creer_5_cases():
    res = {}
    case1 = case.creer_case("H", None, None, [])
    res[1] = {"case":case1, "fleche":'H', "protection":None, "serveur":None, "presents":[]}
    prot = protection.creer_protection(protection.DPO, 2)
    case2 = case.creer_case("", prot, None, [])
    res[2] = {"case":case2, "fleche":'', "protection":prot, "serveur":None, "presents":[]}
    equip = equipement.creer_equipement(equipement.SERVEUR, 10)
    case3 = case.creer_case("", None, equip, [])
    res[3] = {"case":case3, "fleche":'', "protection":None, "serveur":equip, "presents":[]}
    liste_tro = [trojan.creer_trojan(1, 3, 'G'), trojan.creer_trojan(2, 0, 'H')]
    case4 = case.creer_case("", None, None, liste_tro)
    res[4] = {"case":case4, "fleche":'', "protection":None, "serveur":None, "presents":liste_tro.copy()}
    prot = protection.creer_protection(protection.DONNEES_PERSONNELLES, 1)
    case5 = case.creer_case("G", prot, None, [])
    res[5] = {"case":case5, "fleche":'G', "protection":prot, "serveur":None, "presents":[]}
    return res

def test_get_fleche():
    res = creer_5_cases()
    for elem in res.values():
        assert case.get_fleche(elem["case"]) == elem["fleche"]

def get_protection():
    res = creer_5_cases()
    for elem in res.values():
        assert case.get_protection(elem["case"]) == elem["protection"]

def test_get_serveur():
    res = creer_5_cases()
    for elem in res.values():
        assert case.get_serveur(elem["case"]) == elem["serveur"]

def test_get_trojans():
    res = creer_5_cases()
    for elem in res.values():
        assert case.get_trojans(elem["case"]) == elem["presents"]
        
def test_get_trojans_entrants():
    res = creer_5_cases()
    for elem in res.values():
        assert case.get_trojans_entrants(elem["case"]) == []

def test_set_fleche():
    res = creer_5_cases()
    direc = "HBGDHGDB"
    ind = 0
    for elem in res.values():
        case.set_fleche(elem["case"],direc[ind])
        assert case.get_fleche(elem["case"]) == direc[ind]
        ind += 1

def test_set_serveur():
    res = creer_5_cases()
    resistance = 10
    for elem in res.values():
        serv = equipement.creer_equipement(equipement.SERVEUR, resistance)
        case.set_serveur(elem["case"], serv)
        assert case.get_serveur(elem["case"]) == serv
        resistance -= 1

def test_set_protection():
    res = creer_5_cases()
    ind = 0
    for elem in res.values():
        prot = protection.creer_protection(ind, 2)
        case.set_protection(elem["case"], prot)
        assert case.get_protection(elem["case"]) == prot
        ind += 1

def test_set_les_trojans():
    res = creer_5_cases()
    liste1 = [trojan.creer_trojan(1, 0, 'G'), trojan.creer_trojan(2, 1, 'D'),
        trojan.creer_trojan(1, 4, 'H'), trojan.creer_trojan(3, 3, 'B'),trojan.creer_trojan(3, 0, 'G')]
    liste2 = []
    for elem in res.values():
        case.set_les_trojans(elem["case"], liste1.copy(), liste2.copy())
        assert case.get_trojans(elem["case"]) == iste1 and case.get_trojans_entrants(elem["case"])==liste2
        liste2.append(liste1.pop())

def test_ajouter_trojan():
    res=creer_5_cases()
    tro1=trojan.creer_trojan(1,0,'G')
    tro2=trojan.creer_trojan(3,3,'B')
    for elem in res.values():
        case.ajouter_trojan(elem["case"],tro1)
        assert case.get_trojans_entrants(elem["case"])==[tro1]
        case.ajouter_trojan(elem["case"],tro2)
        assert case.get_trojans_entrants(elem["case"])==[tro1,tro2]

def mettre_a_jour_case():
    res=creer_5_cases()
    # premiere case
    tro1=trojan.creer_trojan(1,0,'G')
    tro2=trojan.creer_trojan(3,3,'B')
    cas=res[1]["case"]
    case.ajouter_trojan(cas,tro1)
    case.ajouter_trojan(cas,tro2)
    t1a=trojan.creer_trojan(1,0,'H')
    t2a=trojan.creer_trojan(3,3,'H')
    le_resuliste_troat=case.mettre_a_jour_case(cas)
    assert le_resuliste_troat=={1:1,2:0,3:1,4:0}
    assert case.get_trojans(cas) in [[t1a,t2a],[t2a,t1a]]
    assert case.get_trojans_entrants(cas)==[]
    
    # troisieme case
    tro1=trojan.creer_trojan(1,0,'G')
    tro2=trojan.creer_trojan(3,3,'B')
    cas=res[3]["case"]
    t1a=trojan.creer_trojan(1,0,'H')
    t2a=trojan.creer_trojan(3,3,'H')
    le_resuliste_troat=case.mettre_a_jour_case(cas)
    assert le_resuliste_troat=={1:0,2:0,3:0,4:0}
    assert case.get_trojans(cas)== []
    assert case.get_trojans_entrants(cas)==[]
    assert equipement.get_resistance(case.get_serveur(cas))==9
    # quatrieme case
    tro1=trojan.creer_trojan(1,0,'G')
    tro2=trojan.creer_trojan(3,3,'B')
    cas=res[4]["case"]
    le_resuliste_troat=case.mettre_a_jour_case(cas)
    assert le_resuliste_troat=={1:1,2:0,3:1,4:0}
    assert case.get_trojans(cas)== res[4]["presents"]+[tro1,tro2]
    assert case.get_trojans_entrants(cas)==[]

def test_poser_avatar():
    res=creer_5_cases()
    for elem in res.values():
        le_res=case.poser_avatar(elem["case"])
        assert case.contient_avatar(elem["case"])
        if len(elem["presents"])==0:
            assert le_res=={1:0,2:0,3:0,4:0}
        else:
            assert le_res=={1:1,2:1,3:0,4:0}

def test_enlever_avatar():
    res=creer_5_cases()
    for elem in res.values():
        case.enlever_avatar(elem["case"])
        assert not case.contient_avatar(elem["case"])

def test_contient_avatar():
    res=creer_5_cases()
    for elem in res.values():
        assert not case.contient_avatar(elem["case"])        

def test_reinit_trojans_entrants():
    res=creer_5_cases()
    for elem in res.values():
        case.ajouter_trojan(elem["case"],trojan.creer_trojan(1,1,'G'))
        case.reinit_trojans_entrants(elem["case"])
        assert case.get_trojans_entrants(elem["case"])==[] 
