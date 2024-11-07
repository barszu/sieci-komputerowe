export function Details({
  children,
  summary = "Kliknij, aby zobaczyć więcej",
  ml = "1.5em",
}) {
  return (
    <details
      style={{
        border: "1px solid #403938",
        borderRadius: "4px",
        padding: "0.5em",
        margin: `0.1em {ml}`,
        cursor: "pointer",
      }}
    >
      <summary>
        <i>{summary}</i>
      </summary>
      {children}
    </details>
  );
}

export default Details;
