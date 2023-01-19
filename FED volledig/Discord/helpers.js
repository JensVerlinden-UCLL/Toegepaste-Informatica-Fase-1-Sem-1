


const getGames = () => { //functie om games op te halen
    fetchGames("http://localhost:3000/games", "GET", null, true)

}

const getGameByName = (name) => { //functie om game op te halen op naam
    return fetchGames("http://localhost:3000/games/name/" + name, "GET")
}

const addGame = (game) => { //functie om game toe te voegen
    fetchGames("http://localhost:3000/games", "POST", game)
    console.log("addGame: ", game)
}

const deleteGame = (game) => { //functie om game te verwijderen
    if (game == null) return
    if (game == "") return
    fetchGames("http://localhost:3000/games/" + game.id, "DELETE")
}

const deleteAllGames = () => { //functie om alle games te verwijderen
    fetchGames("http://localhost:3000/games", "DELETE")
}

const toggleFavourite = (game) => { //functie om game favoriet te maken
    fetchGames("http://localhost:3000/games/" + game.id + "/favourite", "POST")
}


const setRating = (game, rating) => { //functie om rating te geven
    fetchGames("http://localhost:3000/games/" + game.id + "/rating", "POST", { "rating": rating })
}

const gamesFilter = (query) => { //functie om games te filteren
    return fetchGames("http://localhost:3000/games/filter?query=" + query, "GET")
}

const fetchGames = async (url, method = "GET", body = null, fill = false) => { //functie om games op te halen en te bewerken
    try {
        let respons;
        if (!body) {
            respons = await fetch(
                url,
                {
                    method: method,
                    headers: {
                        Accept: "application/json",
                        "Content-Type": "application/json",
                        "Access-Control-Allow-Origin": "*",
                        "Authorization": "SomeSuperSecretPassword554433!"
                    }
                }
            )
        } else {
            respons = await fetch(
                url,
                {
                    method: method,
                    headers: {
                        Accept: "application/json",
                        "Content-Type": "application/json",
                        "Access-Control-Allow-Origin": "*",
                        "Authorization": "SomeSuperSecretPassword554433!"
                    },
                    body: JSON.stringify(body)
                }
            )
        }
        if (fill) {
            games.length = 0
            const result = await respons.json()
            games.push(...result)
            return
        }
        const result = await respons.json()
        return result


    }
    catch (error) {
        console.log(error)
    }
}
