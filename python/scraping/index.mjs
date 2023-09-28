import express from "express";
import dotenv from "dotenv";
import axios from "axios";

import {
  connection,
  MovieID,
  Review,
  disconnectFromDatabase,
} from "./database.mjs";
import { fetchData } from "./getMovie.mjs";

dotenv.config();

const app = express();
app.use(express.json());

app.post("/movies/", async (req, res) => {
  try {
    console.log("post request received!");
    //console.log(req.body);
    const movieName = req.body.movieName;
    console.log("name", req.body);
    await fetchData(axios, movieName);
    res.status(200).send("Movie data fetched successfully!");
  } catch (err) {
    console.log(err);
    res.status(500).send("Internal Server Error");
  }
});

// fetchData(axios);

app.listen(3000, () => {
  console.log("Server started on port 3000");
});
