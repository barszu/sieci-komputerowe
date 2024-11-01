const withNextra = require("nextra")({
  theme: "nextra-theme-docs",
  themeConfig: "./theme.config.tsx",
  latex: true,
  defaultShowCopyCode: true,
});

module.exports = withNextra({
  images: {
    unoptimized: true,
  },
  output: "export",
  trailingSlash: true,
  basePath: "/sieci-komputerowe",
});
