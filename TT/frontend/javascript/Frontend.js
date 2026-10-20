async function def() {
  let reg = true
  console.log("Clicked");

  const output = document.getElementById('gg');
  const input_text = document.getElementById('ggg');

  output.textContent = 'Waiting For Answer';
  const data = parseInt(input_text.value);

  if (typeof data === "number") {
    output.textContent == `Invalid type...`
    reg = false
  }

  if (reg === true) {
    try {
      const response = await fetch('http://localhost/p', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: data })
      });

      const serverData = await response.json();
      console.log(serverData);
      
      if (serverData.status === "success") {
          output.textContent = `Server Answer: ${serverData.message}`;
      } else if (serverData.status === "error") {
          output.textContent = `Server Error: ${serverData.message}`;
      } else {
        output.textContent == `Server Error: ..Unknown..`
      }

    } catch (error) {
      console.log('error', error);
      output.textContent = 'Critical connection error!';
    }
  } else {
    output.textContent = 'Critical Valid'
  }
}
