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

// connection();
fetchData(axios);

app.listen(3000, () => {
  console.log("Server started on port 3002");
});
