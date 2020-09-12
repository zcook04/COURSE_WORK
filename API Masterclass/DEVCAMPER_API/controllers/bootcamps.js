const Bootcamp = require('../models/Bootcamp');
const ErrorResponse = require('../utils/errorResponse');

// @DESC        GET ALL BOOTCAMPS
// @ROUTE       GET /api/v1/bootcamps
// @ACCESS      PUBLIC
exports.getBootcamps = async (req, res, next) => {
  try {
    const bootcamps = await Bootcamp.find();

    res.status(200).json({
      success: true,
      count: bootcamps.length,
      data: bootcamps,
    });
  } catch (err) {
    res.status(400).json({
      success: false,
    });
  }
};

// @DESC        GET SINGLE BOOTCAMP
// @ROUTE       GET /api/v1/bootcamps/:id
// @ACCESS      PUBLIC
exports.getBootcamp = async (req, res, next) => {
  try {
    const bootcamp = await Bootcamp.findById(req.params.id);

    if (!bootcamp) {
      return next(
        new ErrorResponse(`Bootcamp not found with id of ${req.params.id}`, 404)
      );
    }

    res.status(200).json({
      success: true,
      data: bootcamp,
    });
  } catch (err) {
    next(
      new ErrorResponse(`Bootcamp not found with id of ${req.params.id}`, 404)
    );
  }
};

// @DESC        CREATE A SINGLE BOOTCAMP
// @ROUTE       POST /api/v1/bootcamps/:id
// @ACCESS      PRIVATE
exports.createBootcamp = async (req, res, next) => {
  try {
    const bootcamp = await Bootcamp.create(req.body);
    res.status(201).json({
      success: true,
      data: bootcamp,
    });
  } catch (err) {
    res.status(400).json({
      success: false,
      msg: err,
    });
  }
};

// @DESC        UPDATE A SINGLE BOOTCAMP
// @ROUTE       PUT /api/v1/bootcamps/:id
// @ACCESS      PRIVATE
exports.updateBootcamp = async (req, res, next) => {
  try {
    const bootcamp = await Bootcamp.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
      runValidators: true,
    });

    if (!bootcamp) {
      return res.status(400).json({ success: false });
    }

    res.status(200).json({ success: true, data: bootcamp });
  } catch (err) {
    res.status(400).json({
      success: false,
      msg: err,
    });
  }
};

// @DESC        DELETE A SINGLE BOOTCAMP
// @ROUTE       DELETE /api/v1/bootcamps/:id
// @ACCESS      PRIVATE
exports.deleteBootcamp = async (req, res, next) => {
  try {
    const bootcamp = await Bootcamp.findByIdAndDelete(req.params.id);

    if (!bootcamp) {
      return res.status(400).json({ success: false, data: {} });
    }

    res.status(200).json({ success: true });
  } catch (err) {
    res.status(400).json({
      success: false,
      msg: err,
    });
  }
};
