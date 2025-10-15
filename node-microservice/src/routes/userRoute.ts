import { authMiddleware } from "@/middlewares/auth.middleware";
import { prisma } from "@/utils/prismaClient";
import express from "express";

const router = express.Router();

// Create a new user
router.post("/new-user", authMiddleware, async (req, res) => {
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
      },
    });
    res
      .status(200)
      .json({ message: "User created successfully", data: newUser });
  } catch (error) {
    res.status(500).json({ message: error });
  }
});

// Get all users
router.get("/all-users", authMiddleware, async (req, res) => {
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

// Get all deleted users
router.get("/all-deleted-users", authMiddleware, async (req, res) => {
  try {
    const allUsers = await prisma.user.findMany({
      where: { isDeleted: true },
    });
    res.status(200).json({
      message: "All deleted users fetched successfully",
      data: allUsers,
    });
  } catch (error) {
    res.status(500).json({ message: error });
  }
});

// Get user by id
router.get("/get-user/:id", authMiddleware, async (req, res) => {
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

// Update user
router.put("/update-user/:id", authMiddleware, async (req, res) => {
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

// Restore User
router.put("/restore-user/:id", authMiddleware, async (req, res) => {
  try {
    const { id } = req.params;
    const uerToRestore = await prisma.user.update({
      where: { id: parseInt(id) },
      data: { isDeleted: false, deletedAt: null },
    });
    res
      .status(200)
      .json({ message: "User restored successfully", data: uerToRestore });
  } catch (error) {
    res.status(500).json({ message: error });
  }
});

// Soft delete user
router.delete("/delete-user/:id", authMiddleware, async (req, res) => {
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
