import rateLimit from "express-rate-limit";

export const limiter = rateLimit({
  windowMs: 1 * 60 * 1000,
  max: 100,
  message: "Too many requests from this IP, please try again after 1 minute",
});
