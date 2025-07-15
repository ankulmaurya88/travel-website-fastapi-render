
// Fetch destinations from backend
fetch("http://localhost:8001/destinations")
  .then(res => res.json())
  .then(data => {
    const list = document.getElementById("dest-list");
    data.forEach(dest => {
      const div = document.createElement("div");
      div.className = "destination";
      div.innerHTML = `<h4>${dest.name}</h4><p>${dest.description}</p>`;
      list.appendChild(div);
    });
  });

// Handle contact form submission
document.getElementById("contact-form").addEventListener("submit", function (e) {
  e.preventDefault();
  const formData = new FormData(this);
  const payload = Object.fromEntries(formData.entries());

  fetch("http://localhost:8001/contact", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(payload),
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("form-status").textContent = data.message;
  });
});
