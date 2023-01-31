/* 1. Aanvragen: geef een overzicht van de verschillende type diensten die we aanbieden,
waarbij voor elke status waarin een aanvraag zich kan bevinden, een kolom getoond
wordt met het aantal aanvragen in die desbetreffende status. Zorg ervoor dat er enkel
de aantallen voor het huidig jaar getoond worden. De filter op jaar mag niet hard-coded
zijn. De lijst wordt gesorteerd volgens de volgende volgorde: ‘Leveren van expertise’,
‘Uitwerken van media’ en ‘Coachen en begeleiden’. */

SELECT  A.typenaam, T.huidige_status, count(*) AS aantal_aanvragen
FROM groep_64.aanvraag AS T INNER JOIN groep_64.aanvraag_voor_type_dienst AS A ON T.id = A.id
WHERE EXTRACT(YEAR FROM T.aanvraagdatum) = EXTRACT(YEAR FROM Date(NOW()))
GROUP BY A.typenaam, T.huidige_status
ORDER BY
CASE
	WHEN A.typenaam = 'Leveren van expertise' THEN '1'
	WHEN A.typenaam = 'Uitwerken van media' THEN '2'
	ELSE '3'
END

/* 2. Planning medewerker: geef het overzicht van het aantal ingepland uren voor een
bepaalde medewerker waarbij er een opdeling gemaakt wordt over de verschillende
projecten. Elk project vormt een rij van het overzicht. Per week voorzien we 2 kolommen,
een eerste kolom geeft het aantal ingeplande uren van de werknemer in die week,
de twee kolom geeft het percentage weer van deze uren in de totale capaciteit van
de werknemer. We willen het overzicht voor de 5 volgende weken. Sorteer de rijen
alfabetisch volgend de naam van de projecten. */

SELECT P.projectnaam, I.week, I.aantal_uren, CAST((CAST(I.aantal_uren AS NUMERIC) / CAST(M.capaciteit AS NUMERIC) * 100) AS NUMERIC(4,2)) || '%' AS percentage
FROM groep_64.taak AS T 
INNER JOIN (groep_64.ingeplande_medewerker_taak AS I INNER JOIN groep_64.medewerker AS M ON I.personeelsnummer = M.personeelsnummer) ON T.taak_id = I.taak_id
INNER JOIN groep_64.project AS P ON T.id = P.id
WHERE I.personeelsnummer = 'r7390462' AND I.week > DATE(NOW()) AND I.week <= DATE(NOW()) + 35
ORDER BY 1,2

/* 3. Project: planned vs actuals: voor elk project in status ‘Planned and ongoing’ willen
we een overzicht van de ingeschatte kost en de (huidige) reële kost. Voor elke categorie (ingeschat vs reëel) willen we een kolom ‘Aantal uren’, ‘Rate’, ‘Kost aantal uren’
en ‘Onkosten’. Voor elk project willen we telkens de naam van het project weten, de
verantwoordelijke medewerker (voornaam + achternaam), de startdatum en einddatum, gevolgd door de informatie van projectkosten. Zet de projecten met de vroegste
einddatum bovenaan, dit mag ook een datum in het verleden zijn. */

SELECT P.projectnaam, M.voornaam || ' ' || M.achternaam as naam_verantwoordelijke, P.startdatum, P.einddatum, SUM(DISTINCT T.geschat_aantal_uren) AS geschat_aantal_uren , IJ.rate AS geschatte_rate, SUM(DISTINCT T.geschat_aantal_uren) * IJ.rate AS geschatte_kost_uren, CAST(SUM(DISTINCT T.geschatte_onkosten) AS NUMERIC(10,2)) AS geschatte_onkosten, SUM(RTP.aantal_uren) AS reëel_aantal_uren, CAST(AVG(RT.rate) AS NUMERIC(4,2)) AS reële_rate, CAST(SUM(RTP.aantal_uren) * AVG(RT.rate) AS NUMERIC(10,2)) AS reële_kost_uren, SUM(RTP.kosten) AS reëele_onkosten
FROM groep_64.project AS P 
INNER JOIN groep_64.taak AS T 
			INNER JOIN groep_64.rate_taak AS RT ON T.rate_id = RT.rate_id
			INNER JOIN groep_64.registreerder_taakprestaties AS RTP ON T.taak_id = RTP.taak_id
		ON P.id = T.id
INNER JOIN groep_64.medewerker AS M ON M.personeelsnummer = P.verantwoordelijke_medewerker
INNER JOIN groep_64.rate_algemene_werking AS IJ ON P.inschattingsjaar = IJ.inschattingsjaar
WHERE P.status = 'planned and ongoing'
GROUP BY P.id, T.id, M.personeelsnummer, IJ.rate
ORDER BY 4
 
/* 4. UTM Media Archive: geef een overzicht van de beschikbare video’s in het UTM Media
Archive die voor een opleiding binnen UCLL werden gecreëerd en gelabeld werden met
‘Afstandsonderwijs’. Geef voor elke video de naam van het bestand, de URL, de datum
waarop het opgeladen werd en de opleiding waarvoor de video werd gemaakt. Sorteer
zodat de meest recente video’s bovenaan getoond worden. */

SELECT U.naam, U.url, U.datum_upload as uploaddatum, P.naam_klant AS opleiding
FROM groep_64.utm_media_archive_item AS U
INNER JOIN groep_64.label_van_utmma_item AS L ON U.naam = L.naam
INNER JOIN groep_64.project AS P ON U.id = P.id
WHERE L.label = 'afstandsonderwijs' AND P.naam_klant LIKE '%Opleiding%' AND U.bestandstype = 'video'
ORDER BY 3 DESC

/* 5. Klanten: geef het overzicht van de klanten waar we het afgelopen jaar voor gewerkt
hebben. Voor elke klant waarvoor we het afgelopen jaar hebben gewerkt (met ‘gewerkt’
bedoelen we een project gestart), willen we een overzicht van het aantal aanvragen,
aantal projecten (met bijkomende kolommen voor aantal projecten in status ‘Planned
and ongoing’ en status ‘Delivered’), bedrag van de openstaande facturen, het totaal van
de facturen voor het afgelopen jaar en het totaal van de facturen over de verschillende
jaren heen. De lijst moet gesorteerd worden zodat de klant met het hoogste totale
bedrag van facturen voor het afgelopen jaar bovenaan komt te staan. */

SELECT K.naam_klant, COUNT(A.id) AS aanvragen, COUNT(P1.id) AS projecten, COUNT(CASE P1.status WHEN 'planned and ongoing' THEN 1 ELSE NULL end) AS planned_and_ongoing, COUNT(CASE P1.status WHEN 'delivered' THEN 1 ELSE NULL end) AS delivered, SUM(CASE P1.status WHEN 'delivered' THEN P1.factuur ELSE 0 end) AS factuur_open, SUM(CASE WHEN P1.einddatum > DATE(NOW()) - 365 THEN P1.factuur ELSE 0 end) AS factuur_jaar, SUM(CASE WHEN P1.factuur IS NOT NULL THEN P1.factuur ELSE 0 END) AS factuur_totaal
FROM groep_64.klant AS K
INNER JOIN (groep_64.aanvraag AS A LEFT OUTER JOIN groep_64.project AS P1 ON A.id = P1.id) ON K.naam_klant = A.naam_klant
GROUP BY K.naam_klant
HAVING MAX(P1.einddatum) > DATE(NOW()) - 365 
ORDER BY 8 DESC