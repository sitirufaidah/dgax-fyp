function deleteRecord(recordId) {
  fetch("/delete-record", {
    method:"POST",
    body: JSON.stringify({ recordId: recordId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function startAnalyse(id, num1, num2, num3, num4, num5, num6, num7) {
  fetch("start-analyse", {
    method: "POST",
    body: JSON.stringify({ id: id, hydrogen: num1 , methane: num2, acetylene: num3, ethylene: num4, ethane: num5, carbonmonoxide: num6, carbondioxide: num7}),
  }).then((_res) => {
    window.location.href = "/";
  });
}
