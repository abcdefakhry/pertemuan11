require("dotenv").config();

const express = require("express");
const axios = require("axios");

const app = express();

app.use(express.json());

app.get("/health", (req, res) => {

  res.json({
    status: "success",
    message: "Node Service aktif"
  });
});

app.post("/api/obesity/predict", async (req, res) => {

  try {
    const response = await axios.post(
      `${process.env.PYTHON_API}/predict`,
      req.body,
      {
        timeout: 5000
      }
    );
    res.json({
      service: "Node.js API Gateway",
      ml_response: response.data
    });
  } catch (error) {
    if (error.code === "ECONNREFUSED") {
      return res.status(503).json({
        status: "error",
        message: "Python ML Service tidak tersedia"
      });
    }
    res.status(500).json({
      status: "error",
      message: error.message
    });
  }
});

app.listen(process.env.PORT, () => {

  console.log(`Node Service berjalan di port ${process.env.PORT}`);

});
