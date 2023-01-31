CREATE SCHEMA IF NOT EXISTS groep_64;

CREATE  TABLE groep_64.contactpersoon ( 
	personeelsnummer     char(8)  NOT NULL  ,
	voornaam             varchar(60)  NOT NULL  ,
	achternaam           varchar(100)  NOT NULL  ,
	"e-mail"             varchar(200)  NOT NULL  ,
	telefoonnummer       varchar(20)  NOT NULL  ,
	CONSTRAINT pk_contactpersoon PRIMARY KEY ( personeelsnummer )
 );

CREATE  TABLE groep_64.klant ( 
	naam_klant           varchar(150)  NOT NULL  ,
	CONSTRAINT pk_klant PRIMARY KEY ( naam_klant )
 );

CREATE  TABLE groep_64.label ( 
	label                varchar(100)  NOT NULL  ,
	CONSTRAINT pk_label PRIMARY KEY ( label )
 );

CREATE  TABLE groep_64.medewerker ( 
	personeelsnummer     char(8)  NOT NULL  ,
	voornaam             varchar(60)  NOT NULL  ,
	achternaam           varchar(100)  NOT NULL  ,
	"e-mail"             varchar(200)  NOT NULL  ,
	telefoonnummer       varchar(20)  NOT NULL  ,
	capaciteit           smallint  NOT NULL  ,
	CONSTRAINT pk_medewerker PRIMARY KEY ( personeelsnummer )
 );

CREATE  TABLE groep_64.rate_algemene_werking ( 
	inschattingsjaar     date  NOT NULL  ,
	rate                 numeric  NOT NULL  ,
	CONSTRAINT pk_rate_algemene_werking PRIMARY KEY ( inschattingsjaar )
 );

ALTER TABLE groep_64.rate_algemene_werking ADD CONSTRAINT cns_rate_algemene_werking_jaar CHECK ( ((EXTRACT(month FROM inschattingsjaar) = (1)::numeric) AND (EXTRACT(day FROM inschattingsjaar) = (1)::numeric) AND (inschattingsjaar >= '2014-01-01'::date)) );

CREATE  TABLE groep_64.rate_taak ( 
	rate                 numeric  NOT NULL  ,
	rate_id              char(3)  NOT NULL  ,
	CONSTRAINT pk_rate_taak PRIMARY KEY ( rate_id )
 );

CREATE  TABLE groep_64.type_dienst ( 
	typenaam             varchar(21)  NOT NULL  ,
	CONSTRAINT pk_type_dienst PRIMARY KEY ( typenaam )
 );

CREATE  TABLE groep_64.aanvraag ( 
	id                   char(8)  NOT NULL  ,
	huidige_status       varchar(8)  NOT NULL  ,
	beschrijving         varchar(400)  NOT NULL  ,
	naam_aanvrager       varchar(120)  NOT NULL  ,
	aanvraagdatum        date  NOT NULL  ,
	deadline             date  NOT NULL  ,
	naam_klant           varchar(150)  NOT NULL  ,
	intern_of_extern     char(6)  NOT NULL  ,
	CONSTRAINT pk_aanvraag PRIMARY KEY ( id ),
	CONSTRAINT fk_aanvraag_klant FOREIGN KEY ( naam_klant ) REFERENCES groep_64.klant( naam_klant )   
 );

ALTER TABLE groep_64.aanvraag ADD CONSTRAINT cns_aanvraag_aanvraagdatum CHECK ( ((aanvraagdatum >= '2014-01-01'::date) AND (aanvraagdatum < date(now()))) );

ALTER TABLE groep_64.aanvraag ADD CONSTRAINT cns_aanvraag_deadline CHECK ( ((deadline >= '2014-01-01'::date) AND (deadline > aanvraagdatum)) );

CREATE  TABLE groep_64.aanvraag_voor_type_dienst ( 
	id                   char(8)  NOT NULL  ,
	typenaam             varchar(21)  NOT NULL  ,
	CONSTRAINT pk_aanvraag_voor_type_dienst PRIMARY KEY ( id, typenaam ),
	CONSTRAINT fk_aanvraag_voor_type_dienst_aanvraag FOREIGN KEY ( id ) REFERENCES groep_64.aanvraag( id )   ,
	CONSTRAINT fk_aanvraag_voor_type_dienst_type_dienst FOREIGN KEY ( typenaam ) REFERENCES groep_64.type_dienst( typenaam )   
 );

CREATE  TABLE groep_64.contactpersoon_in_aanvraag ( 
	personeelsnummer     char(8)  NOT NULL  ,
	id                   char(8)  NOT NULL  ,
	CONSTRAINT pk_contactpersoon_wordt_vermeldt_in_aanvraag PRIMARY KEY ( personeelsnummer, id ),
	CONSTRAINT fk_contactpersoon_wordt_vermeldt_in_aanvraag_aanvraag FOREIGN KEY ( id ) REFERENCES groep_64.aanvraag( id )   ,
	CONSTRAINT fk_contactpersoon_wordt_vermeldt_in_aanvraag_contactpersoon FOREIGN KEY ( personeelsnummer ) REFERENCES groep_64.contactpersoon( personeelsnummer )   
 );

CREATE  TABLE groep_64.contactpersoon_van_klant ( 
	personeelsnummer     char(8)  NOT NULL  ,
	naam_klant           varchar(150)  NOT NULL  ,
	CONSTRAINT pk_contactpersoon_van_klant PRIMARY KEY ( personeelsnummer, naam_klant ),
	CONSTRAINT fk_contactpersoon_van_klant_contactpersoon FOREIGN KEY ( personeelsnummer ) REFERENCES groep_64.contactpersoon( personeelsnummer )   ,
	CONSTRAINT fk_contactpersoon_van_klant_klant FOREIGN KEY ( naam_klant ) REFERENCES groep_64.klant( naam_klant )   
 );

CREATE  TABLE groep_64.externe_klant ( 
	naam_klant           varchar(150)  NOT NULL  ,
	adres                varchar(300)  NOT NULL  ,
	CONSTRAINT pk_externe_klant PRIMARY KEY ( naam_klant ),
	CONSTRAINT fk_externe_klant_klant FOREIGN KEY ( naam_klant ) REFERENCES groep_64.klant( naam_klant )   
 );

CREATE  TABLE groep_64.interne_klant ( 
	naam_klant           varchar(150)  NOT NULL  ,
	departement          varchar(150)    ,
	opleiding            varchar(150)    ,
	campus               varchar(150)    ,
	CONSTRAINT pk_interne_klant PRIMARY KEY ( naam_klant ),
	CONSTRAINT fk_interne_klant_klant FOREIGN KEY ( naam_klant ) REFERENCES groep_64.klant( naam_klant )   
 );

ALTER TABLE groep_64.interne_klant ADD CONSTRAINT cns_interne_klant CHECK ( (((departement IS NULL) AND (opleiding IS NULL) AND (campus IS NULL)) OR ((departement IS NOT NULL) AND (opleiding IS NOT NULL) AND (campus IS NOT NULL)) OR ((departement IS NOT NULL) AND (campus IS NOT NULL))) );

CREATE  TABLE groep_64.medewerker_voor_type_dienst ( 
	personeelsnummer     char(8)  NOT NULL  ,
	typenaam             varchar(21)  NOT NULL  ,
	CONSTRAINT pk_medewerker_voor_type_dienst PRIMARY KEY ( personeelsnummer, typenaam ),
	CONSTRAINT fk_medewerker_voor_type_dienst_medewerker FOREIGN KEY ( personeelsnummer ) REFERENCES groep_64.medewerker( personeelsnummer )   ,
	CONSTRAINT fk_medewerker_voor_type_dienst_type_dienst FOREIGN KEY ( typenaam ) REFERENCES groep_64.type_dienst( typenaam )   
 );

CREATE  TABLE groep_64.project ( 
	id                   char(8)  NOT NULL  ,
	factuur              numeric    ,
	startdatum           date    ,
	einddatum            date    ,
	status               varchar(19)  NOT NULL  ,
	korting              numeric    ,
	kostenplaats         varchar(150)    ,
	verantwoordelijke_medewerker char(8)  NOT NULL  ,
	naam_klant           varchar(150)  NOT NULL  ,
	inschattingsjaar     date  NOT NULL  ,
	projectnaam          varchar(150)  NOT NULL  ,
	intern_of_extern     char(6)  NOT NULL  ,
	CONSTRAINT pk_project PRIMARY KEY ( id ),
	CONSTRAINT fk_project_aanvraag FOREIGN KEY ( id ) REFERENCES groep_64.aanvraag( id )   ,
	CONSTRAINT fk_project_klant FOREIGN KEY ( naam_klant ) REFERENCES groep_64.klant( naam_klant )   ,
	CONSTRAINT fk_project_medewerker FOREIGN KEY ( verantwoordelijke_medewerker ) REFERENCES groep_64.medewerker( personeelsnummer )   ,
	CONSTRAINT fk_project_rate_algemene_werking FOREIGN KEY ( inschattingsjaar ) REFERENCES groep_64.rate_algemene_werking( inschattingsjaar )   
 );

ALTER TABLE groep_64.project ADD CONSTRAINT cns_project_data CHECK ( ((startdatum > '2014-01-01'::date) AND (einddatum > '2014-01-01'::date) AND (einddatum > startdatum) AND ((((status)::text = 'estimation ongoing'::text) AND (startdatum IS NULL) AND (einddatum IS NULL)) OR (((status)::text = 'planned and ongoing'::text) AND (startdatum IS NOT NULL) AND (einddatum IS NOT NULL)) OR ((((status)::text = 'delivered'::text) OR ((status)::text = 'closed'::text)) AND (startdatum IS NOT NULL) AND (einddatum IS NOT NULL)))) );

ALTER TABLE groep_64.project ADD CONSTRAINT cns_project_factuur CHECK ( (((((status)::text = 'delivered'::text) OR ((status)::text = 'closed'::text)) AND (factuur IS NOT NULL)) OR ((((status)::text = 'planned and ongoing'::text) OR ((status)::text = 'estimation ongoing'::text)) AND (factuur IS NULL))) );

ALTER TABLE groep_64.project ADD CONSTRAINT cns_project_start_en_einddatum CHECK ( ((((status)::text = 'estimation ongoing'::text) AND (startdatum IS NULL) AND (einddatum IS NULL)) OR (((status)::text = 'planned and ongoing'::text) AND (startdatum IS NOT NULL)) OR ((((status)::text = 'delivered'::text) OR ((status)::text = 'closed'::text)) AND (startdatum IS NOT NULL) AND (einddatum IS NOT NULL))) );

CREATE  TABLE groep_64.project_is_gekoppeld_aan_project ( 
	id1                  char(8)  NOT NULL  ,
	id2                  char(8)  NOT NULL  ,
	CONSTRAINT pk_project_is_gekoppeld_aan_project PRIMARY KEY ( id1, id2 ),
	CONSTRAINT fk_project_is_gekoppeld_aan_project_project FOREIGN KEY ( id1 ) REFERENCES groep_64.project( id )   ,
	CONSTRAINT fk_project_is_gekoppeld_aan_project_project_0 FOREIGN KEY ( id2 ) REFERENCES groep_64.project( id )   
 );

CREATE  TABLE groep_64.registreerder_projectprestaties ( 
	id                   char(8)  NOT NULL  ,
	personeelsnummer     char(8)  NOT NULL  ,
	aantal_uren          integer  NOT NULL  ,
	datum                date  NOT NULL  ,
	opmerking_uren       varchar(400)    ,
	kosten               numeric    ,
	beschrijving_kosten  varchar(400)    ,
	CONSTRAINT pk_registreerder_projectprestaties PRIMARY KEY ( id, personeelsnummer, datum ),
	CONSTRAINT fk_registreerder_projectprestaties_medewerker FOREIGN KEY ( personeelsnummer ) REFERENCES groep_64.medewerker( personeelsnummer )   ,
	CONSTRAINT fk_registreerder_projectprestaties_project FOREIGN KEY ( id ) REFERENCES groep_64.project( id )   
 );

ALTER TABLE groep_64.registreerder_projectprestaties ADD CONSTRAINT cns_registreerder_projectprestaties_datum CHECK ( ((datum > '2014-01-01'::date) AND (datum < date(now()))) );

ALTER TABLE groep_64.registreerder_projectprestaties ADD CONSTRAINT cns_registreerder_projectprestaties_prestaties CHECK ( (((kosten IS NOT NULL) AND (beschrijving_kosten IS NOT NULL)) OR ((kosten IS NULL) AND (beschrijving_kosten IS NULL))) );

CREATE  TABLE groep_64.relatiebeheerder ( 
	personeelsnummer     char(8)  NOT NULL  ,
	naam_klant           varchar(150)  NOT NULL  ,
	CONSTRAINT pk_contactpersoon_beheert_relatie_met_externe_klan PRIMARY KEY ( personeelsnummer, naam_klant ),
	CONSTRAINT fk_contactpersoon_beheert_relatie_met_externe_klant_contactpers FOREIGN KEY ( personeelsnummer ) REFERENCES groep_64.contactpersoon( personeelsnummer )   ,
	CONSTRAINT fk_contactpersoon_beheert_relatie_met_externe_klant_externe_kla FOREIGN KEY ( naam_klant ) REFERENCES groep_64.externe_klant( naam_klant )   
 );

CREATE  TABLE groep_64.statusveranderaar ( 
	personeelsnummer     char(8)  NOT NULL  ,
	id                   char(8)  NOT NULL  ,
	datum                date  NOT NULL  ,
	tijdstip             time  NOT NULL  ,
	opmerking            varchar(400)  NOT NULL  ,
	nieuwe_status        varchar(8)  NOT NULL  ,
	CONSTRAINT pk_statusveranderaar PRIMARY KEY ( personeelsnummer, id, nieuwe_status ),
	CONSTRAINT fk_statusveranderaar_aanvraag FOREIGN KEY ( id ) REFERENCES groep_64.aanvraag( id )   ,
	CONSTRAINT fk_statusveranderaar_medewerker FOREIGN KEY ( personeelsnummer ) REFERENCES groep_64.medewerker( personeelsnummer )   
 );

ALTER TABLE groep_64.statusveranderaar ADD CONSTRAINT cns_statusveranderaar_datum CHECK ( ((datum > '2014-01-01'::date) AND (datum < date(now()))) );

CREATE  TABLE groep_64.taak ( 
	typenaam             varchar(21)  NOT NULL  ,
	id                   char(8)  NOT NULL  ,
	geschatte_onkosten   numeric  NOT NULL  ,
	geschat_aantal_uren  integer  NOT NULL  ,
	taak_id              char(8)  NOT NULL  ,
	rate_id              char(3)  NOT NULL  ,
	CONSTRAINT pk_taak PRIMARY KEY ( taak_id ),
	CONSTRAINT fk_taak_project FOREIGN KEY ( id ) REFERENCES groep_64.project( id )   ,
	CONSTRAINT fk_taak_rate_taak FOREIGN KEY ( rate_id ) REFERENCES groep_64.rate_taak( rate_id )   ,
	CONSTRAINT fk_taak_type_dienst FOREIGN KEY ( typenaam ) REFERENCES groep_64.type_dienst( typenaam )   
 );

CREATE  TABLE groep_64.utm_media_archive_item ( 
	naam                 varchar(150)  NOT NULL  ,
	id                   char(8)  NOT NULL  ,
	beschrijving         varchar(400)  NOT NULL  ,
	datum_upload         date  NOT NULL  ,
	bestandstype         varchar(60)  NOT NULL  ,
	bestandsgrootte_bytes bigint  NOT NULL  ,
	url                  varchar(300)  NOT NULL  ,
	vertrouwelijk        boolean  NOT NULL  ,
	CONSTRAINT "pk_utm_media_archive-item" PRIMARY KEY ( naam ),
	CONSTRAINT "fk_utm_media_archive-item_project" FOREIGN KEY ( id ) REFERENCES groep_64.project( id )   
 );

CREATE  TABLE groep_64.ingeplande_medewerker_taak ( 
	taak_id              char(8)  NOT NULL  ,
	personeelsnummer     char(8)  NOT NULL  ,
	week                 date  NOT NULL  ,
	aantal_uren          integer  NOT NULL  ,
	CONSTRAINT "pk_ingeplande medewerker taak" PRIMARY KEY ( taak_id, personeelsnummer, week ),
	CONSTRAINT "fk_ingeplande medewerker taak_medewerker" FOREIGN KEY ( personeelsnummer ) REFERENCES groep_64.medewerker( personeelsnummer )   ,
	CONSTRAINT "fk_ingeplande medewerker taak_taak" FOREIGN KEY ( taak_id ) REFERENCES groep_64.taak( taak_id )   
 );

ALTER TABLE groep_64.ingeplande_medewerker_taak ADD CONSTRAINT cns_ingeplande_medewerker_taak_week CHECK ( ((EXTRACT(dow FROM week) = (1)::numeric) AND (week > '2014-01-01'::date)) );

CREATE  TABLE groep_64.label_van_utmma_item ( 
	naam                 varchar(150)  NOT NULL  ,
	label                varchar(100)  NOT NULL  ,
	CONSTRAINT "pk_label_van_utmma-item" PRIMARY KEY ( naam, label ),
	CONSTRAINT "fk_label_van_utmma-item_label" FOREIGN KEY ( label ) REFERENCES groep_64.label( label )   ,
	CONSTRAINT "fk_label_van_utmma-item_utm_media_archive-item" FOREIGN KEY ( naam ) REFERENCES groep_64.utm_media_archive_item( naam )   
 );

CREATE  TABLE groep_64.medewerker_in_utmma_item ( 
	personeelsnummer     char(8)  NOT NULL  ,
	naam                 varchar(150)  NOT NULL  ,
	CONSTRAINT "pk_medewerker_in_utmma-item" PRIMARY KEY ( personeelsnummer, naam ),
	CONSTRAINT "fk_medewerker_in_utmma-item_medewerker" FOREIGN KEY ( personeelsnummer ) REFERENCES groep_64.medewerker( personeelsnummer )   ,
	CONSTRAINT "fk_medewerker_in_utmma-item_utm_media_archive-item" FOREIGN KEY ( naam ) REFERENCES groep_64.utm_media_archive_item( naam )   
 );

CREATE  TABLE groep_64.medewerker_taak ( 
	taak_id              char(8)  NOT NULL  ,
	personeelsnummer     char(8)  NOT NULL  ,
	CONSTRAINT pk_medewerker_taak PRIMARY KEY ( taak_id, personeelsnummer ),
	CONSTRAINT fk_medewerker_taak_medewerker FOREIGN KEY ( personeelsnummer ) REFERENCES groep_64.medewerker( personeelsnummer )   ,
	CONSTRAINT fk_medewerker_taak_taak FOREIGN KEY ( taak_id ) REFERENCES groep_64.taak( taak_id )   
 );

CREATE  TABLE groep_64.registreerder_taakprestaties ( 
	taak_id              char(8)  NOT NULL  ,
	personeelsnummer     char(8)  NOT NULL  ,
	aantal_uren          integer  NOT NULL  ,
	datum                date  NOT NULL  ,
	"opmerking-uren"     varchar(400)    ,
	beschrijving_kosten  varchar(400)    ,
	kosten               numeric    ,
	CONSTRAINT pk_registreerder_taakprestaties PRIMARY KEY ( taak_id, personeelsnummer, datum ),
	CONSTRAINT fk_registreerder_taakprestaties_medewerker FOREIGN KEY ( personeelsnummer ) REFERENCES groep_64.medewerker( personeelsnummer )   ,
	CONSTRAINT fk_registreerder_taakprestaties_taak FOREIGN KEY ( taak_id ) REFERENCES groep_64.taak( taak_id )   
 );

ALTER TABLE groep_64.registreerder_taakprestaties ADD CONSTRAINT cns_registreerder_taakprestaties_datum CHECK ( ((datum > '2014-01-01'::date) AND (datum < date(now()))) );

ALTER TABLE groep_64.registreerder_taakprestaties ADD CONSTRAINT cns_registreerder_taakprestaties_prestaties CHECK ( (((kosten IS NOT NULL) AND (beschrijving_kosten IS NOT NULL)) OR ((kosten IS NULL) AND (beschrijving_kosten IS NULL))) );
