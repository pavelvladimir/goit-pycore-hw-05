import clsx from "clsx";
import Link from "@docusaurus/Link";
import Layout from "@theme/Layout";
import styles from "./index.module.css";

const cards = [
  {
    title: "Project Docs",
    text: "Task notes, run instructions, and the structure of the repository.",
    href: "/docs/intro",
  },
  {
    title: "Python API",
    text: "Reference pages generated from Python docstrings through Sphinx.",
    href: "/python-api",
  },
  {
    title: "Task 1",
    text: "Closure-based Fibonacci caching with recursive calculation and result reuse.",
    href: "/docs/tasks/task-01",
  },
  {
    title: "Task 2",
    text: "Generator-based profit extraction from text with regex-powered number parsing.",
    href: "/docs/tasks/task-02",
  },
];

function Card({ title, text, href }) {
  return (
    <Link className={styles.cardLink} to={href}>
      <article className={styles.card}>
        <h3>{title}</h3>
        <p>{text}</p>
      </article>
    </Link>
  );
}

export default function Home() {
  return (
    <Layout
      title="Python Homework Docs"
      description="Docusaurus and Sphinx documentation for Python homework tasks"
    >
      <main className={styles.page}>
        <section className={styles.hero}>
          <div className={styles.heroCopy}>
            <p className={styles.eyebrow}>Python homework documentation</p>
            <h1>One docs site for Python homework notes, usage guides, and API reference.</h1>
            <p className={styles.lead}>
              This project combines Docusaurus for the main docs experience,
              Sphinx for API pages generated from Python docstrings, and a
              small `uv`-based Python homework workflow.
            </p>
            <div className={styles.actions}>
              <Link className={clsx("button button--primary", styles.primary)} to="/docs/intro">
                Open docs
              </Link>
              <Link className={clsx("button button--secondary", styles.secondary)} to="/python-api">
                Open API
              </Link>
            </div>
          </div>
          <div className={styles.heroPanel}>
            <div className={styles.commandBlock}>
              <span>Python</span>
              <code>uv run python main.py</code>
            </div>
            <div className={styles.commandBlock}>
              <span>Tests</span>
              <code>uv run python -m unittest discover -s tests -q</code>
            </div>
            <div className={styles.commandBlock}>
              <span>Docs</span>
              <code>pnpm docs:start</code>
            </div>
          </div>
        </section>

        <section className={styles.grid}>
          {cards.map((card) => (
            <Card key={card.href} {...card} />
          ))}
        </section>
      </main>
    </Layout>
  );
}
