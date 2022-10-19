-- Ecrire une requete parametree pour avoir la liste des articles valant moins d’une
-- certaine somme.
PREPARE moinsque FROM 'SELECT reference,libelle,prix FROM ARTICLE WHERE prix<?';
set @pr=20;
--execute moinsque using @pr ;

-- 2. Ecrire une requete parametree pour avoir, en fonction du libelle d’un article et d’un
-- departement, les quantite en stock de cet article dans les entrepots du departement
-- choisi
PREPARE quantArt FROM 'SELECT reference,libelle,prix,departement,SUM(quantite) 
FROM ARTICLE NATURAL JOIN STOCKER NATURAL JOIN ENTREPOT 
WHERE libelle=? AND departement=?
GROUP BY libelle';
set @pr1="Chaise";
set @pr2="Loiret";
--execute quantArt using @pr1,@pr2 ;


-- Ecrire une fonction maxRefArticle qui retourne la plus grande reference utilisee pour
-- identifier un article. (0 si la table article est vide).
DELIMITER |
CREATE OR REPLACE FUNCTION maxRefArticle() returns int
BEGIN
    DECLARE res INT;
    SELECT IFNULL(max(reference),0) INTO res FROM ARTICLE;
    RETURN res;
END |
DELIMITER ;
--SELECT maxRefArticle();

-- 2. Ecrire une fonction deptEntrepot(codeEnt int) qui retourne le departement ou se
-- trouve l’entrepot de code codeEnt.
DELIMITER |
CREATE OR REPLACE FUNCTION deptEntrepot(codeEnt int) returns VARCHAR(42)
BEGIN
    DECLARE dpt VARCHAR(42);
    SELECT departement INTO dpt FROM ENTREPOT WHERE code=codeEnt;
    RETURN dpt;
END |
DELIMITER ;
--SELECT deptEntrepot(2);


-- 3. Ecrire une fonction valEntrepot(codeEnt int) qui retourne la valeur des marchan-
-- dises contenues dans l’entrepot codeEnt.
DELIMITER |
CREATE OR REPLACE FUNCTION valEntrepot(codeEnt int) returns DECIMAL(6,2)
BEGIN
    DECLARE valTot DECIMAL(6,2);
    SELECT SUM(quantite*prix) INTO valTot FROM ENTREPOT NATURAL JOIN STOCKER NATURAL JOIN ARTICLE 
    WHERE code=codeEnt GROUP BY code;
    RETURN valTot;
END |
DELIMITER ;

-- 4. Ecrire une procedure pour afficher tous les entrepots.
DELIMITER |
CREATE OR REPLACE PROCEDURE tousEntrepots()
BEGIN 
    DECLARE res VARCHAR(500) DEFAULT '';
    DECLARE codeE INT(9);
    DECLARE nomE VARCHAR(42);
    DECLARE dpt VARCHAR(42);
    DECLARE fini BOOLEAN DEFAULT false;
    DECLARE cursorEnt CURSOR FOR
        SELECT code,nom,departement FROM ENTREPOT;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET fini=true;
    OPEN cursorEnt;
        WHILE NOT fini DO
            FETCH cursorEnt INTO codeE,nomE,dpt;
            IF NOT fini THEN
                SET res = CONCAT(res,codeE,' ',nomE,' ',dpt,' \n');
            END IF;
        END WHILE;
    CLOSE cursorEnt;
    SELECT res;
END |
DELIMITER ;
--CALL tousEntrepots();
-- 5. Ecrire une procédure pour afficher pour chaque departement, le nombre d’entrepots et les entrepots presents dans ce departement.
DELIMITER |
CREATE OR REPLACE PROCEDURE triEnt()
BEGIN 
    DECLARE res VARCHAR(500) DEFAULT '';
    DECLARE dpt VARCHAR(42);
    DECLARE fini BOOLEAN DEFAULT false;
    DECLARE cursorEnt CURSOR FOR
        SELECT departement FROM ENTREPOT GROUP BY departement;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET fini=true;
    OPEN cursorEnt;
        WHILE NOT fini DO
            FETCH cursorEnt INTO dpt;
            IF NOT fini THEN
                SET res = CONCAT(res,dpt,' a ',(SELECT COUNT(*) FROM ENTREPOT WHERE departement=dpt),' entrepots qui sont \n');
                SET res = CONCAT(res,(SELECT GROUP_CONCAT(nom) FROM ENTREPOT WHERE departement=dpt),' \n');
            END IF;
        END WHILE;
    CLOSE cursorEnt;
    SELECT res;
END |
CALL triEnt();
DELIMITER ;
-- 6. crire une procedure pour afficher tous les entrepots groupés par departement 
-- on utilise une requete pour avoir le nombre d’entrepots par departement et la valeur totale des marchandises dans chaque entrepot
DELIMITER |
CREATE OR REPLACE PROCEDURE triEntVal()
BEGIN 
    DECLARE res VARCHAR(500) DEFAULT '';
    DECLARE codeE INT(9);
    DECLARE nomE VARCHAR(42);
    DECLARE dpt VARCHAR(42);
    DECLARE deptP VARCHAR(42) DEFAULT '';
    DECLARE nbe INT(9) DEFAULT 1;
    DECLARE val DECIMAL(6,2) DEFAULT 0;
    DECLARE fini BOOLEAN DEFAULT false;
    DECLARE cursorEnt CURSOR FOR
        SELECT nom,code,departement FROM ENTREPOT ORDER BY departement;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET fini=true;
    OPEN cursorEnt;
        WHILE NOT fini DO
            FETCH cursorEnt INTO nomE,codeE,dpt;
            IF NOT fini THEN
                IF  deptP='' or dpt<>deptP THEN
                    SET res = CONCAT(res,'Le departement ',dpt,' a ',nbe,' entrepots \n');
                    SET deptP=dpt;
                    SET nbe=1;
                END IF;
                SET val = valEntrepot(codeE);

                SET res = CONCAT(res,'Entrepot ',nomE,' S',codeE,' ',dpt,' a une val tot de ',val,'\n');
                SET nbe=nbe+1;

            END IF;
        END WHILE;
    CLOSE cursorEnt;
    SELECT res;
END |
DELIMITER ;

CALL triEntVal();
-- 7. Ecrire une fonction qui permet de stocker un nouvel article dans la table article
-- ou de modifier le prix d’un article dej`a existant. Par exemple majArticle(123,
-- ’tuile17x27’, 3.55) modifiera le prix de l’article 123 s’il existe et qu’il correspond
-- `a ’tuile 17x27’, si ne nom n’est pas ’tuile17x27’ afficher un message d’erreur,
-- si l’article 123 n’est pas dans la base ajouter un nouvel article en prenant comme
-- reference la plus grande des references presentes dans la base plus 1 `a la place de 123.
-- La fonction retournera la reference de l’article cree ou modifie (-1 si erreur).
DELIMITER |
CREATE OR REPLACE FUNCTION majArticle(ref INT(9), nom VARCHAR(42), prix DECIMAL(9,2)) returns INT(9)
BEGIN 
    DECLARE res INT(9) DEFAULT -1;
    DECLARE refMax INT(9) DEFAULT 0;
    DECLARE refMin INT(9) DEFAULT 0;
    DECLARE refE INT(9);
    DECLARE nomE VARCHAR(42);
    DECLARE prixE DECIMAL(9,2);
    DECLARE fini BOOLEAN DEFAULT false;
    DECLARE cursorArt CURSOR FOR
        SELECT reference,libelle,prix FROM ARTICLE;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET fini=true; 
    OPEN cursorArt;
        WHILE NOT fini DO
            FETCH cursorArt INTO refE,nomE,prixE;
            IF refE > refMax THEN
                SET refMax=refE;
            END IF;
            IF refE < refMin THEN
                SET refMin=refE;
            END IF;
            IF refE = ref THEN
                IF nomE = nom THEN
                    UPDATE ARTICLE SET prix=prix WHERE reference=ref;
                    SET res=ref;
                END IF;
            END IF;
        END WHILE;
    CLOSE cursorArt;
    IF res = -1 THEN -- si l'article n'existe pas
        INSERT INTO ARTICLE VALUES (refMax+1,nom,prix);
        SET res=refMax+1;
    END IF;
    RETURN res;
END |
DELIMITER ;
SELECT majArticle(123,'tuile17x27',3.55);
SELECT * FROM ARTICLE;
-- -- 8. Ecrire une fonction entrerStock(refA int, codeE int, qte int) qui augmente
-- -- le stock de l’article refA dans l’entrepot codeE de qte. Retourne la nouvelle quantite
-- -- de l’article (-1) quand l’article ou l’entrepot n’existe pas.
DELIMITER |
CREATE OR REPLACE FUNCTION entrerStock(refA INT(9), codeE INT(9), qte INT(9)) returns int
BEGIN 
    DECLARE res INT(9) DEFAULT -1;
    DECLARE refE INT(9);
    DECLARE codeEE INT(9);
    DECLARE qteE INT(9);
    DECLARE fini BOOLEAN DEFAULT false;
    
        IF res = -1 AND (SELECT COUNT(*) FROM ARTICLE WHERE reference=refA) = 1 AND (SELECT COUNT(*) FROM ENTREPOT WHERE code=codeE) = 1 THEN
            INSERT INTO STOCKER VALUES (refA,codeE,qte);
            SET res=qte;
        END IF;
        ELSE
            qte= SELECT qteE FROM STOCKER WHERE reference=refA AND code=codeE;
            UPDATE STOCKER SET quantite=quantite+qte WHERE reference=refA AND code=codeE;
            SET res=qteE+qte;
    CLOSE cursorArt;
    COMMIT;
    RETURN res;
END |
DELIMITER ;
SELECT * FROM STOCKER;
SELECT entrerStock(123,3,10);
SELECT * FROM STOCKER;
-- 9. Ecrire une fonction sortirStock(refA int, codeE int, qte int) qui diminue le
-- stock de l’article refA dans l’entrepot codeE de qte. La quantite `a sortir est limitee
-- `a la quantite presente. Retourne la quantite reellement sortie.
DELIMITER |
CREATE OR REPLACE FUNCTION sortirStock(refA INT(9), codeE INT(9), qte INT(9)) returns int
BEGIN 
    DECLARE res INT(9) DEFAULT -1;
    DECLARE refE INT(9);
    DECLARE codeEE INT(9);
    DECLARE qteE INT(9);
    DECLARE fini BOOLEAN DEFAULT false;
    DECLARE cursorArt CURSOR FOR
        SELECT reference,code,quantite FROM STOCKER;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET fini=true; 
    OPEN cursorArt;
        WHILE NOT fini DO
            FETCH cursorArt INTO refE,codeEE,qteE;
            IF refE = refA AND codeEE = codeE THEN 
                -- si l'article n'existe pas dans l'entrepot
                IF qteE >= qte THEN
                    UPDATE STOCKER SET quantite=quantite-qte WHERE reference=refA AND code=codeE;
                    SET res=qte;
                ELSE
                    UPDATE STOCKER SET quantite=0 WHERE reference=refA AND code=codeE;
                    SET res=qteE;
                END IF;
            END IF;
        END WHILE;
    CLOSE cursorArt;
    COMMIT;
    RETURN res;
END |
DELIMITER ;
SELECT * FROM STOCKER;
SELECT sortirStock(123,1,20);
SELECT * FROM STOCKER;