const citaten = [
  {
    titel: 'foolish',
    citaat: 'Stay hungry, stay foolish.',
    auteur: 'Steve Jobs',
    taal: 'en'
  },
  {
    titel: 'count days',
    citaat: "Don't count the days, make the days count.",
    auteur: 'Muhammad Ali',
    taal: 'en'
  },
  {
    titel: 'overwinnen',
    citaat: 'Veni, vidi, vici.',
    auteur: 'Julius Caesar',
    taal: 'la'
  },
  {
    titel: 'schatbewaarder',
    citaat: 'De Vlamingen zijn de schatbewaarders van de Nederlandse taal',
    auteur: 'Jan de Hartog',
    taal: 'nl'
  },
  {
    titel: 'vandaag',
    citaat: 'Wat je vandaag moet doen, moet je doen zoals je morgen denkt dat je het had moeten doen.',
    auteur: 'Toon Hermans',
    taal: 'nl'
  },
  {
    titel: 'humor',
    citaat: 'Gevoel voor humor begint bij gevoel voor verdriet.',
    auteur: 'Toon Hermans',
    taal: 'nl',
  },
  {
    titel: 'aimer',
    citaat: "Le verbe aimer est difficile à conjuguer : son passé n'est pas simple, son présent n'est qu'indicatif, et son futur est toujours conditionnel.",
    auteur: 'Jean Cocteau',
    taal: 'fr'
  },
  {
    titel: 'équipe',
    citaat: "Les performances individuelles, ce n'est pas le plus important. On gagne et on perd en équipe.",
    auteur: 'Zinedine Zidane',
    taal: 'fr'
  }

];

// hier komt de rest van je JS code voor vragen 1, 2 en 3

// VRAAG 1

const citaten_weergeven = (citatenlijst, langecitaten = false) => {

  const citaten_section = document.querySelector("section.citaten");

  citaten_section.innerHTML = '';

  if (langecitaten) {

    document.querySelector('h1').innerText = 'Beroemde citaten (meer dan 50 karakters)';

  };

  citatenlijst
  .filter((citaat) => langecitaten ? citaat.citaat.length > 50 : true)
  .forEach((citaat) => {

    const citaat_article = document.createElement("article");

    const citaat_titel = document.createElement("h2");
    citaat_titel.innerText = citaat.titel;

    const citaat_tekst = document.createElement("p");
    citaat_tekst.innerText = citaat.citaat;

    const citaat_auteur = document.createElement("p");
    citaat_auteur.innerText = `- ${citaat.auteur}`;

    citaat_article.appendChild(citaat_titel);
    citaat_article.appendChild(citaat_tekst);
    citaat_article.appendChild(citaat_auteur);

    citaten_section.appendChild(citaat_article);
    
  });
};

citaten_weergeven(citaten);

// VRAAG 2

const lange_citaten_button = document.getElementById("langeCitaten");

lange_citaten_button.addEventListener("click", () => citaten_weergeven(citaten, true));

// VRAAG 3

const formulier = document.querySelector("form");

const div_feedback = document.getElementById("feedback");

formulier.addEventListener("submit", (event) => {
  event.preventDefault();

  div_feedback.innerHTML = '';

  const error_lijst = [];

  const titel_formulier = document.getElementById("titel").value;

  const citaat_formulier = document.getElementById("citaat").value;

  const auteur_formulier = document.getElementById("auteur").value;

  const taal_formulier = document.getElementById("taal").value;

  // In het filmpje wordt maximaal 1 error weergegeven maar deze code kan ze beide tonen, bv. in het geval dat auteur niet ingevuld is en het citaat wel, maar dit is geen minimaal 10 karakters lang. Ik heb dit nagevraagd bij meneer Van Hee en hij zei dat ik dit mocht gebruiken.

  if (!titel_formulier || !citaat_formulier || !auteur_formulier || !taal_formulier){
    error_lijst.push("Fout: niet alle velden ingevuld!");
  };

  if (citaat_formulier && citaat_formulier.length < 10){
    error_lijst.push("Fout: citaat moet minstens 10 letters lang zijn!");
  };

  if (error_lijst.length > 0){
    error_lijst.forEach((error) => {
      div_feedback.innerHTML += `<p>${error}</p>`
    });
  }
  else{
    citaten.push({
      titel: `${titel_formulier}`,
      citaat: `${citaat_formulier}`,
      auteur: `${auteur_formulier}`,
      taal: `${taal_formulier}`
    });

    citaten_weergeven(citaten);

    div_feedback.innerHTML = '<p>Nieuw citaat toegevoegd.</p>';

  };

});
