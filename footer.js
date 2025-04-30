document.addEventListener("DOMContentLoaded", function () {
  // Ano atual
  const ano = new Date().getFullYear();
  const anoSpan = document.getElementById("anoAtual");
  if (anoSpan) anoSpan.textContent = ano;

  // Data de modificação (last modified do documento)
  const mod = new Date(document.lastModified);
  const dataFormatada = mod.toLocaleString("pt-PT", {
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });

  const dataSpan = document.getElementById("dataModificacao");
  if (dataSpan) dataSpan.textContent = dataFormatada;
});
document.addEventListener("DOMContentLoaded", function () {
  // Ano atual
  const ano = new Date().getFullYear();
  const anoSpan = document.getElementById("anoAtual");
  if (anoSpan) anoSpan.textContent = ano;

  // Data de modificação (last modified do documento)
  const mod = new Date(document.lastModified);
  const dataFormatada = mod.toLocaleString("pt-PT", {
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });

  const dataSpan = document.getElementById("dataModificacao");
  if (dataSpan) dataSpan.textContent = dataFormatada;
});
