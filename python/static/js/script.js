// function getCookie(name) {
//   let cookieValue = null;
//   if (document.cookie && document.cookie !== "") {
//     const cookies = document.cookie.split(";");
//     for (let i = 0; i < cookies.length; i++) {
//       const cookie = cookies[i].trim();
//       if (cookie.startsWith(name + "=")) {
//         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//         break;
//       }
//     }
//   }
//   return cookieValue;
// }

document.addEventListener("DOMContentLoaded", () => {
  let form = document.querySelector("form");
  console.log("Event listener added");
  console.log(form);
  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    let movieInput = document.getElementById("movie-input");

    if (!movieInput.value) {
      console.log("please enter a movie title");
    } else {
      let movieName = movieInput.value;
      console.log(movieName);
      // Launch the scraping file
      try {
        console.log("test");
        const response = await fetch("/movies/", {
          method: "POST",
          body: JSON.stringify({ movieName }),
          headers: {
            "Content-Type": "application/json",
            //"X-CSRFToken": getCookie("csrftoken"),
          },
        });
        if (response.ok) {
          const data = await response.json();
          console.log(data);
        } else {
          console.error("Error:", response.status);
        }
        // console.log(response.body);
        console.log("done !");
        // Handle the response from your Express app
      } catch (error) {
        console.error("Error:", error);
      }
    }
  });
});
