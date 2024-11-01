import React from "react";
import { DocsThemeConfig } from "nextra-theme-docs";

const config: DocsThemeConfig = {
  logo: <span>Sieci</span>,
  project: {
    link: "https://github.com/barszu/sieci-komputerowe",
  },
  docsRepositoryBase: "https://github.com/barszu/sieci-komputerowe/tree/main",
  editLink: {
    text: null,
  },
  feedback: {
    content: "Zauważyłeś błąd, masz pomysł co poprawić - to zgłoś propozycję!",
  },
  footer: {
    text: "Notatki z sieci, autor Bartłomiej Szubiak",
  },
};

export default config;
