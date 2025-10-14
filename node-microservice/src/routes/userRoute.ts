import { prisma } from "@/utils/prismaClient";
import express from "express";

const router = express.Router();

router.post("/new-user", async (req, res) => {
  try {
    const {
      name,
      email,
      phone,
      country,
      gender,
      profilePicture,
      role,
      age,
      university,
      company,
      title,
      department,
      address,
      state,
      city,
      status,
    } = req.body;
    const newUser = await prisma.user.create({
      data: {
        name,
        email,
        phone,
        country,
        gender,
        profilePicture,
        role,
        age,
        university,
        company,
        title,
        department,
        address,
        state,
        city,
        status,
      },
    });
    res
      .status(200)
      .json({ message: "User created successfully", data: newUser });
  } catch (error) {
    res.status(500).json({ message: error });
  }
});

router.get("/all-users", async (req, res) => {
  try {
    const allUsers = await prisma.user.findMany({
      where: { isDeleted: false },
    });
    res
      .status(200)
      .json({ message: "All users fetched successfully", data: allUsers });
  } catch (error) {
    res.status(500).json({ message: error });
  }
});

router.get("/get-user/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const userFound = await prisma.user.findUnique({
      where: { id: parseInt(id), isDeleted: false },
    });
    if (userFound) {
      res
        .status(200)
        .json({ message: "User fetched successfully", data: userFound });
    } else {
      res.status(404).json({ message: "User not found" });
    }
  } catch (error) {
    res.status(500).json({ message: error });
  }
});

router.put("/update-user/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const {
      name,
      email,
      phone,
      country,
      gender,
      profilePicture,
      role,
      age,
      university,
      company,
      title,
      department,
      address,
      state,
      status,
      city,
    } = req.body;
    const userToUpdate = await prisma.user.update({
      where: { id: parseInt(id), isDeleted: false },
      data: {
        name,
        email,
        phone,
        country,
        gender,
        profilePicture,
        role,
        age,
        university,
        company,
        title,
        department,
        address,
        state,
        status,
        city,
      },
    });
    res
      .status(200)
      .json({ message: "User updated successfully", data: userToUpdate });
  } catch (error) {
    res.status(500).json({ message: error });
  }
});

router.delete("/delete-user/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const userDelete = await prisma.user.update({
      where: { id: parseInt(id), isDeleted: false },
      data: { isDeleted: true, deletedAt: new Date() },
    });
    res
      .status(200)
      .json({ message: "User deleted successfully", data: userDelete });
  } catch (error) {
    res.status(500).json({ message: error });
  }
});

export default router;
