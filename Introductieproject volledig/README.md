# Getting started

## Downloaden challenges

- Maak op je laptop een directory aan voor het introductieproject, bv. `C:\introductieproject`.
- Open een consolevenster in deze directory.
  - Windows: open Windows Explorer/Verkenner, ga naar de folder, rechterklik en kies "Git Bash Here".
  - MacOS: bekijk dit [filmpje](https://www.youtube.com/watch?v=xsCCgITrrWI). Je kan ook vragen om hulp aan de lector.

Voer vervolgens de volgende commando's in.

**MERK OP: Enkel de regels die beginnen op `$` moet je zelf ingeven.**

**De `$` zelf hoef je niet in te geven, die wijst op een console commando!**

```bash
#<URL> = de link je persoonlijke GitHub classroom, verkregen door het accepteren van de Classroom Assignment
#Vergeet het punt niet op het einde van git clone!
$ git clone <URL> .
Cloning into '.'...
warning: You appear to have cloned an empty repository.

$ git remote add upstream https://github.com/ucll-introductieproject/student-challenges

$ git remote -v
origin  <URL> (fetch)
origin  <URL> (push)
upstream        https://github.com/ucll-introductieproject/student-challenges (fetch)
upstream        https://github.com/ucll-introductieproject/student-challenges (push)

$ git pull upstream master
remote: Enumerating objects: 174, done.
remote: Counting objects: 100% (174/174), done.
remote: Compressing objects: 100% (91/91), done.
remote: Total 174 (delta 91), reused 158 (delta 80), pack-reused 0
Receiving objects: 100% (174/174), 1.24 MiB | 9.56 MiB/s, done.
Resolving deltas: 100% (91/91), done.
From https://github.com/ucll-introductieproject/student-challenges
 * branch            master     -> FETCH_HEAD
 * [new branch]      master     -> upstream/master

$ git push -u origin master
Enumerating objects: 174, done.
Counting objects: 100% (174/174), done.
Delta compression using up to 16 threads
Compressing objects: 100% (80/80), done.
Writing objects: 100% (174/174), 1.24 MiB | 1.32 MiB/s, done.
Total 174 (delta 91), reused 174 (delta 91), pack-reused 0
remote: Resolving deltas: 100% (91/91), done.
To URL
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

## Opstarten challenges

- We starten nu via Python een lokale web server:

```bash
$ python -m http.server
```

- Surf in de browser nu naar http://localhost:8000/overview.html. Hier krijg je een overzicht van alle challenges.
- De eerste challenge waar je aan moet beginnen is "Git" - "Basics". Volg de instructies die hier beschreven staan.

## Updaten challenges

Doorheen het semester zullen nieuwe challenges gepubliceerd worden. Om deze in jouw repository te synchroniseren voer je onderstaande commando's uit.

**Belangrijk: voordat je dit doet zorg je best dat je geen uitgaande wijzigingen hebt, om merge conflicten te voorkomen. Doe dus eerst een git commit en git push van je meest recente wijzingen.**

```bash
$ git pull upstream master
$ git push
```
