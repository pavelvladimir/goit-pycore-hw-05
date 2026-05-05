import { useEffect } from "react";
import Layout from "@theme/Layout";
import useBaseUrl from "@docusaurus/useBaseUrl";

export default function PythonApiPage() {
  const apiUrl = useBaseUrl("/api/index.html");

  useEffect(() => {
    window.location.replace(apiUrl);
  }, [apiUrl]);

  return (
    <Layout title="Python API" description="Redirecting to the generated Python API reference">
      <main style={{ padding: "4rem 1.5rem", textAlign: "center" }}>
        <h1>Opening Python API Reference</h1>
        <p>If the redirect does not happen automatically, use the link below.</p>
        <p>
          <a href={apiUrl}>Open the generated API documentation</a>
        </p>
      </main>
    </Layout>
  );
}
