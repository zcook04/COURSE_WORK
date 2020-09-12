const express = require('express');
const path = require('path');
const dotenv = require('dotenv');
const morgan = require('morgan');
const colors = require('colors');
const errorHandler = require('./middleware/error');
const connectDB = require('./config/db');

// LOAD ENV VARIABLES
dotenv.config({
  path: path.resolve(__dirname + '/config/config.env'),
});

// CONNECT TO DB
connectDB();

// ROUTES
const bootcamps = require('./routes/bootcamps');

const app = express();

// BODY PARSER
app.use(express.json());

// DEV LOGGING MIDDELWAWRE
if (process.env.NODE_ENV === 'development') {
  app.use(morgan('dev'));
}

// MOUNT ROUTERS
app.use('/api/v1/bootcamps', bootcamps);

app.use(errorHandler);

const PORT = process.env.PORT || 5000;

const server = app.listen(PORT, () =>
  console.log(
    `Server running in ${process.env.NODE_ENV} mode on port ${PORT}`.yellow.bold
  )
);

// HANDLE UNHANDLED PROMISE REJECTIONS
process.on('unhandledRejection', (err, promise) => {
  console.log(`Error: ${err.message}`.red);
  // CLOSE SERVER AND EXIT PROCESS
  server.close(() => process.exit(1));
});
