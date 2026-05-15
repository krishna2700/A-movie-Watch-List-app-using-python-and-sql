import express from "express";
import {
  getSupportedLanguages,
  generateReadme,
  generateReadmeBulk,
  generateReadmeAll,
  generateReadmeRaw,
} from "../controllers/readme.controller.js";

const router = express.Router();

// GET  /api/readme/languages
// Returns the list of all 15 supported language codes, names, and text direction.
router.get("/languages", getSupportedLanguages);

// POST /api/readme/generate
// Generates a README in ONE selected language.
// Body: { language, name, description, features?, techStack?, repoUrl?, license?, format? }
// Set format: "raw" to receive a Markdown file download instead of JSON.
router.post("/generate", generateReadme);

// POST /api/readme/generate/bulk
// Generates README in MULTIPLE selected languages at once.
// Body: { languages: ["en","es","fr"], name, description, features?, techStack?, repoUrl?, license? }
router.post("/generate/bulk", generateReadmeBulk);

// POST /api/readme/generate/all
// Generates README in ALL 15 languages at once.
// Body: { name, description, features?, techStack?, repoUrl?, license? }
router.post("/generate/all", generateReadmeAll);

// GET  /api/readme/generate/:language
// Browser-friendly convenience endpoint — streams raw Markdown as a file download.
// Optional query params: name, description, features (CSV), techStack (CSV), repoUrl, license
// Example: GET /api/readme/generate/fr?name=MyApp&description=A+cool+app
router.get("/generate/:language", generateReadmeRaw);

export default router;
