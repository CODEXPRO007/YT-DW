async function fetchVideo() {
  const url = document.getElementById("url").value;

  const res = await fetch(`/api/download?url=${encodeURIComponent(url)}`, {
    headers: {
      "X-API-KEY": "PREMIUM999"   // change to PREMIUM999
    }
  });

  const data = await res.json();

  if (data.error) {
    alert(data.error);
    return;
  }

  document.getElementById("output").innerHTML = `
    <h3>${data.title}</h3>
    <a href="${data.video}" target="_blank"> Download Video Now ⬇️</a><br>
    ${data.audio ? `<a href="${data.audio}" target="_blank">🎵 Download Audio</a>` : "<p>🔒 Audio Premium Only</p>"}
  `;
}
