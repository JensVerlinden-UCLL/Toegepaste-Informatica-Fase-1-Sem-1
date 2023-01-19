// hier komt de JS code voor vraag 4

const button_gta = document.getElementById("spel1");

const button_hfw = document.getElementById("spel2");

const ul_lijst = document.querySelector("ul");

const counter_titel = document.getElementById("aantalKliks");

let counter = 0;

const createLi = () => document.createElement('li');

const knop_klikker = async (knop) => {

    const response = await fetch(`http://localhost:3000/games/name/${knop.innerText}`); 
    const result = await response.json(); 

    ul_lijst.innerHTML = '';

    const id_li = createLi();
    id_li.innerText = `id: ${result.id}`;

    const naam_li = createLi();
    naam_li.innerText = `naam: ${result.name}`;

    const type_li = createLi();
    type_li.innerText = `type: ${result.type}`;

    const waardering_li = createLi();
    waardering_li.innerText = `waardering: ${result.rating}`;

    const favoriet_li = createLi();
    favoriet_li.innerText = `favoriet: ${result.isFavourite}`;

    ul_lijst.appendChild(id_li);
    ul_lijst.appendChild(naam_li);
    ul_lijst.appendChild(type_li);
    ul_lijst.appendChild(waardering_li);
    ul_lijst.appendChild(favoriet_li);

    counter++;

    counter_titel.innerText = `Aantal keren op een knop gedrukt = ${counter}`;
};

button_gta.addEventListener("click", () => knop_klikker(button_gta));

button_hfw.addEventListener("click", () => knop_klikker(button_hfw));