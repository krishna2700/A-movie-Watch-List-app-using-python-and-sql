const http = require("http");
const fs = require("fs");
const path = require("path");

// ── Language Templates (15 languages) ─────────────────────────────────────────

const LANGUAGES = {
  en: {
    name: "English", direction: "ltr",
    s: {
      overview: "Overview", features: "Features", tech: "Tech Stack",
      install: "Installation", usage: "Usage", contrib: "Contributing", license: "License",
      contribText: "Contributions are welcome! Please open an issue or submit a pull request.",
      licenseText: (l) => `This project is licensed under the ${l} License.`,
      defaultDesc: "A brief description of what this project does.",
      defaultFeatures: ["Easy to use", "Well documented", "Highly configurable"],
    },
  },
  es: {
    name: "Spanish (Español)", direction: "ltr",
    s: {
      overview: "Descripción general", features: "Características", tech: "Tecnologías",
      install: "Instalación", usage: "Uso", contrib: "Contribuciones", license: "Licencia",
      contribText: "¡Las contribuciones son bienvenidas! Por favor abre un issue o envía un pull request.",
      licenseText: (l) => `Este proyecto está licenciado bajo la Licencia ${l}.`,
      defaultDesc: "Una breve descripción del proyecto.",
      defaultFeatures: ["Fácil de usar", "Bien documentado", "Altamente configurable"],
    },
  },
  fr: {
    name: "French (Français)", direction: "ltr",
    s: {
      overview: "Présentation", features: "Fonctionnalités", tech: "Technologies",
      install: "Installation", usage: "Utilisation", contrib: "Contributions", license: "Licence",
      contribText: "Les contributions sont les bienvenues ! Veuillez ouvrir une issue ou soumettre une pull request.",
      licenseText: (l) => `Ce projet est sous licence ${l}.`,
      defaultDesc: "Une brève description du projet.",
      defaultFeatures: ["Facile à utiliser", "Bien documenté", "Hautement configurable"],
    },
  },
  de: {
    name: "German (Deutsch)", direction: "ltr",
    s: {
      overview: "Übersicht", features: "Funktionen", tech: "Technologien",
      install: "Installation", usage: "Verwendung", contrib: "Mitwirken", license: "Lizenz",
      contribText: "Beiträge sind willkommen! Bitte öffne ein Issue oder sende einen Pull Request.",
      licenseText: (l) => `Dieses Projekt steht unter der ${l}-Lizenz.`,
      defaultDesc: "Eine kurze Beschreibung des Projekts.",
      defaultFeatures: ["Einfach zu bedienen", "Gut dokumentiert", "Hochkonfigurierbar"],
    },
  },
  zh: {
    name: "Chinese Simplified (中文)", direction: "ltr",
    s: {
      overview: "项目概述", features: "功能特性", tech: "技术栈",
      install: "安装", usage: "使用方法", contrib: "贡献", license: "许可证",
      contribText: "欢迎贡献！请提交 Issue 或 Pull Request。",
      licenseText: (l) => `本项目基于 ${l} 许可证开源。`,
      defaultDesc: "项目的简要描述。",
      defaultFeatures: ["易于使用", "文档完善", "高度可配置"],
    },
  },
  ja: {
    name: "Japanese (日本語)", direction: "ltr",
    s: {
      overview: "概要", features: "機能", tech: "技術スタック",
      install: "インストール", usage: "使い方", contrib: "コントリビューション", license: "ライセンス",
      contribText: "コントリビューションを歓迎します！Issue を開くか Pull Request を送ってください。",
      licenseText: (l) => `このプロジェクトは ${l} ライセンスの下に公開されています。`,
      defaultDesc: "プロジェクトの簡単な説明。",
      defaultFeatures: ["使いやすい", "ドキュメントが充実", "高い設定可能性"],
    },
  },
  pt: {
    name: "Portuguese (Português)", direction: "ltr",
    s: {
      overview: "Visão Geral", features: "Funcionalidades", tech: "Tecnologias",
      install: "Instalação", usage: "Uso", contrib: "Contribuições", license: "Licença",
      contribText: "Contribuições são bem-vindas! Abra uma issue ou envie um pull request.",
      licenseText: (l) => `Este projeto está licenciado sob a Licença ${l}.`,
      defaultDesc: "Uma breve descrição do projeto.",
      defaultFeatures: ["Fácil de usar", "Bem documentado", "Altamente configurável"],
    },
  },
  hi: {
    name: "Hindi (हिन्दी)", direction: "ltr",
    s: {
      overview: "अवलोकन", features: "विशेषताएं", tech: "तकनीकी स्टैक",
      install: "इंस्टॉलेशन", usage: "उपयोग", contrib: "योगदान", license: "लाइसेंस",
      contribText: "योगदान स्वागत योग्य है! कृपया एक issue खोलें या pull request सबमिट करें।",
      licenseText: (l) => `यह प्रोजेक्ट ${l} लाइसेंस के अंतर्गत है।`,
      defaultDesc: "प्रोजेक्ट का संक्षिप्त विवरण।",
      defaultFeatures: ["उपयोग में आसान", "अच्छी तरह प्रलेखित", "उच्च कॉन्फ़िगर करने योग्य"],
    },
  },
  ar: {
    name: "Arabic (العربية)", direction: "rtl",
    s: {
      overview: "نظرة عامة", features: "الميزات", tech: "التقنيات المستخدمة",
      install: "التثبيت", usage: "الاستخدام", contrib: "المساهمة", license: "الرخصة",
      contribText: "المساهمات مرحب بها! يرجى فتح issue أو إرسال pull request.",
      licenseText: (l) => `هذا المشروع مرخص بموجب رخصة ${l}.`,
      defaultDesc: "وصف مختصر للمشروع.",
      defaultFeatures: ["سهل الاستخدام", "موثق جيداً", "قابل للتهيئة بشكل كبير"],
    },
  },
  ru: {
    name: "Russian (Русский)", direction: "ltr",
    s: {
      overview: "Обзор", features: "Возможности", tech: "Технологии",
      install: "Установка", usage: "Использование", contrib: "Участие в разработке", license: "Лицензия",
      contribText: "Вклад приветствуется! Пожалуйста, откройте issue или отправьте pull request.",
      licenseText: (l) => `Этот проект распространяется под лицензией ${l}.`,
      defaultDesc: "Краткое описание проекта.",
      defaultFeatures: ["Простота использования", "Хорошая документация", "Высокая настраиваемость"],
    },
  },
  ko: {
    name: "Korean (한국어)", direction: "ltr",
    s: {
      overview: "개요", features: "기능", tech: "기술 스택",
      install: "설치", usage: "사용법", contrib: "기여", license: "라이선스",
      contribText: "기여를 환영합니다! Issue를 열거나 Pull Request를 제출해 주세요.",
      licenseText: (l) => `이 프로젝트는 ${l} 라이선스에 따라 배포됩니다.`,
      defaultDesc: "이 프로젝트에 대한 간략한 설명입니다.",
      defaultFeatures: ["사용하기 쉬운", "문서화 잘 됨", "고도로 구성 가능"],
    },
  },
  it: {
    name: "Italian (Italiano)", direction: "ltr",
    s: {
      overview: "Panoramica", features: "Funzionalità", tech: "Tecnologie Utilizzate",
      install: "Installazione", usage: "Utilizzo", contrib: "Contributi", license: "Licenza",
      contribText: "I contributi sono benvenuti! Apri un issue o invia una pull request.",
      licenseText: (l) => `Questo progetto è distribuito con la Licenza ${l}.`,
      defaultDesc: "Una breve descrizione del progetto.",
      defaultFeatures: ["Facile da usare", "Ben documentato", "Altamente configurabile"],
    },
  },
  nl: {
    name: "Dutch (Nederlands)", direction: "ltr",
    s: {
      overview: "Overzicht", features: "Functies", tech: "Gebruikte Technologieën",
      install: "Installatie", usage: "Gebruik", contrib: "Bijdragen", license: "Licentie",
      contribText: "Bijdragen zijn welkom! Open een issue of dien een pull request in.",
      licenseText: (l) => `Dit project is gelicenseerd onder de ${l} Licentie.`,
      defaultDesc: "Een korte beschrijving van het project.",
      defaultFeatures: ["Gemakkelijk te gebruiken", "Goed gedocumenteerd", "Zeer configureerbaar"],
    },
  },
  tr: {
    name: "Turkish (Türkçe)", direction: "ltr",
    s: {
      overview: "Genel Bakış", features: "Özellikler", tech: "Kullanılan Teknolojiler",
      install: "Kurulum", usage: "Kullanım", contrib: "Katkıda Bulunma", license: "Lisans",
      contribText: "Katkılarınızı bekliyoruz! Lütfen bir issue açın veya pull request gönderin.",
      licenseText: (l) => `Bu proje ${l} Lisansı kapsamında lisanslanmıştır.`,
      defaultDesc: "Projenin kısa bir açıklaması.",
      defaultFeatures: ["Kullanımı kolay", "İyi belgelenmiş", "Yüksek düzeyde yapılandırılabilir"],
    },
  },
  pl: {
    name: "Polish (Polski)", direction: "ltr",
    s: {
      overview: "Przegląd", features: "Funkcje", tech: "Użyte Technologie",
      install: "Instalacja", usage: "Użycie", contrib: "Wkład", license: "Licencja",
      contribText: "Wkłady są mile widziane! Otwórz issue lub wyślij pull request.",
      licenseText: (l) => `Ten projekt jest objęty licencją ${l}.`,
      defaultDesc: "Krótki opis projektu.",
      defaultFeatures: ["Łatwy w użyciu", "Dobrze udokumentowany", "Wysoko konfigurowalny"],
    },
  },
};

// ── README Builder ─────────────────────────────────────────────────────────────

function normalizeArray(val) {
  if (!val) return null;
  if (Array.isArray(val)) return val.filter(Boolean);
  return val.split(",").map((v) => v.trim()).filter(Boolean);
}

function buildReadme(langCode, p) {
  const { s } = LANGUAGES[langCode];
  const slug = (p.name || "my-project").toLowerCase().replace(/\s+/g, "-");
  const repo = p.repoUrl || `https://github.com/your-username/${slug}`;
  const license = p.license || "MIT";
  const features = normalizeArray(p.features) || s.defaultFeatures;
  const techStack = normalizeArray(p.techStack) || [];
  const description = p.description || s.defaultDesc;

  const techSection = techStack.length
    ? `## ${s.tech}\n\n${techStack.map((t) => `- ${t}`).join("\n")}\n\n`
    : "";

  return `# ${p.name}

## ${s.overview}

${description}

## ${s.features}

${features.map((f) => `- ${f}`).join("\n")}

${techSection}## ${s.install}

\`\`\`bash
git clone ${repo}
cd ${slug}
npm install
\`\`\`

## ${s.usage}

\`\`\`bash
npm start
\`\`\`

## ${s.contrib}

${s.contribText}

## ${s.license}

${s.licenseText(license)}
`;
}

// ── Utility helpers ────────────────────────────────────────────────────────────

const SAVE_DIR = path.join(__dirname, "readme-api-files");

function sendJSON(res, status, data) {
  const body = JSON.stringify(data, null, 2);
  res.writeHead(status, {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, DELETE, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Content-Length": Buffer.byteLength(body),
  });
  res.end(body);
}

function parseBody(req) {
  return new Promise((resolve, reject) => {
    let body = "";
    req.on("data", (c) => (body += c));
    req.on("end", () => {
      try { resolve(body ? JSON.parse(body) : {}); }
      catch { reject(new Error("Invalid JSON body")); }
    });
  });
}

function saveFile(filename, content) {
  if (!fs.existsSync(SAVE_DIR)) fs.mkdirSync(SAVE_DIR, { recursive: true });
  const filePath = path.join(SAVE_DIR, filename);
  fs.writeFileSync(filePath, content, "utf-8");
  return filePath;
}

// ── Request Router ─────────────────────────────────────────────────────────────

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, "http://localhost");
  const pathname = url.pathname;
  const method = req.method;

  // CORS preflight
  if (method === "OPTIONS") {
    res.writeHead(204, {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, POST, DELETE, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
    });
    return res.end();
  }

  // ── GET / ────────────────────────────────────────────────────────────────────
  if (method === "GET" && pathname === "/") {
    return sendJSON(res, 200, {
      name: "README Generator API",
      version: "2.0.0",
      description: "Generate professional README.md files in 15 languages",
      supportedLanguages: Object.keys(LANGUAGES).length,
      endpoints: [
        { method: "GET",    path: "/",                         description: "API documentation (this page)" },
        { method: "GET",    path: "/health",                   description: "Health check" },
        { method: "GET",    path: "/languages",                description: "List all 15 supported language codes" },
        { method: "POST",   path: "/generate",                 description: "Generate README in ONE selected language" },
        { method: "POST",   path: "/generate/bulk",            description: "Generate README in MULTIPLE selected languages" },
        { method: "POST",   path: "/generate/all",             description: "Generate README in ALL 15 languages at once" },
        { method: "GET",    path: "/saved",                    description: "List all saved README files" },
        { method: "GET",    path: "/saved/:filename",          description: "Get content of a saved README" },
        { method: "DELETE", path: "/saved/:filename",          description: "Delete a saved README" },
      ],
      requestBody: {
        "/generate": {
          required: { language: "string (e.g. 'en', 'es', 'fr', 'de', 'zh', 'ja', 'pt', 'hi', 'ar', 'ru', 'ko', 'it', 'nl', 'tr', 'pl')", name: "string — project name", description: "string — project description" },
          optional: { features: "array or CSV string of features", techStack: "array or CSV string of technologies", repoUrl: "string — GitHub/repo URL", license: "string (default: MIT)", save: "boolean — save file to disk (default: false)" },
        },
        "/generate/bulk": { same_as: "/generate but", languages: "array of language codes instead of a single language" },
        "/generate/all": { same_as: "/generate but", note: "Generates for ALL 15 languages — no language field needed" },
      },
    });
  }

  // ── GET /health ──────────────────────────────────────────────────────────────
  if (method === "GET" && pathname === "/health") {
    return sendJSON(res, 200, { status: "ok", uptime: Math.round(process.uptime()) + "s", timestamp: new Date().toISOString() });
  }

  // ── GET /languages ───────────────────────────────────────────────────────────
  if (method === "GET" && pathname === "/languages") {
    return sendJSON(res, 200, {
      count: Object.keys(LANGUAGES).length,
      languages: Object.entries(LANGUAGES).map(([code, l]) => ({ code, name: l.name, direction: l.direction })),
    });
  }

  // ── POST /generate ───────────────────────────────────────────────────────────
  if (method === "POST" && pathname === "/generate") {
    let body;
    try { body = await parseBody(req); } catch (e) { return sendJSON(res, 400, { error: e.message }); }

    const { language = "en", name, description, features, techStack, repoUrl = "", license = "MIT", save = false } = body;

    if (!name?.trim()) return sendJSON(res, 400, { error: 'Missing required field: "name"' });
    if (!description?.trim()) return sendJSON(res, 400, { error: 'Missing required field: "description"' });

    const langCode = language.toLowerCase();
    if (!LANGUAGES[langCode]) {
      return sendJSON(res, 400, { error: `Unsupported language: "${language}"`, supportedCodes: Object.keys(LANGUAGES) });
    }

    const content = buildReadme(langCode, { name: name.trim(), description: description.trim(), features, techStack, repoUrl, license });
    const langInfo = LANGUAGES[langCode];
    const filename = langCode === "en" ? "README.md" : `README.${langCode}.md`;
    const result = { success: true, language: { code: langCode, name: langInfo.name, direction: langInfo.direction }, filename, content };

    if (save) { result.savedTo = saveFile(filename, content); }
    return sendJSON(res, 201, result);
  }

  // ── POST /generate/bulk ──────────────────────────────────────────────────────
  if (method === "POST" && pathname === "/generate/bulk") {
    let body;
    try { body = await parseBody(req); } catch (e) { return sendJSON(res, 400, { error: e.message }); }

    const { languages = ["en"], name, description, features, techStack, repoUrl = "", license = "MIT", save = false } = body;

    if (!name?.trim()) return sendJSON(res, 400, { error: 'Missing required field: "name"' });
    if (!description?.trim()) return sendJSON(res, 400, { error: 'Missing required field: "description"' });
    if (!Array.isArray(languages) || languages.length === 0) {
      return sendJSON(res, 400, { error: '"languages" must be a non-empty array of language codes' });
    }

    const params = { name: name.trim(), description: description.trim(), features, techStack, repoUrl, license };
    const results = [];
    const errors = [];

    for (const lang of languages) {
      const langCode = lang.toLowerCase();
      if (!LANGUAGES[langCode]) { errors.push({ language: lang, error: `Unsupported code: "${lang}"` }); continue; }
      const content = buildReadme(langCode, params);
      const filename = langCode === "en" ? "README.md" : `README.${langCode}.md`;
      const entry = { language: { code: langCode, name: LANGUAGES[langCode].name, direction: LANGUAGES[langCode].direction }, filename, content };
      if (save) { entry.savedTo = saveFile(filename, content); }
      results.push(entry);
    }

    return sendJSON(res, 201, { success: true, generated: results.length, failed: errors.length, results, ...(errors.length && { errors }) });
  }

  // ── POST /generate/all ───────────────────────────────────────────────────────
  if (method === "POST" && pathname === "/generate/all") {
    let body;
    try { body = await parseBody(req); } catch (e) { return sendJSON(res, 400, { error: e.message }); }

    const { name, description, features, techStack, repoUrl = "", license = "MIT", save = false } = body;
    if (!name?.trim()) return sendJSON(res, 400, { error: 'Missing required field: "name"' });
    if (!description?.trim()) return sendJSON(res, 400, { error: 'Missing required field: "description"' });

    const params = { name: name.trim(), description: description.trim(), features, techStack, repoUrl, license };
    const readmes = Object.keys(LANGUAGES).map((langCode) => {
      const content = buildReadme(langCode, params);
      const filename = langCode === "en" ? "README.md" : `README.${langCode}.md`;
      const entry = { language: { code: langCode, name: LANGUAGES[langCode].name, direction: LANGUAGES[langCode].direction }, filename, content };
      if (save) { entry.savedTo = saveFile(filename, content); }
      return entry;
    });

    return sendJSON(res, 201, { success: true, count: readmes.length, readmes });
  }

  // ── GET /saved ───────────────────────────────────────────────────────────────
  if (method === "GET" && pathname === "/saved") {
    try {
      if (!fs.existsSync(SAVE_DIR)) return sendJSON(res, 200, { success: true, count: 0, files: [] });
      const files = fs.readdirSync(SAVE_DIR).filter((f) => f.endsWith(".md")).map((filename) => {
        const stats = fs.statSync(path.join(SAVE_DIR, filename));
        return { filename, sizeBytes: stats.size, modifiedAt: stats.mtime };
      });
      return sendJSON(res, 200, { success: true, count: files.length, files });
    } catch (e) { return sendJSON(res, 500, { error: e.message }); }
  }

  // ── GET /saved/:filename ─────────────────────────────────────────────────────
  const savedMatch = pathname.match(/^\/saved\/([^/]+\.md)$/);
  if (method === "GET" && savedMatch) {
    const filename = savedMatch[1];
    const filePath = path.join(SAVE_DIR, filename);
    if (!fs.existsSync(filePath)) return sendJSON(res, 404, { error: `File "${filename}" not found` });
    return sendJSON(res, 200, { success: true, filename, content: fs.readFileSync(filePath, "utf-8") });
  }

  // ── DELETE /saved/:filename ──────────────────────────────────────────────────
  const deleteMatch = pathname.match(/^\/saved\/([^/]+\.md)$/);
  if (method === "DELETE" && deleteMatch) {
    const filename = deleteMatch[1];
    const filePath = path.join(SAVE_DIR, filename);
    if (!fs.existsSync(filePath)) return sendJSON(res, 404, { error: `File "${filename}" not found` });
    fs.unlinkSync(filePath);
    return sendJSON(res, 200, { success: true, message: `"${filename}" deleted successfully` });
  }

  return sendJSON(res, 404, { error: "Endpoint not found", hint: "Visit GET / for API documentation" });
});

server.listen(3456, () => {
  console.log("README Generator API v2.0 running on http://localhost:3456");
  console.log("API docs: GET http://localhost:3456/");
});
