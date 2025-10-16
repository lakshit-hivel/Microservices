import jwt from "jsonwebtoken";
import dotenv from "dotenv";
import express from "express";
import { prisma } from "@/utils/prismaClient";

dotenv.config({ path: "./.env" });
const router = express.Router();

const generateToken = (id: number) => {
  return jwt.sign({ id }, process.env.JWT_SECRET as string, {
    expiresIn: "1000h",
  });
};

router.post("/register", async (req, res) => {
  const { email, username, password } = req.body;
  try {
    if (await prisma.authUser.findUnique({ where: { email } }))
      return res.status(400).json({ message: "Email already exists" });
    const newUser = await prisma.authUser.create({
      data: { email, username, password },
    });
    const token = generateToken(newUser.id);
    res.status(200).json({ message: "User created successfully", token });
  } catch (error) {
    res.status(500).json({ message: error });
  }
});

router.post("/login", async (req, res) => {
  const { username, password } = req.body;
  try {
    const user = await prisma.authUser.findUnique({ where: { username } });
    if (!user) return res.status(400).json({ message: "User not found" });
    if (user.password !== password)
      return res.status(400).json({ message: "Invalid password" });
    const token = generateToken(user.id);
    res.status(200).json({ message: "Login successful", token });
  } catch (error) {
    res.status(500).json({ message: error });
  }
});

export default router;
