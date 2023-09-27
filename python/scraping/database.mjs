import mongoose from "mongoose";

//connection to the db
const connection = async () => {
  try {
    await mongoose.connect(process.env.CONNECTION_STRING, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log("Connecting to MongoDB...");
    console.log("Connection successful!");

    // Rest of your code
  } catch (error) {
    console.error("Error connecting to MongoDB:", error);
  }
};

const moviereviews = new mongoose.Schema({
  reviewText: String,
});

const Review = mongoose.model("Review", moviereviews);

const movieData = new mongoose.Schema({
  movieName: String,
  movieID: String,
});

const MovieID = mongoose.model("MovieID", movieData, "movieids");

const disconnectFromDatabase = async () => {
  try {
    await mongoose.disconnect();
    console.log("Disconnected from MongoDB");
  } catch (error) {
    console.error("Error disconnecting from MongoDB:", error);
  }
};

export { connection, Review, MovieID, disconnectFromDatabase };
