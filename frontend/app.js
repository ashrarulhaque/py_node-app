const express = require("express");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();
const PORT = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());


app.get("/", (req, res) => {
  res.send(`
    <h2>Submit Your Data</h2>
    <form method="POST" action="/submit">
        <label>Name:</label>
        <input type="text" name="name" required><br><br>

        <label>Email:</label>
        <input type="email" name="email"><br><br>

        <button type="submit">Submit</button>
    </form>
  `);
});


app.post("/submit", async (req, res) => {
  try {
    const { name, email } = req.body;

    const response = await axios.post("http://backend:5000/submitform", {
      name,
      email
    });

    res.send(`<h3>${response.data.message}</h3>`);
  } catch (error) {
    console.error(error.message);
    res.send("<h3>Error submitting data</h3>");
  }
});

app.listen(PORT, () => {
  console.log(`Frontend running at http://localhost:${PORT}`);
});
