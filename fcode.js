let people = [];

function addPerson() {
  const name = document.getElementById("name").value.trim();
  const paid = parseFloat(document.getElementById("paid").value);

  if (name === "" || isNaN(paid)) {
    alert("Please enter a valid name and amount");
    return;
  }

  people.push({ name, paid });
  document.getElementById("name").value = "";
  document.getElementById("paid").value = "";

  updatePeopleTable();
}

function updatePeopleTable() {
  const tbody = document.getElementById("peopleTableBody");
  tbody.innerHTML = "";

  people.forEach(person => {
    const row = document.createElement("tr");
    row.innerHTML = `<td>${person.name}</td><td>₹${person.paid.toFixed(2)}</td>`;
    tbody.appendChild(row);
  });

  document.getElementById("totalPeople").innerText = people.length;
}

function calculateSplit() {
  if (people.length === 0) {
    alert("No people added.");
    return;
  }

  const total = people.reduce((sum, p) => sum + p.paid, 0);
  const equalShare = total / people.length;

  const balances = people.map(p => {
    const balance = p.paid - equalShare;
    return {
      name: p.name,
      balance: balance.toFixed(2),
      status: balance > 0 ? "Gets Back" : balance < 0 ? "Owes" : "Settled"
    };
  });

  updateBalancesTable(balances);
}

function updateBalancesTable(balances) {
  const tbody = document.getElementById("balancesTableBody");
  tbody.innerHTML = "";

  balances.forEach(person => {
    const row = document.createElement("tr");
    row.innerHTML = `<td>${person.name}</td><td>${person.balance}</td><td>${person.status}</td>`;
    tbody.appendChild(row);
  });
}
