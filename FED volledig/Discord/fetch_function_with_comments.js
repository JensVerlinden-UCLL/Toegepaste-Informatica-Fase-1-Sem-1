/**
 * @typedef {"GET" | "POST" | "PUT" | "DELETE"} Method
 * 
 * @typedef {Object} RequestOptions
 * @property {Method?} method the fetch method to execute.
 * @property {Object?} data the data to send along with the request.
 * @property {string?} query the query to append at the back of the url.
 * @property {string?} header extra header options.
 */

/**
 * @typedef {Object} Game
 * @property {string} name the name of the game.
 * @property {string} type the genre of the game.
 * @property {number} rating the rating of the game.
 */

/**
 * Simple request function.
 * 
 * Example:
 * ```
 * const json = await request("/games", { method: "GET" });
 * const json = await request("/games/filter", { method: "GET", query: "Dying Light 2" });
 * const json = await request("/games/44ebb4f6-3f64-4b11-a98f-e35469507318", { method: "DELETE" });
 * const json = await request("/games", { method: "POST", data: { name: "A generic game", type: "Generic", rating: 5 } });
 * ```
 * 
 * @param {string} path the path to send the request to.
 * @param {RequestOptions?} options options for the request.
 */
const request = (path, { method, headers, data, query }={}) => {

    let url = "http://localhost:3000" + path; // Change hostname if necessery
    
    if (query) {
        url += "?" + new URLSearchParams({ query });
    }

    return fetch(url, {
        method: method || "GET",
        headers: Object.assign({}, {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }, headers || {}),
        body: JSON.stringify(data)
    });
};

/**
 * Fetch games with a query.
 * 
 * Query is not case sensitive so query = "Elden" will have the same result as "ELDEN" or "elden" ...
 * 
 * Example:
 * ```
 * const games = await fetchGamesWithQuery("Hitman 3");
 * ```
 * 
 * @param {string} query is not case sensitive so query = "Elden" will have the same result as "ELDEN" or "elden" ...
 */
const fetchGamesWithQuery = async (query) => {
    const res = await request("/games/filter", { query });
    return res.json();
};

/**
 * Fetch all games.
 * 
 * Example:
 * ```
 * const games = await fetchAllGames(); // Fetches all games.
 * ```
 */
const fetchAllGames = async () => {
    const res = await request("/games");
    return res.json();
};

/**
 * Fetch all games or certain games using a search query by name.
 * 
 * Example:
 * ```
 * const games = await fetchGames(); // Without a search query.
 * const games = await fetchGames("Destiny 2"); // With a search query.
 * ```
 * 
 * @param {string?} query is not case sensitive so query = "Elden" will have the same result as "ELDEN" or "elden" ...
 */
const fetchGames = (query) => {
    if (query) {
        return fetchGamesWithQuery(query);
    }
    return fetchAllGames();
};

/**
 * Adds a game.
 * 
 * Example:
 * ```
 * const res = await addGame({ name: "Random game", type: "Generic", rating: 5 });
 * ```
 * 
 * @param {Game} game the game to add.
 */
const addGame = async (game) => {
    const res = await request("/games", {
        method: "POST",
        data: game
    });
    return res.json();
};

/**
 * Fetch a game by name.
 * 
 * Example:
 * ```
 * const game = await fetchGameByName("Elden Ring");
 * ```
 * 
 * @param {string} name the name of the game to fetch.
 */
const fetchGameByName = async (name) => {
    const res = await request(`/games/name/${name}`);
    return res.json();
};

/**
 * Toggle favourite for a game.
 * 
 * Example:
 * ```
 * const res = await toggleFavourite("44ebb4f6-3f64-4b11-a98f-e35469507318");
 * const res = await toggleFavourite(game.id);
 * ```
 * 
 * @param {string} uuid the id of the game to toggle favourite on.
 */
const toggleFavourite = async (uuid) => {
    const res = await request(`/games/${uuid}/favourite`, {
        method: "POST"
    });
    return res.json();
};

/**
 * Set a rating for a game
 * 
 * Example:
 * ```
 * const res = await setRating("44ebb4f6-3f64-4b11-a98f-e35469507318", 5);
 * const res = await setRating(game.id, 3);
 * ```
 * 
 * @param {string} uuid the id of the game to modify the rating on.
 * @param {number} rating the rating to set.
 */
const setRating = async (uuid, rating) => {
    const res = await request(`/games/${uuid}/rating`, {
        method: "POST",
        data: { rating }
    });
    return res.json();
};

/**
 * Remove a game by its uuid.
 * 
 * Example:
 * ```
 * const res = await deleteGame("44ebb4f6-3f64-4b11-a98f-e35469507318");
 * const res = await deleteGame(game.id);
 * ```
 * 
 * @param {string} uuid the id of the game to delete.
 */
const deleteGame = async (uuid) => {
    const res = await request(`/games/${uuid}`, {
        method: "DELETE"
    });
    return res.json();
};

/**
 * Delete all games
 * 
 * Example:
 * ```
 * const res = await deleteAllGames();
 * ```
 */
const deleteAllGames = async () => {
    const res = await request("/games", {
        method: "DELETE",
        headers: {
            "Authorization": "SomeSuperSecretPassword554433!" // Change password if neceserry
        }
    });
    return res.json();
};