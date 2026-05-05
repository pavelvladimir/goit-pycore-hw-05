const config = {
  title: "Python Homework Docs",
  tagline: "Docusaurus site with Python API docs generated from docstrings",
  url: "https://example.com",
  baseUrl: "/",
  organizationName: "paveltravnicek",
  projectName: "goit-pycore-hw-05",
  onBrokenLinks: "throw",
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: "warn",
    },
  },
  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },
  presets: [
    [
      "classic",
      {
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
          routeBasePath: "docs",
        },
        blog: false,
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      },
    ],
  ],
  themeConfig: {
    navbar: {
      title: "Python Homework Docs",
      items: [
        {
          type: "docSidebar",
          sidebarId: "tutorialSidebar",
          position: "left",
          label: "Docs",
        },
        {
          to: "/python-api",
          label: "API",
          position: "left",
        },
      ],
    },
    footer: {
      style: "dark",
      links: [
        {
          title: "Documentation",
          items: [
            {
              label: "Overview",
              to: "/docs/intro",
            },
            {
              label: "Python API",
              to: "/python-api",
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Python Homework Docs.`,
    },
  },
};

module.exports = config;
