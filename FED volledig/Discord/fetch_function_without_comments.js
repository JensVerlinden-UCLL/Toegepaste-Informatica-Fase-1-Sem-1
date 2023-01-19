const HOSTNAME = "http://localhost:3000";

const fetchGamesWithQuery = async (query) => {
    const res = await fetch(HOSTNAME + `/games/filter?${new URLSearchParams({ query })}`);
    return res.json();
};

const fetchAllGames = async () => {
    const res = await fetch(HOSTNAME + "/games");
    return res.json();
};

const fetchGames = (query) => {
    if (query) {
        return fetchGamesWithQuery(query);
    }
    return fetchAllGames();
};

const addGame = async (game) => {
    const res = await fetch(HOSTNAME + "/games", {
        method: "POST",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify(game)
    });
    return res.json();
};

const fetchGameByName = async (name) => {
    const res = await fetch(HOSTNAME + `/games/name/${name}`);
    return res.json();
};

const toggleFavourite = async (uuid) => {
    const res = await fetch(HOSTNAME + `/games/${uuid}/favourite`, {
        method: "POST",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    });
    return res.json();
};

const setRating = async (uuid, rating) => {
    const res = await fetch(HOSTNAME + `/games/${uuid}/rating`, {
        method: "POST",
        headers: {
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ rating })
    });
    return res.json();
};

const deleteGame = async (uuid) => {
    const res = await fetch(HOSTNAME + `/games/${uuid}`, {
        method: "DELETE"
    });
    return res.json();
};

const deleteAllGames = async () => {
    const res = await fetch(HOSTNAME + "/games", {
        method: "DELETE",
        headers: {
            "Authorization": "SomeSuperSecretPassword554433!" // Change password if neceserry
        }
    });
    return res.json();
};