BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "eleve" (
	"num_etu"	integer NOT NULL,
	"nom"	varchar(50) NOT NULL,
	"prenom"	varchar(50) NOT NULL,
	"groupe_s1"	varchar(50) NOT NULL,
	"groupe_s2"	varchar(50) NOT NULL,
	PRIMARY KEY("num_etu" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "matiere" (
	"id_matiere"	integer NOT NULL,
	"nom_matiere"	varchar(50) NOT NULL,
	PRIMARY KEY("id_matiere" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "periode" (
	"id_periode"	integer NOT NULL,
	"date_debut"	varchar(500) NOT NULL,
	"date_fin"	varchar(500) NOT NULL,
	"semestre"	integer NOT NULL,
	PRIMARY KEY("id_periode" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "professeur" (
	"id_prof"	varchar(50) NOT NULL,
	"nom_prof"	varchar(50) NOT NULL,
	"prenom_prof"	varchar(50) NOT NULL,
	"email_prof"	varchar(500) NOT NULL,
	PRIMARY KEY("id_prof")
);
CREATE TABLE IF NOT EXISTS "semaine" (
	"id_semaine"	integer NOT NULL,
	"date_debut"	varchar(500) NOT NULL,
	"date_fin"	varchar(500) NOT NULL,
	"id_periode_id"	integer NOT NULL,
	FOREIGN KEY("id_periode_id") REFERENCES "periode"("id_periode") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id_semaine" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "oral" (
	"id_oral"	integer NOT NULL,
	"date_oral"	varchar(500) NOT NULL,
	"heure_oral"	varchar(500) NOT NULL,
	"id_matiere_id"	integer NOT NULL,
	"id_prof_id"	varchar(50) NOT NULL,
	PRIMARY KEY("id_oral" AUTOINCREMENT),
	FOREIGN KEY("id_prof_id") REFERENCES "professeur"("id_prof") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("id_matiere_id") REFERENCES "matiere"("id_matiere") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "possibilitesoutien" (
	"id"	integer NOT NULL,
	"id_matiere_id"	integer NOT NULL,
	"id_periode_id"	integer NOT NULL,
	"id_prof_id"	varchar(50) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("id_periode_id") REFERENCES "periode"("id_periode") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("id_matiere_id") REFERENCES "matiere"("id_matiere") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("id_prof_id") REFERENCES "professeur"("id_prof") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "participantsoral" (
	"id"	integer NOT NULL,
	"commentaire"	varchar(800) NOT NULL,
	"id_oral_id"	integer NOT NULL,
	"num_etu_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("id_oral_id") REFERENCES "oral"("id_oral") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("num_etu_id") REFERENCES "eleve"("num_etu") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "estdisponible" (
	"id"	integer NOT NULL,
	"id_oral_id"	integer NOT NULL,
	"id_prof_id"	varchar(50) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("id_oral_id") REFERENCES "oral"("id_oral") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("id_prof_id") REFERENCES "professeur"("id_prof") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "params" (
	"id"	integer NOT NULL,
	"jour_sout"	varchar(10) NOT NULL,
	"heure_sout"	time NOT NULL,
	"seuil"	real NOT NULL,
	"date_rentree"	date NOT NULL,
	"date_fin_p1"	date NOT NULL,
	"date_fin_p2"	date NOT NULL,
	"date_fin_p3"	date NOT NULL,
	"date_fin_annee"	date NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "qcm" (
	"id_qcm"	integer NOT NULL,
	"nom_qcm"	varchar(50) NOT NULL,
	"url_qcm"	varchar(500) NOT NULL,
	"date_debut"	varchar(500) NOT NULL,
	"date_fin"	varchar(500) NOT NULL,
	"id_matiere_id"	integer NOT NULL,
	PRIMARY KEY("id_qcm" AUTOINCREMENT),
	FOREIGN KEY("id_matiere_id") REFERENCES "matiere"("id_matiere") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "resultatqcm" (
	"id"	integer NOT NULL,
	"note"	integer NOT NULL,
	"id_qcm_id"	integer NOT NULL,
	"num_etu_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("id_qcm_id") REFERENCES "qcm"("id_qcm") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("num_etu_id") REFERENCES "eleve"("num_etu") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "sondage" (
	"id_sond"	integer NOT NULL,
	"url_sond"	varchar(500) NOT NULL,
	"date_sond"	varchar(500) NOT NULL,
	PRIMARY KEY("id_sond" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "repsondage" (
	"id"	integer NOT NULL,
	"matiere_voulue"	varchar(100) NOT NULL,
	"volontaire"	varchar(50) NOT NULL,
	"commentaire"	varchar(800) NOT NULL,
	"id_sondage_id"	integer NOT NULL,
	"num_etu_id"	integer NOT NULL,
	FOREIGN KEY("id_sondage_id") REFERENCES "sondage"("id_sond") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("num_etu_id") REFERENCES "eleve"("num_etu") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "reponsequestionsondage" (
	"id"	integer NOT NULL,
	"reponse"	varchar(500) NOT NULL,
	"id_quest_id"	integer NOT NULL,
	"num_etu_id"	integer NOT NULL,
	FOREIGN KEY("id_quest_id") REFERENCES "questionsondage"("id_quest") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("num_etu_id") REFERENCES "eleve"("num_etu") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "questionsondage" (
	"id_quest"	integer NOT NULL,
	"question"	varchar(500) NOT NULL,
	"id_sond_id"	integer NOT NULL,
	PRIMARY KEY("id_quest" AUTOINCREMENT),
	FOREIGN KEY("id_sond_id") REFERENCES "sondage"("id_sond") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"last_name"	varchar(150) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"first_name"	varchar(150) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "user" (
	"username"	varchar(50) NOT NULL,
	"password"	varchar(64) NOT NULL,
	"est_admin"	varchar(1) NOT NULL,
	PRIMARY KEY("username")
);
CREATE INDEX IF NOT EXISTS "semaine_id_periode_id_384febf1" ON "semaine" (
	"id_periode_id"
);
CREATE INDEX IF NOT EXISTS "oral_id_matiere_id_01ba43a4" ON "oral" (
	"id_matiere_id"
);
CREATE INDEX IF NOT EXISTS "oral_id_prof_id_1ee270ae" ON "oral" (
	"id_prof_id"
);
CREATE INDEX IF NOT EXISTS "possibilitesoutien_id_matiere_id_60c11fdc" ON "possibilitesoutien" (
	"id_matiere_id"
);
CREATE INDEX IF NOT EXISTS "possibilitesoutien_id_periode_id_4cb89e62" ON "possibilitesoutien" (
	"id_periode_id"
);
CREATE INDEX IF NOT EXISTS "possibilitesoutien_id_prof_id_d92287ff" ON "possibilitesoutien" (
	"id_prof_id"
);
CREATE INDEX IF NOT EXISTS "participantsoral_id_oral_id_b5236e19" ON "participantsoral" (
	"id_oral_id"
);
CREATE INDEX IF NOT EXISTS "participantsoral_num_etu_id_16064fc8" ON "participantsoral" (
	"num_etu_id"
);
CREATE INDEX IF NOT EXISTS "estdisponible_id_oral_id_145c4247" ON "estdisponible" (
	"id_oral_id"
);
CREATE INDEX IF NOT EXISTS "estdisponible_id_prof_id_c15fab7c" ON "estdisponible" (
	"id_prof_id"
);
CREATE INDEX IF NOT EXISTS "qcm_id_matiere_id_2df0c341" ON "qcm" (
	"id_matiere_id"
);
CREATE INDEX IF NOT EXISTS "resultatqcm_id_qcm_id_8fad5c61" ON "resultatqcm" (
	"id_qcm_id"
);
CREATE INDEX IF NOT EXISTS "resultatqcm_num_etu_id_f2a07428" ON "resultatqcm" (
	"num_etu_id"
);
CREATE INDEX IF NOT EXISTS "repsondage_id_sondage_id_f1bd2174" ON "repsondage" (
	"id_sondage_id"
);
CREATE INDEX IF NOT EXISTS "repsondage_num_etu_id_6938e85d" ON "repsondage" (
	"num_etu_id"
);
CREATE INDEX IF NOT EXISTS "reponsequestionsondage_id_quest_id_6497b8be" ON "reponsequestionsondage" (
	"id_quest_id"
);
CREATE INDEX IF NOT EXISTS "reponsequestionsondage_num_etu_id_7271c6aa" ON "reponsequestionsondage" (
	"num_etu_id"
);
CREATE INDEX IF NOT EXISTS "questionsondage_id_sond_id_74071d7a" ON "questionsondage" (
	"id_sond_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" (
	"user_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_group_id_97559544" ON "auth_user_groups" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" (
	"user_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
COMMIT;
