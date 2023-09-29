function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Check if the cookie name matches the provided name
      if (cookie.substring(0, name.length + 1) === name + "=") {
        // Extract the cookie value
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

document.addEventListener("DOMContentLoaded", () => {
  let form = document.querySelector("form");
  console.log("Event listener added");
  console.log(form);
  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    let movieInput = document.getElementById("movie-input");
    if (!movieInput.value) {
      console.log("Please enter a movie title");
    } else {
      let movieName = movieInput.value;
      console.log(movieName);

      // Get the CSRF token from the cookie
      const csrftoken = getCookie("csrftoken");

      // Launch the scraping file
      try {
        const url = "http://localhost:3000/movies/";
        const response = await fetch(url, {
          method: "POST",
          body: JSON.stringify({ movieName }),
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken, // Include the CSRF token in the request headers
          },
        });
        if (response.ok) {
          const data = await response.json();
          console.log(data);
        }
        console.log("done !");
      } catch (error) {
        console.error("Error:", error);
      }

      // Send a POST request to your Django app to navigate to a new page
      try {
        const djangoUrl = "/movies/";
        const djangoResponse = await fetch(djangoUrl, {
          method: "POST",
          body: new URLSearchParams({ movie_name: movieName }),
          headers: {
            "X-CSRFToken": csrftoken, // Include the CSRF token in the request headers
          },
        });
        if (djangoResponse.ok) {
          console.log("Navigating to new page");
          window.location.href = "/movies/results/";
        }
      } catch (error) {
        console.error("Error:", error);
      }
    }
  });
});
