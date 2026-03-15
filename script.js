
fetch("data.json")
.then(response => response.json())
.then(data => {

const table = document.getElementById("prixTable")
const rendementList = document.getElementById("rendementList")

data.villes.forEach(v => {

let row = document.createElement("tr")

row.innerHTML = `
<td>${v.ville}</td>
<td>${v.prix}</td>
`

table.appendChild(row)

let item = document.createElement("li")
item.textContent = v.ville + " : " + v.rendement + "%"

rendementList.appendChild(item)

})

})
.catch(error => {
console.error("Erreur chargement données:", error)
})
