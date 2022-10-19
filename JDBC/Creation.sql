-- CREATE DATABASE IF NOT EXISTS ENTREPOT DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE DBlidec;

drop table STOCKER;
drop table ARTICLE;
drop table ENTREPOT;

CREATE TABLE ARTICLE (
  reference INT(9),
  libelle VARCHAR(42),
  prix DECIMAL(6,2),
  PRIMARY KEY (reference)
) ;

CREATE TABLE ENTREPOT (
  code INT(9),
  nom VARCHAR(42),
  departement VARCHAR(42),
  PRIMARY KEY (code)
) ;

CREATE TABLE STOCKER (
  reference INT(9),
  code INT(9),
  quantite INT(5),
  PRIMARY KEY (reference, code)
) ;

ALTER TABLE STOCKER ADD FOREIGN KEY (code) REFERENCES ENTREPOT (code);
ALTER TABLE STOCKER ADD FOREIGN KEY (reference) REFERENCES ARTICLE (reference);



-- 1. Creer un trigger pour faire en sorte que on ne veut pas avoir plusieurs entrepots avec le meme nom dans le meme departement.
-- 2. Creer un trigger pour faire en sorte que on ne veut pas plus de trois entrepots dans un meme departement.
DELIMITER |
CREATE OR REPLACE TRIGGER unNomDansDept BEFORE INSERT ON ENTREPOT FOR EACH ROW
BEGIN
    IF (SELECT COUNT(*) FROM ENTREPOT WHERE nom=NEW.nom AND departement=NEW.departement)>0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Un entrepot avec ce nom existe deja dans ce departement';
    END IF;
    IF (SELECT COUNT(*) FROM ENTREPOT WHERE departement=NEW.departement)>=3 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Il y a deja 3 entrepots dans ce departement';
    END IF;
END |
DELIMITER ;

-- 3. A chaque fois que le stock d’un article est modifie (a la hausse ou a la baisse), on veut
-- conserver une trace de la mise a jour
CREATE TABLE IF NOT EXISTS ARCHIVE (
  reference INT(9),
  code INT(9),
  quantite INT(5),
  dateMaj DATE
) ;
DELIMITER |
CREATE OR REPLACE TRIGGER stockMaj AFTER UPDATE ON STOCKER FOR EACH ROW
BEGIN
    INSERT INTO ARCHIVE VALUES (OLD.reference, OLD.code, OLD.quantite,NOW());
END |
DELIMITER ;
    
insert into ARTICLE values(1, 'Chaise', 49),
                          (2, 'Table', 110), 
                          (123, 'tuile17x27', 2.55);
    
insert into ENTREPOT values(1, 'Orléans nord', 'Loiret'), 
                           (2, 'Orléans sud', 'Loiret'), 
                           (3, 'Bourges', 'Cher');

insert into STOCKER values(1, 1, 45), 
                          (1, 2, 55),
                          (1, 3, 25),
                          (2, 1, 10),
                          (123, 2, 2000),
                          (123, 3, 1250);
